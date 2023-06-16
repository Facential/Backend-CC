from flask import Flask, request, jsonify, render_template
import tensorflow as tf
from tensorflow.keras.models import load_model
import os
import uuid
import requests
import logging
import datetime
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, storage, auth
import pymysql.cursors
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, API_WEATHER, API_POLLUTION
from skin_products import overall_conditions, cleansing_products, toner_products, serum_products, moisturizer_products, sunscreen_products


app = Flask(__name__)

# Initialize Firebase
cred = credentials.Certificate('service_account_key.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'usersface'
})
bucket = storage.bucket()

# Load the model
model = load_model('model.h5')

# Define class labels
class_labels = class_labels = {0: 'Oily', 1: 'Normal',2: 'Sensitive' , 3: 'Dry', 4:'nonface', 5:"Combination" }  # Example mapping of class indices to labels

# Connect to MySQL
def create_connection():
    connection = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        db=DB_NAME,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor,
        init_command='SET time_zone = "+07:00"'
    )
    return connection

def preprocess_image(image):
    # Normalize pixel values to the range [0, 1]
    image = image / 255.0

    # Perform any other preprocessing steps such as resizing, cropping, etc.
    # ...

    return image

@app.route('/', methods=['GET'])
def success():
    if request.method == 'GET':
        response = {
            'message': 'Success!'
        }
        return render_template('index.html'), 200
    else:
        response = {
            'message': 'Error: Resource not found.'
        }
        return jsonify(response), 404

#E.Classifiy
@app.route('/classify', methods=['POST'])
def classify_skin_type():
    # Generate a unique name for the image
    unique_filename = str(uuid.uuid4()) + '.jpg'

    # Get the image file from the request
    image_file = request.files['image']

    # Save the file to a temporary location
    temp_path = 'temp_image.jpg'
    image_file.save(temp_path)

    # Load and preprocess the image
    image = tf.keras.preprocessing.image.load_img(temp_path, target_size=(224, 224))
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = preprocess_image(image)  # Preprocess the image as per your model's requirements

    # Add a batch dimension to the image
    image = tf.expand_dims(image, axis=0)

    # Perform inference
    predictions = model.predict(image)

    # Process the predictions
    predicted_classes = tf.argmax(predictions, axis=1)
    predicted_label = class_labels[predicted_classes[0].numpy()]

    # # Delete the temporary file
    # os.remove(temp_path)

    if predicted_label != 'nonface' and predicted_classes[0].numpy() != 4:
        # Upload the image to Firebase storage
        blob = bucket.blob('images/' + unique_filename)
        blob.upload_from_filename(temp_path)

        # Get the public URL of the uploaded image
        image_url = blob.public_url

        #Delete the temporary file
        os.remove(temp_path)

        user_uid = request.form.get('Authorization')

        # Connect to MySQL
        connection = create_connection()

        try:
            with connection.cursor() as cursor:
                # Insert the classification result into the database
                sql = "INSERT INTO classification_results (user_uid, skin_type, image_url) VALUES (%s, %s, %s)"
                cursor.execute(sql, (user_uid, predicted_classes[0].numpy(), image_url))
                connection.commit()

        finally:
            # Close the database connection
            connection.close()

        # Return the predicted skin type as the API response
        response = {
            'skin_type': predicted_label
        }
        return jsonify(response), 200
    else:
        os.remove(temp_path)
        # Set response message for non-face image
        response = {
            'message': 'Image does not contain a valid face.'
        }
        return jsonify(response), 400
    
#E.Get All Data
@app.route('/getdata/<user_uid>', methods=['GET'])
def get_all_data(user_uid):
    # Connect to MySQL
    connection = create_connection()

    try:
        with connection.cursor() as cursor:
            # Retrieve all data for the specified user UID
            sql = "SELECT * FROM classification_results WHERE user_uid = %s"
            cursor.execute(sql, (user_uid,))
            result = cursor.fetchall()

        if result:
            # Convert the skin type numbers to corresponding text
            for record in result:
                record['skin_type'] = class_labels[record['skin_type']]
                # Format the timestamp without seconds and "GMT" text
                record['timestamp'] = record['timestamp'].strftime("%a, %d %b %Y %H:%M")

            response = {
                "history": result,
                "message": "success",
                "status": 200
            }
            return jsonify(response)
        else:
            # If no result found, return an empty result
            response = {
                'message': 'No data found for the specified user UID.',
                'status': 404
            }
            return jsonify(response), 404

    except Exception as e:
        response = {
            'message': 'Error: Failed to retrieve the data.',
            'error': str(e),
            'status': 500
        }
        return jsonify(response), 500

    finally:
        # Close the database connection
        connection.close()


#E.Get Spesific Data
@app.route('/getdata/<user_uid>/<id>', methods=['GET'])
def get_spesific_data(user_uid, id):
    # Connect to MySQL
    connection = create_connection()
    skin_labels = {0: 'Oily', 1: 'Normal',2: 'Sensitive' , 3: 'Dry', 4:'nonface', 5:"Combination" }

    try:
        with connection.cursor() as cursor:
            # Retrieve the specific data record for the specified user UID and ID
            sql = "SELECT * FROM classification_results WHERE user_uid = %s AND id = %s"
            cursor.execute(sql, (user_uid, id))
            result = cursor.fetchone()

        if result:
            # Convert the skin type number to corresponding text
            result['skin_type'] = skin_labels[int(result['skin_type'])]
            result['overall'] = get_overall_condition(result['skin_type'])
            result['cleansing'] = get_cleansing_product(result['skin_type'])
            result['toner'] = get_toner_product(result['skin_type'])
            result['serum'] = get_serum_product(result['skin_type'])
            result['moisturizer'] = get_moisturizer_product(result['skin_type'])
            result['sunscreen'] = get_sunscreen_product(result['skin_type'])

            return jsonify(result)
        else:
            # If no result found, return an empty result
            response = {
                'message': 'No data found for the specified user UID and ID.'
            }
            return jsonify(response), 404

    except Exception as e:
        response = {
            'message': 'Error: Failed to retrieve the data.',
            'error': str(e)
        }
        return jsonify(response), 500

    finally:
        # Close the database connection
        connection.close()

#E.Get Latest Data
@app.route('/getdata/<user_uid>/latest', methods=['GET'])
def get_latest_data(user_uid):
    # Connect to MySQL
    connection = create_connection()
    skin_labels = {0: 'Oily', 1: 'Normal',2: 'Sensitive' , 3: 'Dry', 4:'nonface', 5:"Combination" } 
    
    try:
        with connection.cursor() as cursor:
            # Retrieve the latest classification result for the specified user UID
            sql = "SELECT * FROM classification_results WHERE user_uid = %s ORDER BY id DESC LIMIT 1" 
            cursor.execute(sql, (user_uid,))
            result = cursor.fetchone()

        if result is not None:
            # Convert the skin type number to corresponding text
            result['skin_type'] = skin_labels[int(result['skin_type'])]
            result['overall'] = get_overall_condition(result['skin_type'])
            result['cleansing'] = get_cleansing_product(result['skin_type'])
            result['toner'] = get_toner_product(result['skin_type'])
            result['serum'] = get_serum_product(result['skin_type'])
            result['moisturizer'] = get_moisturizer_product(result['skin_type'])
            result['sunscreen'] = get_sunscreen_product(result['skin_type'])

            return jsonify(result)
        else:
            # If no result found, return an empty result
            response = {
                    'message': 'No classification results found for the specified user UID.'
                }
            return jsonify(response), 404

    finally:
        # Close the database connection
        connection.close()

#E.Delete All Data
@app.route('/delete/<user_uid>', methods=['DELETE'])
def delete_all_data(user_uid):
    # Connect to MySQL
    connection = create_connection()

    try:
        with connection.cursor() as cursor:
            # Retrieve the image_urls for the specified user UID
            sql = "SELECT image_url FROM classification_results WHERE user_uid = %s"
            cursor.execute(sql, (user_uid,))
            results = cursor.fetchall()

            if results:
                for result in results:
                    image_url = result['image_url']
                    # Remove the prefix from the image URL
                    image_path = image_url.replace('https://storage.googleapis.com/usersface/', '')
                    # Delete the image from Firebase storage
                    blob = bucket.blob(image_path)
                    blob.delete()

                # Delete the classification results from the database
                sql = "DELETE FROM classification_results WHERE user_uid = %s"
                cursor.execute(sql, (user_uid,))
                connection.commit()

                return jsonify({'message': 'Classification results deleted successfully.'}), 200
            else:
                return jsonify({'message': 'Classification results not found.'}), 404

    finally:
        # Close the database connection
        connection.close()

#Delete Spesific Data
@app.route('/delete/<user_uid>/<id>', methods=['DELETE'])
def delete_spesific_data(user_uid, id):
    # Connect to MySQL
    connection = create_connection()

    try:
        with connection.cursor() as cursor:
            # Check if the record exists
            sql = "SELECT * FROM classification_results WHERE `id` = %s AND `user_uid` = %s"
            cursor.execute(sql, (id, user_uid))
            record = cursor.fetchone()

            if record:
                # Delete the record
                sql = "DELETE FROM classification_results WHERE `id` = %s"
                cursor.execute(sql, id)
                connection.commit()

                response = {
                    'message': 'Record deleted successfully.'
                }
                return jsonify(response), 200
            else:
                response = {
                    'message': 'Error: Record not found.'
                }
                return jsonify(response), 404

    except Exception as e:
        response = {
            'message': 'Error: Failed to delete the record.',
            'error': str(e)
        }
        return jsonify(response), 500

    finally:
        connection.close()

# Configure logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/recommendation', methods=['POST'])
def get_recommendation():
    latitude = request.form.get('latitude')
    longitude = request.form.get('longitude')

    if latitude and longitude:
        weather_data = get_weather_data(latitude, longitude)
        pollution_data = get_pollution_data(latitude, longitude)

        if weather_data:
            temperature = weather_data['temperature']
            pollution_index = pollution_data['pollution_index'] if pollution_data else None

            # Log the temperature and pollution index values
            app.logger.debug(f"Temperature: {temperature}")
            app.logger.debug(f"Pollution Index: {pollution_index}")

            skincare_recommendation = get_skincare_recommendation(temperature, pollution_index)

            # Remove newline characters from skincare_recommendation
            skincare_recommendation = skincare_recommendation.replace('\n', '')

            data = {
                'temperature': f"{temperature}°",
                'pollution_index': pollution_index,
                'skincare_recommendation': skincare_recommendation
            }
            response ={
                'data': data,
                'message': 'success',
                'status': 200
            }
            return jsonify(response), 200
        else:
            data = {
                'temperature': None,
                'pollution_index': None,
                'skincare_recommendation': None,
            }
            response ={
                'data': data,
                'message': 'Failed to fetch weather data.',
                'status': 500
            }
            return jsonify(response), 500
    else:
        data = {
            'temperature': None,
            'pollution_index': None,
            'skincare_recommendation': None,
        }
        response = {
            'data': data,
            'message': 'Latitude and longitude are required parameters.',
            'status': 400
        }
        
        return jsonify(response), 400


def get_range_category(value, ranges):
    if value is None:
        return 'N/A'

    for category, (lower, upper) in ranges.items():
        if lower <= value <= upper:
            return category
    return None


def get_weather_data(latitude, longitude):
    # Make a request to a weather API using latitude and longitude
    # Replace <API_KEY> with your actual weather API key
    api_key_temp = API_WEATHER
    url = f'https://api.weatherapi.com/v1/current.json?key={api_key_temp}&q={latitude},{longitude}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temperature = data['current']['temp_c']
        return {'temperature': temperature}
    else:
        return None


def get_pollution_data(latitude, longitude):
    # Make a request to the OpenAQ API using latitude and longitude
    api_key_pollution = API_POLLUTION
    url = f'https://api.openaq.org/v2/latest?coordinates={latitude},{longitude}&radius=100000&api_key={api_key_pollution}'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        results = data['results']

        if results:
            # Get the air pollution index from the first available result
            pollution_index = results[0]['measurements'][0]['value']
            return {'pollution_index': pollution_index}
        else:
            return None
    else:
        return None

def get_skincare_recommendation(temperature, pollution_index):
    skincare_recommendation = ""

    # Define the ranges for temperature and pollution index
    temperature_ranges = {
        'low': (0, 10),
        'moderate': (11, 25),
        'high': (26, 40),
        'very high': (41, float('inf'))
    }

    pollution_index_ranges = {
        'low': (0, 50),
        'moderate': (51, 100),
        'high': (101, 150),
        'very high': (151, float('inf'))
    }

    # Determine the temperature category
    temperature_category = get_range_category(temperature, temperature_ranges)

    # Determine the pollution index category
    pollution_category = get_range_category(pollution_index, pollution_index_ranges)

    # Make skincare recommendations based on temperature and pollution index
    if temperature_category == 'low':
        skincare_recommendation += "We recommend to use a moisturizer to prevent dryness.\n"
    elif temperature_category == 'moderate':
        skincare_recommendation += "We recommend to apply sunscreen to protect your skin from moderate sun exposure.\n"
    elif temperature_category == 'high':
        skincare_recommendation += "We recommend to use oil-free and lightweight skincare products to prevent excessive oiliness.\n"
    elif temperature_category == 'very high':
        skincare_recommendation += "We recommend to stay indoors and avoid direct sun exposure. Apply sunscreen if necessary.\n"

    if pollution_category == 'low':
        skincare_recommendation += " A basic skincare routine is sufficient to maintain your skin health.\n"
    elif pollution_category == 'moderate':
        skincare_recommendation += " Use antioxidants and gentle cleansers to combat moderate pollution effects when going outside.\n"
    elif pollution_category == 'high':
        skincare_recommendation += " Also apply a physical barrier like a mask or use anti-pollution skincare products due to high pollution in your area.\n"
    elif pollution_category == 'very high':
        skincare_recommendation += " Minimize outdoor activities and use protective skincare products due to very high pollution.\n"

    return skincare_recommendation


#Condition Text
def get_overall_condition(skin_type):
    return overall_conditions.get(skin_type, "Not Face")

def get_cleansing_product(skin_type):
    return cleansing_products.get(skin_type, "Not Face")

def get_toner_product(skin_type):
    return toner_products.get(skin_type, "Not Face")

def get_serum_product(skin_type):
    return serum_products.get(skin_type, "Not Face")

def get_moisturizer_product(skin_type):
    return moisturizer_products.get(skin_type, "Not Face")

def get_sunscreen_product(skin_type):
    return sunscreen_products.get(skin_type, "Not Face")


if __name__ == '__main__':
    app.run(debug=True)

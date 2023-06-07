# Facential Backend API

This API allows you to classify skin types based on facial images and retrieve skincare recommendations for each skin type. It also provides endpoints to retrieve classification results, delete classification results, and get skincare recommendations for different skin types.

## Base URL
http://34.101.153.119:8080/

# Endpoints
## GET /
This endpoint is used to check the API's availability.

### Request
```
GET /
```
### Response
• Success (200 OK)
```
{
  "message": "Success!"
}
```
• Error (404 Not Found)
```
{
  "message": "Error: Resource not found."
}
```
## POST /classify
This endpoint is used to classify the skin type based on a facial image and provide skincare recommendations.

### Request
```
POST /classify
Content-Type: multipart/form-data
Authorization: <user_token>

image: <image_file>
```
image: A facial image file (JPEG or PNG format).

### Response
• Success (200 OK)
```
{
  "skin_type": "<predicted_skin_type>"
}
```
• Error (400 Bad Request)
```
{
  "message": "Image does not contain a valid face."
}
```
## GET /classification_results/{user_uid}
This endpoint is used to retrieve the latest classification result for a specific user UID.

### Request
```
GET /classification_results/{user_uid}
```
user_uid: The unique identifier of the user.

### Response
• Success (200 OK)
```
{
  "id": "<classification_id>",
  "user_uid": "<user_uid>",
  "skin_type": "<predicted_skin_type>",
  "image_url": "<image_url>",
  "overall": "<overall_condition_text>",
  "cleansing": "<cleansing_product>",
  "toner": "<toner_product>",
  "serum": "<serum_product>",
  "moisturizer": "<moisturizer_product>",
  "sunscreen": "<sunscreen_product>"
}
```
• Error (404 Not Found)
```
{
  "message": "No classification results found for the specified user UID."
}
```
## DELETE /deleteall/{user_uid}
This endpoint is used to delete all classification results and associated images for a specific user UID.

###Request
```
DELETE /deleteall/{user_uid}
```
user_uid: The unique identifier of the user.

###Response
• Success (200 OK)
```
{
  "message": "Classification results deleted successfully."
}
```
• Error (404 Not Found)
```
{
  "message": "Classification results not found."
}
```

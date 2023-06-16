# skin_conditions.py

overall_conditions = {
    'Normal': "Your facial skin is in normal condition. It is not too dry nor oily. Use the recommended products below to maintain it.",
    'Dry': "Your facial skin tends to be dry. It requires treatment that can provide extra moisture. See the recommended products and their suitable ingredients for addressing dry skin.",
    'Oily': "Your facial skin tends to be oily. It requires treatment to control excessive oil production. See the recommended products and their suitable ingredients for addressing oily skin.",
    'Combination': "Your facial skin is in a combination condition, with oily and dry areas. See and use the recommended products that have suitable ingredients for addressing this condition.",
    'Sensitive': "Your facial skin tends to be sensitive. Pay attention to choosing gentle and non-irritating products. See and use the following products that have suitable ingredients for sensitive skin."
}

# skin_products.py

# cleansing_products = {
#     'Normal': "Use a cleanser that contains nourishing ingredients such as aloe vera, chamomile, vitamin E, green tea extract, or cucumber extract. These ingredients are known for their soothing properties and their ability to maintain the balance and moisture of normal skin. A cleanser with these ingredients will help keep your skin feeling refreshed and rejuvenated. Remember to cleanse your skin twice a day for optimal results.",

#     'Dry': "Use a cleanser that contains sodium hyaluronate, as this ingredient provides intense hydration to dry skin, helping to replenish moisture and improve skin's elasticity. Additionally, seek out cleansers with ingredients like ceramides and natural oils such as almond oil, argan oil, or jojoba oil. These ingredients help maintain the skin's moisture barrier, preventing dryness and providing nourishment. With regular use, a cleanser formulated with these beneficial ingredients will leave your skin feeling hydrated, soft, and protected. Remember to gently cleanse your skin twice a day for optimal results, followed by a moisturizer to lock in the hydration",

#     'Oily': "Use a cleanser that includes hyaluronic acid to provide extra moisture and hydration. Ceramides are also important ingredients to maintain and replenish the skin's protective barrier. Niacinamide offers soothing benefits, helping to calm any inflammation or redness. If you're prone to acne, consider a cleanser that contains benzoyl peroxide to help reduce breakouts. By keeping these factors in mind, you can find a cleanser that effectively addresses the specific needs of your oily skin.",

#     'Combination': "For combination skin, where the T-zone (forehead and nose) tends to be oily while the cheeks are dry, it's important to choose the right facial cleanser. Opt for a transparent cleanser with a gentle, gel-like consistency. Look for a facial cleanser that contains mild chemical exfoliants like AHAs (Alpha Hydroxy Acids) or BHAs (Beta Hydroxy Acids), as they are suitable for your skin type. Additionally, it is recommended to choose a cleanser that contains ceramides and peptides to help maintain the skin's protective barrier. These ingredients will help balance and nourish your combination skin, ensuring a healthy complexion.",

#     'Sensitive': "It is important to use ingredients that moisturize and repair the skin barrier, such as glycerin, hyaluronic acid, ceramides, and allantoin. It is recommended to avoid high concentrations of exfoliating agents like 10% glycolic acid, strong fragrances, and physical exfoliants like cleansers with beads. These ingredients and practices can potentially irritate sensitive skin. Instead, opt for gentle and fragrance-free cleansers that prioritize moisturization and avoid harsh physical exfoliation. This will help maintain the health and comfort of your sensitive skin."
# }

# toner_products = {
#     'Normal': "It is recommended to use a toner that provides specific nourishment and balance, formulated with moisturizing ingredients. Nourishing toners are designed to help your skin retain moisture thanks to ingredients like hyaluronic acid and niacinamide. These ingredients help hydrate and maintain the moisture balance of your skin, leaving it healthy and nourished. Incorporating such a toner into your skincare routine can contribute to maintaining the natural vitality and radiance of your normal skin.",

#     'Dry': "It is recommended to use a toner that contains soothing and moisturizing ingredients such as hyaluronic acid, glycerin, vitamin E, chamomile, and antioxidants like green tea. These ingredients help provide the desired hydration for your skin. Additionally, ingredients like aloe vera, fruit extracts, and essential oils have calming properties and can further enhance the moisturizing effect on your skin. By incorporating a toner with these beneficial ingredients into your skincare routine, you can help alleviate dryness and keep your skin hydrated and nourished.",

#     'Oily': "It is recommended to use a facial toner specifically formulated for oily skin to remove excess oil, impurities, and residue after cleansing. Active ingredients such as glycolic acid and clay are beneficial in removing excess oil and unclogging pores. However, it is important to avoid using toners that contain alcohol, as they can excessively dry out the skin and cause irritation. By choosing a toner designed for oily skin and avoiding alcohol-based toners, you can effectively balance your skin's oil production and maintain a healthy complexion.",

#     'Combination': "It is recommended to use toners that are specifically formulated to cleanse the skin without causing dryness. Ingredients such as salicylic acid, lactic acid, and witch hazel are particularly beneficial for combination skin. These ingredients help regulate oil production and promote a balanced complexion. It is important to avoid toners that contain simple alcohols and synthetic fragrances, as they can potentially irritate the skin. By choosing a toner tailored for combination skin and free from harsh ingredients, you can effectively address the specific needs of your skin and maintain a harmonious balance between the oily and dry areas.",

#     'Sensitive': "It is recommended to use alcohol-free toners. Avoid using toners that contain simple alcohols such as ethanol, methanol, denatured alcohol, and isopropyl alcohol, as they can be too harsh for this skin type. Additionally, it is important to steer clear of common irritants like dyes and synthetic fragrances, as these ingredients have the potential to exacerbate sensitivity. Opting for alcohol-free toners that are free from harsh ingredients will help soothe and protect sensitive skin, promoting a healthier and more comfortable complexion."
# }

# serum_products = {
#     'Normal': "Those with normal skin types have the privilege of trying out different face serums without significant concern for irritation. You are encouraged to layer serums as necessary to target various skin concerns or adjust your product choices based on seasonal or hormonal changes that may impact your skin.",

#     'Dry': "Look for those that contain humectant ingredients such as hyaluronic acid, glycerin, betaine, and panthenol. These components have the ability to draw moisture from the air and infuse it into the skin, providing deep hydration. Additionally, watch for serums incorporating nourishing elements like coconut extract, ceramides, plant-derived lipids, essential fatty acids, and antioxidants such as Vitamin E. These ingredients replenish the skin's natural barrier, prevent moisture loss, and promote a healthy, radiant complexion. By incorporating these hydrating face serums into your skincare routine, you can effectively address the needs of your dry skin and achieve a revitalized and moisturized appearance.",

#     'Oily': "You can reduce excessive shine on your skin with a serum that effectively controls oil production. Look for ingredients such as niacinamide and enantia chlorantha extract, known for their excellent oil-controlling properties, sebum reduction, and pore size minimization. Additionally, consider serums that contain zinc, lactic acid, and pink clay as they are ideal for absorbing excess oil. By incorporating these oil-controlling serums into your skincare routine, you can achieve a more balanced and shine-free complexion.",

#     'Combination': "For the dry areas of your face, opt for a hydrating serum that replenishes moisture and restores balance. Meanwhile, tackle the oilier patches with serums containing mattifying agents like niacinamide to control excess sebum. By incorporating these serums into your skincare routine, you can effectively address the unique needs of your combination skin, achieving a more harmonized and healthy complexion.",

#     'Sensitive': "Calendula is a powerful ingredient that offers healing properties and helps prevent scarring. Its gentle nature makes it suitable even for delicate baby skin. When incorporated into a face serum, calendula can effectively soothe and nourish irritated skin. Additionally, including milk proteins and botanical extracts like green tea further enhance the calming effect on the skin. Lecithin plays a remarkable role in strengthening the skin's protective barrier, acting as a barrier against potential irritants. To ensure optimal results, it is advisable to avoid synthetic fragrances and dyes that may cause irritation. Embrace the benefits of calendula-infused serums and enjoy a more tranquil and healthier complexion."
# }

# moisturizer_products = {
#     'Normal': "A moisturizer for normal skin should contain hydrating ingredients like glycerin and hyaluronic acid, protective emollients such as jojoba oil and shea butter, antioxidants like vitamin C and E, skin-barrier-supporting ceramides, niacinamide for balancing and improving skin tone, and a lightweight texture for easy absorption. Use this moisturizer regularly to maintain the hydration of your normal skin, keeping it healthy and radiant.",

#     'Dry': "A cream moisturizer is highly recommended for dry skin as its thick consistency provides a nourishing and long-lasting hydration. The rich texture of a cream moisturizer helps to create a protective barrier on the skin, preventing moisture loss and improving overall hydration. Look for moisturizers that contain a combination of hydrating ingredients, such as humectants to attract and retain moisture, as well as oil-based ingredients to lock in hydration. These cream moisturizers will effectively replenish and restore moisture to dry skin, leaving it soft, supple, and hydrated throughout the day.",

#     'Oily': "It is recommended to use a water-based and oil-free gel moisturizer. These moisturizers are light in texture and do not contain any oils, making them ideal for controlling excess oil and reducing shine. Gel moisturizers primarily contain humectant ingredients that attract and retain moisture in the skin, while also offering rejuvenating properties for added benefits. They are non-greasy and particularly suitable for individuals prone to acne. By incorporating a gel moisturizer into your skincare routine, you can effectively hydrate and balance your oily skin, keeping it free from excessive oiliness and maintaining a healthy complexion.",

#     'Combination': " This skin type can benefit from a wide range of moisturizers. If you have normal skin with dry tendencies, opting for a thicker, cream-based moisturizer is recommended. This will provide the necessary hydration and nourishment to combat dryness. On the other hand, if you have normal skin with oily tendencies, a lighter option such as a gel or gel cream/water cream would be more suitable. These formulas offer moisturization without adding excessive oil to the skin, helping to maintain a balanced complexion. Remember to choose products specifically designed for your skin type to ensure optimal results.",

#     'Sensitive': "Using a moisturizer specifically formulated for sensitive skin, as it can provide gentle hydration and nourishment without causing irritation. Look for products that are fragrance-free, hypoallergenic, and non-comedogenic to minimize the risk of adverse reactions. Ingredients such as ceramides, hyaluronic acid, and aloe vera are known to be soothing and moisturizing for sensitive skin. Additionally, opt for moisturizers with a lightweight, non-greasy texture that can be easily absorbed into the skin. Remember to patch test any new product before applying it to your entire face, and consult with a dermatologist if you have any specific concerns about your skin's sensitivity."
# }

# sunscreen_products = {
#     'Normal': "A sunscreen suitable for normal skin type should provide broad-spectrum protection against UVA and UVB rays, with an SPF of 30 or higher. It is recommended to choose a non-comedogenic sunscreen to prevent pore clogging and breakouts. Opt for a lightweight formula that easily absorbs into the skin for a comfortable and non-greasy feel. Apply this sunscreen daily to safeguard your normal skin from harmful sun damage and maintain its health and youthful appearance.",

#     'Dry': "It is important to prioritize hydration and sun protection. Look for sunscreens that contain hydrating ingredients such as vitamin C, hyaluronic acid, and Centella Asiatica. These ingredients not only provide protection against harmful UV rays but also help to nourish and moisturize dry skin. Opt for a sunscreen with a suitable SPF to effectively shield the skin from UV damage.",

#     'Oily': "It is recommended to use a mattifying, oil-free sunscreen. This type of sunscreen helps control shine and is specifically formulated to suit oily skin's needs. It is also advisable to choose a sunscreen that can double as a moisturizer to simplify your skincare routine and prevent excessive product buildup. By opting for a multi-functional sunscreen, you can effectively protect your skin from the sun's harmful rays while keeping excess oil at bay.",

#     'Combination': "It is recommended to use sunscreen with minimal ingredients to avoid clogging pores while providing the necessary moisture for a balanced complexion. Recommended sunscreens for combination skin include those with SPF that soothe the skin with active circa, a lightweight and sheer texture, and quick absorption with a cooling effect.",

#     'Sensitive': "It is recommended to use a physical sunscreen that contains zinc oxide and/or titanium dioxide. These minerals are ideal for sensitive skin because they typically have fewer ingredients and are less likely to cause adverse reactions. Look for a sunscreen with soothing ingredients like circa, as it can help reduce redness and calm the skin's sensitivity. Incorporate this sunscreen into your skincare routine to effectively protect your sensitive skin."
# }

# skin_products.py

cleansing_products = {
    'Normal': "Use a facial cleanser with a balanced and gentle pH to clean the skin without disturbing its natural balance.",
    'Dry': "Use a gentle facial cleanser that contains moisturizing ingredients to hydrate the skin while cleansing.",
    'Oily': "Use a facial cleanser that can control excessive oil production and effectively clean the pores.",
    'Combination': "Use a facial cleanser that can address both conditions of the skin by removing excess oil and moisturizing the dry areas.",
    'Sensitive': "Choose a gentle facial cleanser that is free from irritants such as fragrances and alcohol."
}

toner_products = {
    'Normal': "Use a toner that provides hydration and maintains the skin's pH balance.",
    'Dry': "Use a toner that contains moisturizing ingredients to hydrate dry skin.",
    'Oily': "Use a toner that can control excess oil and clean the pores.",
    'Combination': "Use a toner that can balance oil production in oily areas and provide hydration to dry areas.",
    'Sensitive': "Choose a gentle toner that is free from irritants such as fragrances and alcohol."
}

serum_products = {
    'Normal': "Use a serum with antioxidant content to protect the skin from damage caused by free radicals.",
    'Dry': "Use a serum with intensive moisturizing ingredients to hydrate and nourish dry skin.",
    'Oily': "Use a serum with ingredients that can control excessive oil production and reduce shine on oily skin.",
    'Combination': "Use a serum with ingredients that can balance oil production in oily areas and provide hydration to dry areas.",
    'Sensitive': "Choose a serum with gentle ingredients that are free from irritants such as fragrances and alcohol."
}

moisturizer_products = {
    'Normal': "Use a lightweight moisturizer with ingredients that maintain the skin's natural moisture.",
    'Dry': "Use a rich moisturizer with ingredients that hydrate and nourish dry skin.",
    'Oily': "Use a lightweight and oil-free moisturizer to maintain moisture without leaving a heavy feeling on oily skin.",
    'Combination': "Use a moisturizer with ingredients that can balance oil production in oily areas and provide hydration to dry areas.",
    'Sensitive': "Choose a moisturizer with gentle ingredients that are free from irritants such as fragrances and alcohol."
}

sunscreen_products = {
    'Normal': "Use a sunscreen with a minimum SPF of 30 that contains antioxidants such as vitamin C and vitamin E.",
    'Dry': "Use a sunscreen with a minimum SPF of 30 that has an oil-free or non-comedogenic formula to prevent pore blockage. Also, choose one that contains zinc oxide or titanium dioxide to absorb excess oil.",
    'Oily': "Use a sunscreen with a minimum SPF of 30 that contains mattifying agents to reduce excessive shine on oily skin.",
    'Combination': "Use a sunscreen with a minimum SPF of 30 that contains niacinamide to balance oil production. Also, choose one that contains hyaluronic acid and green tea extract to moisturize and control oil.",
    'Sensitive': "Choose a sunscreen that is suitable for sensitive skin, avoiding chemical ingredients and fragrances that can cause allergic reactions. Use one that contains zinc oxide or titanium dioxide."
}


# Importing the random module to generate random data
import random

# Importing the json module to convert Python data to JSON format
import json

# A list of some prominent exams held in India
exams_in_india = [
    "JEE", "NEET", "UPSC", "CAT", "GATE", "CLAT", 
    "GMAT", "GRE", "IELTS", "TOEFL", "UGC-NET", "SSC CGL", 
    "IBPS PO", "SBI PO", "RRB", "CTET", "AFCAT", "NDA"
]

def generate_random_data():
    # Randomly select the type of centerImage (either "asset" or "url")
    centerImage_type = random.choice(["asset", "url"])
    
    # Based on the chosen type, assign a URL or asset path to centerImage_url
    if centerImage_type == "url":
        centerImage_url = "https://via.placeholder.com/157x149"
    else:
        centerImage_url = "assets/images/center_image.png"
    
    # List of sample center locations and names
    centerLocations = ["Kalkaji , New Delhi", "Rohini, Delhi", "Saket, Delhi", "Dwarka, Delhi", "Connaught Place, Delhi"]
    centerNames = ["Metro Coaching Center", "Elite Coaching", "Future Academy", "Success Point", "Knowledge Hub"]
    
    # Generate random tags for the center, based on the available exams
    random_tags = []
    available_exams = exams_in_india.copy()
    for _ in range(random.randint(1, 4)):
        tag_choice = random.choice(available_exams)
        available_exams.remove(tag_choice)
        is_highlighted = False
        random_tags.append({"tagText": tag_choice, "isHighlighted": is_highlighted})
    
    # Randomly decide if a discount tag should be added
    if random.choice([True, False]):
        discount_value = random.randint(10, 100)
        random_tags.append({"tagText": f"{discount_value}% Off", "isHighlighted": True})
    
    # Randomly decide if a bottomText should be added, indicating the number of students studying there
    if random.choice([True, False]):
        bottomTexts = [f"{random.randint(1, 5)} of your school students study here"]
    else:
        bottomTexts = []
    
    # Return a dictionary with the generated random data for a coaching center
    return {
        "centerImage": {"type": centerImage_type, "url": centerImage_url},
        "centerLocation": random.choice(centerLocations),
        "centerName": random.choice(centerNames),
        "centerRating": round(random.uniform(3, 5), 1),
        "centerDistance": random.randint(500, 5000),
        "centerTags": random_tags,
        "bottomTexts": bottomTexts
    }

# Generate a list of 100 dictionaries, each containing random data for a coaching center
json_data = [generate_random_data() for _ in range(100)]

# Convert the list of dictionaries to a formatted JSON string
json_data = json.dumps(json_data, indent=2)

# Print the formatted JSON string
print(json_data)

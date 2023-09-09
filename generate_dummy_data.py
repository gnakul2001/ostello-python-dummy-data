# Import the random module for generating random values.
import random

# Import the json module for converting Python data structures to JSON format.
import json

# A list of prominent exams held in India. This will be used for generating sample data.
exams_in_india = [
    "JEE", "NEET", "UPSC", "CAT", "GATE", "CLAT", 
    "GMAT", "GRE", "IELTS", "TOEFL", "UGC-NET", "SSC CGL", 
    "IBPS PO", "SBI PO", "RRB", "CTET", "AFCAT", "NDA"
]

def generate_random_data(wantListOnly=False):
    """
    Generate random data for a coaching center or an 'ask_ostello' type.
    The function can be directed to generate 'list' type only using the wantListOnly parameter.
    """
    # Default type of entry is set to "list".
    type = "list"

    # Determine the type based on randomness unless constrained by 'wantListOnly'.
    if wantListOnly == False and random.choice([True, False]):
        type = "ask_ostello"

    if type == "list":
        # Randomly determine the type of image for the center (either from an asset or a URL).
        centerImage_type = random.choice(["asset", "url"])

        # Assign a value to centerImage based on the chosen type.
        if centerImage_type == "url":
            centerImage_url = "https://via.placeholder.com/157x149"
        else:
            centerImage_url = "assets/images/center_image.png"

        # Sample center locations and names for random data generation.
        centerLocations = ["Kalkaji , New Delhi", "Rohini, Delhi", "Saket, Delhi", "Dwarka, Delhi", "Connaught Place, Delhi"]
        centerNames = ["Metro Coaching Center", "Elite Coaching", "Future Academy", "Success Point", "Knowledge Hub"]

        # Generate random tags for the center based on available exams.
        random_tags = []
        available_exams = exams_in_india.copy()
        for _ in range(random.randint(1, 4)):
            tag_choice = random.choice(available_exams)
            available_exams.remove(tag_choice)
            is_highlighted = False
            random_tags.append({"tagText": tag_choice})

        # Optionally add a bottom text indicating the number of students.
        if random.choice([True, False]):
            bottomTexts = [f"{random.randint(1, 5)} of your school students study here"]
        else:
            bottomTexts = []

        # Return the generated data for the 'list' type.
        return {
            "type": type,
            "data": {
                "center_image": {"type": centerImage_type, "url": centerImage_url},
                "center_location": random.choice(centerLocations),
                "center_name": random.choice(centerNames),
                "center_rating": round(random.uniform(3, 5), 1),
                "center_distance": random.randint(500, 5000),
                "center_tags": random_tags,
                "center_discount": random.randint(10, 100) if random.choice([True, False]) else 0,
                "bottom_texts": bottomTexts
            }
        }
    else:
        # If the type is not 'list', simply return the 'ask_ostello' type.
        return {"type": type}

def process_data(data_list):
    """
    Process the provided data list to ensure that there are no consecutive 'ask_ostello' entries.
    If consecutive 'ask_ostello' entries are found, only the first one is retained, and the rest are replaced with 'list' type entries.
    """
    processed_data = []
    i = 0
    while i < len(data_list):
        # Check for 'ask_ostello' type entries.
        if data_list[i]["type"] == "ask_ostello":
            processed_data.append(data_list[i])
            count_ostello = 1
            while i + 1 < len(data_list) and data_list[i + 1]["type"] == "ask_ostello":
                count_ostello += 1
                i += 1

            # Replace extra 'ask_ostello' entries with 'list' type entries.
            for _ in range(1, count_ostello):
                processed_data.append(generate_random_data(True))
            i += 1
        else:
            # Append non 'ask_ostello' type entries as they are.
            processed_data.append(data_list[i])
            i += 1
    return processed_data

# Generate a list of 100 random data entries.
json_data = [generate_random_data() for _ in range(100)]

# Process the generated data to ensure no consecutive 'ask_ostello' entries exist.
json_data = process_data(json_data)

# Convert the processed list to a formatted JSON string.
json_string = json.dumps(json_data, indent=2)

# Print the resulting JSON string.
print(json_string)

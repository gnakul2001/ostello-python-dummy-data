# Import necessary modules.
import random
import json
import os

# Define a list of major exams held in India for random tag generation.
exams_in_india = [
    "JEE",
    "NEET",
    "UPSC",
    "CAT",
    "GATE",
    "CLAT",
    "GMAT",
    "GRE",
    "IELTS",
    "TOEFL",
    "UGC-NET",
    "SSC CGL",
    "IBPS PO",
    "SBI PO",
    "RRB",
    "CTET",
    "AFCAT",
    "NDA",
]

# Get the parent directory, which should be the project root
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Generate the full path for a given file name by appending it to the current directory.
def generate_file_name(file_name):
    # Construct the file path by appending the filename to the script's directory
    return f"{project_root}/{file_name}.json"


def generate_random_data():
    """Generate random data for a coaching center of type 'list'."""

    # Determine random image type for the center: either 'asset' or 'URL'.
    centerImage_type = random.choice(["asset", "url"])

    # Based on image type, set image source.
    centerImage_url = (
        "https://via.placeholder.com/157x149"
        if centerImage_type == "url"
        else "assets/images/center_image.png"
    )

    # Sample locations and names for the coaching center.
    centerLocations = [
        "Kalkaji , New Delhi",
        "Rohini, Delhi",
        "Saket, Delhi",
        "Dwarka, Delhi",
        "Connaught Place, Delhi",
    ]
    centerNames = [
        "Metro Coaching Center",
        "Elite Coaching",
        "Future Academy",
        "Success Point",
        "Knowledge Hub",
    ]

    # Generate a set of random tags for the center from the exams list.
    random_tags = []
    available_exams = exams_in_india.copy()
    for _ in range(random.randint(1, 4)):
        tag_choice = random.choice(available_exams)
        available_exams.remove(tag_choice)
        random_tags.append({"tag_text": tag_choice})

    # Decide randomly if bottom text (indicating student count) should be added.
    bottomTexts = (
        [f"{random.randint(1, 5)} of your school students study here"]
        if random.choice([True, False])
        else []
    )

    # Compile and return the generated random data.
    return {
        "center_image": {"type": centerImage_type, "url": centerImage_url},
        "center_location": random.choice(centerLocations),
        "center_name": random.choice(centerNames),
        "center_rating": round(random.uniform(3, 5), 1),
        "center_distance": random.randint(500, 5000),
        "center_tags": random_tags,
        "center_discount": random.randint(10, 100)
        if random.choice([True, False])
        else 0,
        "bottom_texts": bottomTexts,
    }


def save_file(file_path):
    # Generate a list of random data for 100 coaching centers.
    json_data = [generate_random_data() for _ in range(100)]

    # Convert the data list into a prettified JSON string.
    json_string = json.dumps(json_data, indent=2)

    try:
        # Open the constructed file path in write mode
        with open(file_path, "w") as file:
            # Write the JSON string to the file
            file.write(json_string)

        return True
    # Handle any exception that might occur during the above operations
    except Exception:
        return False


def main():
    print(
        "OK" if save_file(generate_file_name("center-dummy-data")) is True else "ERROR"
    )


if __name__ == "__main__":
    main()

# Import necessary modules for JSON operations, OS operations, and unit testing.
import json
import os
import unittest

# Import necessary functions and data from the app.generate_dummy_data module.
from app.generate_dummy_data import (
    generate_random_data,
    exams_in_india,
    generate_file_name,
    save_file,
)

# Define a class for testing data generation functions.
class TestDataGeneration(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Generate a temporary file name using the generate_file_name function.
        cls.temp_file = generate_file_name("test_center-dummy-data")

    @classmethod
    def tearDownClass(cls):
        # Delete the temporary file after all tests have completed.
        os.unlink(cls.temp_file)

    def test_generate_random_data(self):
        """Test the generate_random_data function."""
        # Generate a random data sample.
        data = generate_random_data()

        # Check that the generated data is a dictionary.
        self.assertIsInstance(data, dict)

        # Define the list of keys expected in the generated data.
        expected_keys = [
            "center_image",
            "center_location",
            "center_name",
            "center_rating",
            "center_distance",
            "center_tags",
            "center_discount",
            "bottom_texts",
        ]

        # Check that each expected key is present in the generated data.
        for key in expected_keys:
            self.assertIn(key, data)

        # Validate the values of some of the keys in the generated data.
        self.assertIn(data["center_image"]["type"], ["asset", "url"])
        self.assertIn(
            data["center_image"]["url"],
            ["https://via.placeholder.com/157x149", "assets/images/center_image.png"],
        )

        # Define valid location and name values.
        valid_locations = [
            "Kalkaji , New Delhi",
            "Rohini, Delhi",
            "Saket, Delhi",
            "Dwarka, Delhi",
            "Connaught Place, Delhi",
        ]
        valid_names = [
            "Metro Coaching Center",
            "Elite Coaching",
            "Future Academy",
            "Success Point",
            "Knowledge Hub",
        ]

        # Check that the generated location and name values are valid.
        self.assertIn(data["center_location"], valid_locations)
        self.assertIn(data["center_name"], valid_names)

        # Validate the rating and distance values.
        self.assertTrue(3 <= data["center_rating"] <= 5)
        self.assertTrue(500 <= data["center_distance"] <= 5000)

        # Validate that generated tags are in the exams_in_india list.
        for tag in data["center_tags"]:
            self.assertIn(tag["tag_text"], exams_in_india)

        # Validate the discount value.
        self.assertTrue(0 <= data["center_discount"] <= 100)

        # If bottom_texts are present, validate the student count value.
        if data["bottom_texts"]:
            self.assertTrue(1 <= int(data["bottom_texts"][0].split()[0]) <= 5)

    def test_file_writing(self):
        """Test the file writing process."""
        # Check that the save_file function returns True, indicating a successful save.
        self.assertTrue(save_file(self.temp_file))

        # Open the temporary file and check its contents.
        with open(self.temp_file, "r") as file:
            try:
                # Load the content of the file as JSON.
                content = json.loads(file.read())
                # Check that the content is a list of 100 items.
                self.assertIsInstance(content, list)
                self.assertEqual(len(content), 100)
            except json.JSONDecodeError:
                # If there's an error decoding the JSON, the test fails.
                self.fail("The file does not contain valid JSON data.")

        # Validate the structure of a sample data entry in the content.
        sample_data = content[0] if content else {}
        expected_keys = [
            "center_image",
            "center_location",
            "center_name",
            "center_rating",
            "center_distance",
            "center_tags",
            "center_discount",
            "bottom_texts",
        ]
        for key in expected_keys:
            self.assertIn(key, sample_data)

# Execute the tests with a verbosity level of 2 (detailed).
unittest.main(argv=[""], verbosity=2, exit=False)

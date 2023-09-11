# Import the 'os' module to interact with the operating system.
import os
# Import the 'sys' module to interact with the Python runtime environment.
import sys

# Get the absolute path of the current script (main.py) and determine its directory.
# This will give us the root directory of our project.
root_directory = os.path.dirname(os.path.abspath(__file__))

# Add the root directory to the system path.
# This allows us to import modules and packages from our project directory.
sys.path.append(root_directory)

# Import the 'main' function from the 'generate_dummy_data' module inside the 'app' package.
# Rename it to 'generate_data_main' to avoid naming conflicts and to make its purpose clear.
from app.generate_dummy_data import main as generate_data_main

# Define the 'run' function. This will serve as the main entry point when this script is run.
def run():
    # Invoke the 'generate_data_main' function to run the main logic of the 'generate_dummy_data' module.
    generate_data_main()

# Check if this script is being run as the main module.
# If so, invoke the 'run' function.
if __name__ == "__main__":
    run()

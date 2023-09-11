# ostello-python-dummy-data

[![Build](https://github.com/gnakul2001/ostello-python-dummy-data/actions/workflows/build.yml/badge.svg)](https://github.com/gnakul2001/ostello-python-dummy-data/actions/workflows/build.yml)

This repository contains the script used to generate dummy data for the Ostello Institute Search Page Flutter app. The data generated closely represents coaching centers, with attributes such as location, name, image, and more.

## 📌 Overview

Developed by Nakul Gupta, this backend solution leverages Python to create a realistic set of coaching center data. The generated data can be utilized in various applications for demonstration and testing purposes.

## 🔍 Features

- **Random Data**: Generates diverse data to simulate different coaching centers.
- **JSON Output**: Produces a well-structured JSON output for easy consumption.
- **Customizable**: The number of generated entries and other parameters can be easily adjusted in the script.

## ⚙️ Prerequisites

- Python 3.x

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/gnakul2001/ostello-python-dummy-data.git
   ```

2. Navigate to the cloned directory:
   ```bash
   cd ostello-python-dummy-data
   ```

3. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🖥️ Usage

Run the script to generate the dummy data:
```bash
python main.py
```

After execution, a JSON file named `center-dummy-data.json` will be created in the project root, containing the generated dummy data.

## 📚 Data Attributes

Each generated entry has the following attributes:
- `center_image`: Type and URL/asset path of the center's image.
- `center_location`: Location of the coaching center.
- `center_name`: Name of the coaching center.
- `center_rating`: Rating of the coaching center (between 3 to 5).
- `center_distance`: Distance of the coaching center in meters.
- `center_tags`: Exams the center coaches for.
- `center_discount`: Possible discount percentage.
- `bottom_texts`: Additional texts, such as student counts.

## ✅ Running Tests

To run the unit tests, execute:
```bash
pytest
```

## 🤝 Contribution & Support

For any queries, feedback, or contributions, feel free to reach out:

- **Leetcode**: [gnakul2001](http://leetcode.com/gnakul2001)
- **LinkedIn**: [Nakul Gupta](http://linkedin.com/in/thenakulgupta)
- **Github**: [gnakul2001](http://github.com/gnakul2001)
- **Phone**: +91-8802631740
- **Email**: nakulgupta1042@gmail.com

# CV Data Management System

A Python-based system for managing and generating professional CVs using Pydantic models. This project provides a structured way to create, validate, and manage CV data with a focus on data integrity and type safety.

## Features

- **Structured CV Data Model**: Uses Pydantic v2 for robust data validation and type checking
- **JSON Serialization**: Easy import/export of CV data in JSON format
- **Dynamic CV Generation**: Generate sample CVs with realistic data
- **Flexible Schema**: Supports various professional profiles (Developers, Data Scientists, etc.)
- **Date Handling**: Proper handling of dates and time periods
- **Type Safety**: Full type hints and validation

## Project Structure

```
.
├── cv_models.py      # Pydantic models for CV data structure
├── create_cv.py      # Script to load and display CVs
├── generate_sample_cv.py  # Script to generate sample CVs
├── requirements.txt  # Project dependencies
└── README.md        # This file
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd cv-data-management
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Generating a Sample CV

```bash
python generate_sample_cv.py
```
This will create a sample CV and save it as `data_scientist_cv.json`.

### Loading and Displaying a CV

```bash
python create_cv.py
```
This will load the CV from JSON and display a formatted summary.

### Creating Your Own CV

1. Create a JSON file following the schema defined in `cv_models.py`
2. Use the provided scripts to load and validate your CV

## Data Model

The CV data model includes:

- Personal Information
- Professional Summary
- Education History
- Work Experience
- Projects
- Skills
- Certifications
- Languages
- Interests

## Development

### Code Formatting

The project uses Black for code formatting:
```bash
black .
```

### Testing

Run tests using pytest:
```bash
pytest
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Pydantic for the excellent data validation library
- Python community for the rich ecosystem of tools and libraries

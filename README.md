# Django REST Framework Project

## Overview

This project is a Django application that uses Django REST Framework (DRF) to create a robust API. The application includes features for creating and managing items with comprehensive error handling, testing, and API documentation.

## Table of Contents

1. [Features](#features)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Usage](#usage)
6. [Testing](#testing)
7. [API Endpoints](#api-endpoints)
8. [Contributing](#contributing)
9. [Versioning](#versioning)

## Features

- Create, retrieve, update, and delete items.
- Comprehensive error handling with custom responses.
- API documentation using Django REST Framework.
- Testing coverage for various scenarios.

## Requirements

- Python 3.10 or higher
- Django 4.1.x
- Django REST Framework
- Djongo (for MongoDB integration)
- Other dependencies specified in `requirements.txt`

## Installation 
## Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/zee-ham-su/technical_assessment_django.git
   cd technical_assessment_django
   
2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   
3. **Activate the virtual environment:**

   **On Windows:**
   ```bash
   venv\Scripts\activate
   ```
   **On macOS/Linux:**
   ```bash
   source venv/bin/activate
   ```
5. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
6. **Apply migrations:**
   ```bash
   python3 manage.py migrate
   ```

## Configuration
1. **Update your .env or settings file:**
  - Add necessary environment variables or configuration settings for your       
    database and other services.
2. **Steps to Set Up Environment Variables**
   - Create a .env file (if not already present):
   - This file should be located in the root directory of your Django project.
   - Add your MongoDB configuration to this file:
     ```bash
     MONGODB_NAME=your_database_name
     MONGODB_URI=mongodb://localhost:27017/your_database_name
     ```
3. **Update settings.py**
   ```bash
   import os
   Other settings...

   DATABASES = {
      'default': {
          'ENGINE': 'djongo',
          'NAME': os.getenv('MONGODB_NAME', 'default_db_name'),  # Provide a    default name if the env var is not set
          'ENFORCE_SCHEMA': False,
          'CLIENT': {
              'host': os.getenv('MONGODB_URI', 'mongodb://localhost:27017/'),  #  Provide a default URI if the env var is not set
        }
    }
}

4. **Add .env to .gitignore:**
   - Ensure your .env file is not tracked by version control to keep sensitive 
     information secure:
 ```bash
 # .gitignore
 .env
```

## Usage
1. Start the development server:
   ```bash
    python3 manage.py runserver 8080
   ```
2. Access the API:
Open your browser or API client and navigate to http://127.0.0.1:8080/api/.

## Testing
1. **Run tests:**
   ```bash
   python3 manage.py test 
   ```
2. **Test coverage:**
   - Ensure tests cover various scenarios including edge cases and error 
     conditions.

## API Endpoints
  - **Items:**
  - **GET /api/items/** - List all items
  - **POST /api/items/** - Create a new item
  - **GET /api/items/<id>/** - Retrieve an item by ID
  - **PUT /api/items/<id>/** - Update an item by ID
  - **PATCH /api/items/<id>/** - Partially update an item by ID
  - **DELETE /api/items/<id>/** - Delete an item by ID

## Swagger Documentation

Swagger UI provides a user-friendly interface for exploring and interacting with your API's endpoints. It generates interactive API documentation that allows you to test your API directly from the browser.

### Accessing Swagger UI

To access Swagger UI for your API, follow these steps:

1. **Run the Development Server**: Ensure your Django server is running. Use the following command if it isn't already running:
   ```bash
   python3 manage.py runserver
2. **Open Swagger UI: Open your web browser and navigate to:**
   ```bash
   http://127.0.0.1:8080/swagger/
   ```
This URL will display the Swagger UI where you can see all available endpoints, their descriptions, parameters, and responses.
For more details on customizing and using Swagger with Django REST Framework, refer to the  drf-yasg documentation.(https://drf-yasg.readthedocs.io/en/stable/)

## Contributing
1. Fork the repository.
2. Create a new branch for your changes.
3. Commit your changes.
4. Push to your forked repository.
5. Open a pull request.

# Versioning
This project is versioned to ensure backward compatibility and easy maintenance. The current version is [v1].

## License
This project is licensed under the MIT License.

# Tanhuma Project Portal

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
  - [Docker installation](#docker-installation)
  - [Configuration](#configuration)
  - [Deployment](#deployment)
  - [Testing](#testing)
  - [Contributing](#contributing)
  - [License](#license)

## Introduction
The Tanhuma Project Portal is a web application that provides a platform for the Tanhuma Project. The Tanhuma Project is a project that aims to provide a comprehensive and accessible digital edition of the Tanhuma Midrashim.

## Contact
- [Benjamin Schnabel](mailto: benjamin.schnabel@gmx.net)
- e-Lijah Lab, Haifa.
- University of Applied Sciences, Mannheim.

## License
Benjamin Schnabel, 2024.
The Tanhuma Project Portal is open source software licensed under the [MIT License](). The Tanhuma Project Portal is provided "as is" without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.

## Features
- **User Authentication**: Users can create an account and log in to the portal.
- **Synopsis**: Users can view a synopsis of the Tanhuma Midrashim.
- **Ontology**: Users can view the ontology of the Tanhuma Midrashim.
- **Texts**: Users can view the texts of the Tanhuma Midrashim.
- **Commentary**: Users can view the commentary on the Tanhuma Midrashim.
- **Search**: Users can search for specific content within the Tanhuma Midrashim.
- **Contribution**: Users can contribute to the Tanhuma Project by submitting new content or corrections to existing content.
- **Administration**: Administrators can manage the content and users of the portal.
- **API**: The portal provides an API for accessing the content of the Tanhuma Midrashim.
- **Documentation**: The portal provides documentation for the Tanhuma Project.
- **Support**: The portal provides support for users of the Tanhuma Project.

## Installation
To install the Tanhuma Project Portal, follow these steps:
1. Clone the repository:
   ```sh
   git clone https://github.com/tahuma/portal.git
   ```

2. Create a virtual environment:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the dependencies:
   ```sh
    cd portal
    pip install -r requirements.txt
    npm install
    ```
4. Set up the database:
    ```sh
    python manage.py migrate
    ```
5. Create a superuser account:
    ```sh
    python manage.py createsuperuser
    ```
6. Run the development server:
    ```sh
    python manage.py runserver
    ```
7. Access the portal in your web browser: http://localhost:8000

### Docker installation
To install the Tanhuma Project Portal using Docker, follow these steps:
1. Clone the repository:
   ```sh
   git clone
    ```
2. Build the Docker image:
    ```sh
   docker-compose build
   ```
3. Run the Docker container: 
   ```sh
   docker-compose up
   ```
4. Access the portal in your web browser: http://localhost:8000
5. Log in to the portal using the default administrator account:
   - Username: admin
   - Password: admin

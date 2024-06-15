# Django Mini Project

This is a Django mini project designed to manage users, clients, and projects. It includes REST APIs for creating, fetching, updating, and deleting clients and projects, as well as assigning users to projects.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [License](#license)

## Installation

### Prerequisites

- Python 3.x
- MySQL
- Git

### Steps

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/your-repository-name.git
    cd your-repository-name
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv env
    ```

    - **Windows:**

        ```bash
        .\env\Scripts\activate
        ```

    - **macOS/Linux:**

        ```bash
        source env/bin/activate
        ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database:**

    - Make sure MySQL is running.
    - Log in to MySQL and create a database and user:

        ```sql
        CREATE DATABASE mydatabase;
        CREATE USER 'mydatabaseuser'@'localhost' IDENTIFIED BY 'mypassword';
        GRANT ALL PRIVILEGES ON mydatabase.* TO 'mydatabaseuser'@'localhost';
        FLUSH PRIVILEGES;
        ```

5. **Configure the database in Django:**

    Edit `myproject/settings.py`:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'mydatabase',
            'USER': 'mydatabaseuser',
            'PASSWORD': 'mypassword',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
    ```

6. **Apply migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

7. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

8. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

## Usage

### Accessing the Admin Interface

Visit `http://127.0.0.1:8000/admin` and log in with the superuser credentials to manage users, clients, and projects.

### API Endpoints

#### List of All Clients

- **Endpoint:** `GET /api/clients/`
- **Response:**

    ```json
    [
        {
            "id": 1,
            "client_name": "Nimap",
            "created_at": "2019-12-24T11:03:55.931739+05:30",
            "created_by": "Rohit"
        },
        {
            "id": 2,
            "client_name": "Infotech",
            "created_at": "2019-12-24T11:03:55.931739+05:30",
            "created_by": "Rohit"
        }
    ]
    ```

#### Create a New Client

- **Endpoint:** `POST /api/clients/`
- **Input:**

    ```json
    {
        "client_name": "company A"
    }
    ```

- **Response:**

    ```json
    {
        "id": 3,
        "client_name": "company A",
        "created_at": "2019-12-24T11:03:55.931739+05:30",
        "created_by": "Rohit"
    }
    ```

#### Retrieve Client Info

- **Endpoint:** `GET /api/clients/:id`
- **Response:**

    ```json
    {
        "id": 2,
        "client_name": "Infotech",
        "projects": [
            {
                "id": 1,
                "name": "project A"
            }
        ],
        "created_at": "2019-12-24T11:03:55.931739+05:30",
        "created_by": "Rohit",
        "updated_at": "2019-12-24T11:03:55.931739+05:30"
    }
    ```

#### Update Client Info

- **Endpoint:** `PUT/PATCH /api/clients/:id`
- **Input:**

    ```json
    {
        "client_name": "company A"
    }
    ```

- **Response:**

    ```json
    {
        "id": 3,
        "client_name": "company A",
        "created_at": "2019-12-24T11:03:55.931739+05:30",
        "created_by": "Rohit",
        "updated_at": "2019-12-24T11:03:55.931739+05:30"
    }
    ```

#### Delete Client

- **Endpoint:** `DELETE /api/clients/:id`
- **Response Status:** `204 No Content`

#### Create a New Project

- **Endpoint:** `POST /api/projects/`
- **Input:**

    ```json
    {
        "project_name": "Project A",
        "client_id": 1,
        "users": [1]
    }
    ```

- **Response:**

    ```json
    {
        "id": 3,
        "project_name": "Project A",
        "client": "Nimap",
        "users": [
            {
                "id": 1,
                "name": "Rohit"
            }
        ],
        "created_at": "2019-12-24T11:03:55.931739+05:30",
        "created_by": "Ganesh"
    }
    ```

#### List of All Projects Assigned to the Logged-In User

- **Endpoint:** `GET /api/projects/`
- **Response:**

    ```json
    [
        {
            "id": 1,
            "project_name": "Project A",
            "client_name": "Client A",
            "created_at": "2019-12-24T11:03:55.931739+05:30",
            "created_by": "Ganesh"
        },
        {
            "id": 2,
            "project_name": "Project B",
            "client_name": "Client A",
            "created_at": "2019-12-24T11:03:55.931739+05:30",
            "created_by": "Ganesh"
        }
    ]
    ```

#### Delete Project

- **Endpoint:** `DELETE /api/projects/:id`
- **Response Status:** `204 No Content`

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

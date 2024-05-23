# cinelit

## Installation

### Prerequisites

Make sure you have the following tools installed:

- Python (version 3.12), remember to add python to $PATH
- [venv] Should be installed with python
- [Docker Desktop](https://www.docker.com/products/docker-desktop)
- pgadmin4 (Local app) / managing db from http://localhost:8000/admin
- IDE, I recommend to install PyCharm

### Step 1: Clone the Project

To clone the project, run the following command:

```bash
git clone https://github.com/micichocki/cinelit
```

### Step 2: Install Dependencies

First of all you need to create virtual environment

```
python -m venv cinelit
```

To activate virtual environment type:

```
.\Scripts\activate
```

You should now see (cinelit) in terminal.

To install dependencies run this command in project directory:

```bash
pip install -r requirements.txt
```

### Step 3: Running container

```bash\
docker compose up --build
```

This command will start the Docker containers defined in your docker-compose.yml

Please wait for the configuration. It can take several minutes.

### Step 4: Running webserver

```
python manage.py runserver
```

Navigate to:

```
http://localhost:8080/
```

If you see Django template everything should be correct

### Step 5: Run migrations:

To setup db please run

```
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Connect to admin panel:

To create superuser run

```
python manage.py createsuperuser
```

Then fill required credentials

Check if after logging on

```
http://localhost:8000/admin 
```

you can see user models.

Please log into pgadmin and make this query:

```
CREATE SEQUENCE shared_sequence;
```

If any problem occur, please contact me.

## How to work with the repo

### 1.Please make seperate branches if you want to add any functionality

```
git checkout -b <branch_name>

git add .

git commit -m "Message"

git push origin <branch_name>
```

Then make a merge request if you want to merge
changes to main

### 2.Remeber to use

```
pip freeze > requirements.txt
```

if you install any dependency

### 3.After any changes to models apply migrations to db

```
python manage.py makemigrations
python manage.py migrate
```


#  Nuts Service Subscriber Application

This project is part of my Software Engineering course assignment. It implements a small, clean 3-layered application in Python. The goal is to simulate receiving messages from a message bus (Nuts service), process them, and store them in a PostgreSQL database.

Everything runs locally and is kept simple for easy understanding and testing.

---

##  Project Architecture (3-Layered Design)

The system follows a clear 3-layer architecture to keep responsibilities well-separated:

### 1.  API Layer (`api/subscriber.py`)
- Simulates subscription to the Nuts service
- Receives messages (every 2 seconds in simulation)
- Passes messages to the service layer

### 2.  Service Layer (`service/processor.py`)
- Validates the message
- Checks for duplicates
- Saves it using the data layer
- Logs the message to a `.txt` file
- Prints how many messages have been saved in total

### 3.  Data Layer (`data/db.py`)
- Connects to PostgreSQL
- Saves messages to the `messages` table
- Checks for duplicates
- Counts total saved messages

---

##  PostgreSQL Schema Setup

The following table is used to store messages:
`setup_db.sql`


How to Run the Project

You can run the full application either manually or using Docker Compose.


Manual Setup
1. Install PostgreSQL

sudo apt update
sudo apt install postgresql postgresql-contrib

2. Create Database and User

sudo -u postgres psql

Then in the psql shell:

CREATE DATABASE nutsdb;
CREATE USER nutsuser WITH PASSWORD 'nutspassword';
GRANT ALL PRIVILEGES ON DATABASE nutsdb TO nutsuser;
\q

3. Apply Schema

psql -U nutsuser -d nutsdb -h localhost -f setup_db.sql

4. Install Python dependencies

pip install -r requirements.txt

5. Run the application

python3 main.py

You’ll see messages being received, processed, and saved every 2 seconds.
 Running Tests

Tests are located in the tests/ folder. To run them:

python3 -m unittest discover tests










🐳 Docker Compose (Optional but Recommended)

You can run everything using Docker Compose. This sets up PostgreSQL and runs your app with one command.

Run:

docker-compose up --build



Technologies Used

    Python 3.10

    PostgreSQL

    Docker (optional)

    unittest (Python testing)

    asyncio (for simulating message stream)

Author

    Name: Anna Manucharyan

    Course: Software Engineering

    University: American University of Armenia


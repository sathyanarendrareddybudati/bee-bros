# bee-bros
bee-bros is a sample FastAPI application that provides microservices for bee-bros project

# Technologies Used
 - FastAPI
 - Mysql
 - Uvicorn (An ASGI web server, for Python)


## Getting started
To get started with Logging, follow these steps:

- Clone the repository to your local machine
- Install the required packages listed in requirements.txt
- Set up your MYSQL database and create a table for storing logs (see below for an example schema)
- Start the FASTAPI application using `make run` or  `uvicorn main:app --reload`


## Note
- All requests must have x-api-key in headers
- To install all packages using `make install` or `pip install -r requirements.txt`
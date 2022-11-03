# Importing Necessary modules
from fastapi import FastAPI
import uvicorn
import logging

from payload import request_body
from model import gaussianNb

######## Log Start #######
# console logger
# logFormatter = logging.Formatter("%(asctime)s [%(threadName)s] [%(levelname)-4s]  %(message)s")
logFormatter = logging.Formatter("%(asctime)s [%(levelname)-4s]  %(message)s")
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
# Attach LoggingHandler to root logger
logging.getLogger().addHandler(consoleHandler)
logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger(__name__)
######## Log End #######


# Declaring our FastAPI instance
app = FastAPI()
 
# Defining path operation for root endpoint
@app.get('/')
def main():
    logger.info("Welcome to GeeksforGeeks!")
    return {'message': 'Welcome to GeeksforGeeks!'}
 
# Defining path operation for /name endpoint
@app.get('/{name}')
def hello_name(name : str):
    # Defining a function that takes only string as input and output the
    # following message.
    logger.info("Hi "+name)
    return {'message': f'Welcome to GeeksforGeeks!, {name}'}


# Defining path operation for /predict endpoint
@app.post('/predict')
def predict(data : request_body):
    test_data = [[
            data.sepal_length, 
            data.sepal_width, 
            data.petal_length, 
            data.petal_width
    ]]
    target_name = gaussianNb.predict(test_data)
    logger.info("predict result: "+target_name)
    return { 'class' : target_name}
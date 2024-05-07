import logging
from datetime import datetime

import os
import sys

LOG_DIR='Insurance_log' #NAme of the root directory
CURRENT_TIME_STAMP = datetime.now().strftime("%Y-%m-%d-%H_%M_%S") #Current time stamp
LOG_FILE_NAME=f"log_{CURRENT_TIME_STAMP}.log" #log file will be created with current time stamp
FORMAT = '[%(asctime)s] %(name)s - %(levelname)s - %(message)s' #fORMAT OF logging copied from https://docs.python.org/3/library/logging.html


#Lets first make the root directory if it is not present
os.makedirs(LOG_DIR,exist_ok=True)

#Lets now create the files where our logs will be savedl.
LOG_FILE_PATH=os.path.join(LOG_DIR,LOG_FILE_NAME)

logging.basicConfig(filename=LOG_FILE_PATH,
                    filemode='w',
                    format=FORMAT,
                    level=logging.INFO #this level can be set at different level according to requirements
                    )
import logging
import requests
import time

# LOGGER CONFIG
logging.basicConfig(
    filename="info.log",
    format='%(asctime)s %(levelname)s: %(message)s'
)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# VARIABLES
API= 'https://remoteok.com/api'
data = []
last_update_time = 0

# LOGICAL FUNCTIONS
def get_data():
    logger.info("Attempting to retrieve data!")
    global data, last_update_time
    current_time = time.time()
    if not data or (current_time-last_update_time>=600):
        try:
            response = requests.get(API, timeout=5)
            logger.info("Data retrieved successfully!")
            data = response.json()
            last_update_time= current_time
            return data
        except Exception as e:
            logger.exception("Failed to retrieve data")
            return f"Unexpected error occured: {e}"
    else:
        return data


# TEST 
# data = get_data()
# n = int(input('Specify the number of jobs to list: '))
# for i in range(1,n+1):
#     print(data)
#     print('Job Description:')
#     print(f'Position: {data[i]["position"]}')
#     if data[i].get("tags"):
#         print(f'Specifications: {', '.join(data[i]["tags"])}')
#     else:
#         print(f'Specifications:No tags found.')
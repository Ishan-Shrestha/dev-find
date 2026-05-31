import requests
import logging

# LOGGER CONFIG
logging.basicConfig(
    filename="info.log",
    format='%(asctime)s %(levelname)s: %(message)s'
)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# VARIABLES
API= 'https://remoteok.com/api'

# LOGICAL FUNCTIONS
def get_data():
    logger.info("Attempting to retrieve data!")
    try:
        response = requests.get(API, timeout=5)
        logger.info("Data retrieved successfully!")
        return response.json()
    except Exception as e:
        logger.exception("Failed to retrieve data")
        return f"Unexpected error occured: {e}"
    
data = get_data()
n = int(input('Specify the number of jobs to list: '))
for i in range(1,n+1):
    print('Job Description:')
    print(f'Position: {data[i]["position"]}')
    if data[i].get("tags"):
        print(f'Specifications: {', '.join(data[i]["tags"])}')
    else:
        print(f'Specifications:No tags found.')
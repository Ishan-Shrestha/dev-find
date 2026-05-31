import logging
from flask import Flask, request, jsonify
from fetch import get_data

# LOGGER CONFIG
logging.basicConfig(
    filename="info.log",
    format='%(asctime)s %(levelname)s: %(message)s'
)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# FLASK APP SETUP
app = Flask(__name__)

# ROUTES 
@app.route('/api/jobs')
def get_jobs():
    limit = request.args.get('n', default=10, type=int)
    data = get_data()
    requested_data = []
    for i in range(1, limit+1):
        if data[i].get("tags"):
            tempt = {"position":data[i]["position"], "tags":data[i]["tags"]}
        else:
            tempt = {"position":data[i]["position"], "tags":"No tags found."}
        requested_data.append(tempt)
    return jsonify(requested_data)


if __name__ == '__main__':
    app.run(debug=True)
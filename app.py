import logging
from flask import Flask, request, jsonify, render_template
from fetch import get_data
from collections import Counter
import os

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
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/jobs')
def get_jobs():
    limit = request.args.get('n', default=10, type=int)
    data = get_data()
    if isinstance(data, list):
        requested_data = []
        for i in range(1, limit+1):
            if data[i].get("tags"):
                tempt = {"position":data[i]["position"], "tags":data[i]["tags"]}
            else:
                tempt = {"position":data[i]["position"], "tags":"No tags found."}
            requested_data.append(tempt)
        return jsonify(requested_data)
    else:
        return jsonify({"error": "Service unavailable"}), 503

@app.route('/api/skills')
def get_skills():
    data = get_data()
    if isinstance(data, list):
        skill_set = [ skill
            for dict in data
            for skill in dict.get('tags', [])
        ]
        skill_count = Counter(skill_set)
        sorted_data = [
            {'skill':skill, 'count':count}
            for skill, count in skill_count.most_common()
        ]
        return jsonify(sorted_data)
    else:
        return jsonify({"error": "Service unavailable"}), 503

@app.route('/api/jobs/search/')
def search_job():
    if request.args.get('query')==None:
        return jsonify({"error": "No search query provided"}), 400
    else:
        specification = request.args.get('query', type=str).lower()
    data = get_data()
    if isinstance(data, list):
        required_data = []
        for job in data:
            if job.get("position", '').lower()== specification or any(specification == tag.lower() for tag in job.get("tags",[])):
                temp = {"position":job["position"], "tags":job["tags"]}
                required_data.append(temp)
        return jsonify(required_data)      
    else:
        return jsonify({"error": "Service unavailable"}), 503

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
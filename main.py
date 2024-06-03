from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import requests

load_dotenv("/var/devops/ui/.env")

app = Flask(__name__)

application_host = os.getenv("APPLICATION_HOST", "0.0.0.0")
application_port = os.getenv("APPLICATION_PORT", 8888)
backend_api_url = os.getenv("BACKEND_API_URL", "http://0.0.0.0:8080")

@app.route("/get", methods=["GET"])
def start():
    response = requests.get(backend_api_url + "/getdb")
    d = response.json()
    return jsonify(d)

app.run(host=application_host, port=application_port)
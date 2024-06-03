from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os

load_dotenv("/var/devops/flask_app/.env")

app = Flask(__name__)
postgres_host = os.getenv("POSTGRES_HOST", "localhost")
postgres_port = os.getenv("POSTGRES_PORT", "5432")
postgres_user = os.getenv("POSTGRES_USER", "postgres")
postgres_password = os.getenv("POSTGRES_PASSWORD", "postgres")
postgres_db = os.getenv("POSTGRES_DB", "postgres")
application_host = os.getenv("APPLICATION_HOST", "0.0.0.0")
application_port = os.getenv("APPLICATION_PORT", 8888)


@app.route("/api/v1/user/sum", methods=["POST"])
def start():
    a = request.json.get("a", "")
    b = request.json.get("b", "")
    d = {
        "a": a,
        "b": b
    }
    return jsonify(d)

@app.route("/getdb", methods=["GET"])
def getversion():
    response = {
        "postgres_host": postgres_host, 
        "postgres_port": postgres_port,
        "postgres_user": postgres_user,
        "postgres_password": postgres_password,
        "postgres_db": postgres_db
    }
    return jsonify(response)

@app.route("/hi")
def hi():
    return "Hi"

@app.route("/bye")
def bye():
    return "Bye"

app.run(host=application_host, port=application_port)
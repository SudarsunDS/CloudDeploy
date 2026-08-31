from flask import Flask, render_template
import os
import socket
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():

    deployment_info = {
        "environment": os.getenv("ENVIRONMENT", "IBM Cloud"),
        "hostname": socket.gethostname(),
        "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"),
        "platform": "IBM Code Engine"
    }

    return render_template(
        "index.html",
        info=deployment_info
    )


@app.route("/health")
def health():

    return {
        "status": "healthy",
        "service": "clouddeploy",
        "platform": "IBM Code Engine"
    }


@app.route("/api/info")
def api_info():

    return {
        "application": "CloudDeploy",
        "architecture": "Containerized Serverless Application",
        "container_runtime": "Docker",
        "cloud_platform": "IBM Cloud",
        "deployment_service": "IBM Code Engine"
    }


if __name__ == "__main__":

    port = int(
        os.environ.get("PORT", 8080)
    )

    app.run(
        host="0.0.0.0",
        port=port
    )

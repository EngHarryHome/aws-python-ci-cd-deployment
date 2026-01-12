from flask import Flask, jsonify
import os
from datetime import datetime, timezone

def create_app():
    app = Flask(__name__)

    @app.get("/health")
    def health():
        return jsonify(status="ok"), 200

    @app.get("/time")
    def time():
        return jsonify(utc=datetime.now(timezone.utc).isoformat()), 200

    @app.get("/")
    def root():
        return jsonify(
            service="aws-python-ci-cd-deployment",
            version=os.getenv("APP_VERSION", "dev")
        ), 200

    return app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "8000")))


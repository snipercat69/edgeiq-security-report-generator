#!/usr/bin/env python3
"""
EdgeIQ Security Report Generator — Web Server
Serves the report generator via HTTP API.
"""

import subprocess
import sys
import os

from flask import Flask, request, jsonify, send_file
from pathlib import Path

app = Flask(__name__)

# Resolve the report generator script relative to this file
SCRIPT_DIR = Path(__file__).parent
GENERATOR_SCRIPT = SCRIPT_DIR / "report_generator.py"


@app.route("/health")
def health():
    return jsonify({"status": "ok", "service": "edgeiq-security-report-generator"})


@app.route("/generate", methods=["POST"])
def generate():
    """
    Generate a security report.
    Expects JSON body with:
      - config: path to config file (optional, defaults to config.json)
      - format: html | text | json (optional, defaults to html)
      - targets: list of targets (optional)
    """
    data = request.get_json() or {}

    config_path = data.get("config", "config.json")
    report_format = data.get("format", "html")
    targets = data.get("targets", [])

    if not os.path.exists(config_path):
        return jsonify({"error": f"Config file not found: {config_path}"}), 400

    cmd = [
        sys.executable,
        str(GENERATOR_SCRIPT),
        "--config", config_path,
        "--format", report_format,
    ]

    for target in targets:
        cmd.extend(["--targets", target])

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=300,
            cwd=str(SCRIPT_DIR),
        )
        if result.returncode == 0:
            return jsonify({"status": "success", "output": result.stdout})
        else:
            return jsonify({"error": result.stderr or "Generation failed", "returncode": result.returncode}), 500
    except subprocess.TimeoutExpired:
        return jsonify({"error": "Generation timed out after 300 seconds"}), 504
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/")
def index():
    return jsonify({
        "service": "EdgeIQ Security Report Generator",
        "version": "1.0.0",
        "endpoints": {
            "GET /health": "Health check",
            "POST /generate": "Generate a report (JSON body: config, format, targets)",
        }
    })


if __name__ == "__main__":
    # Read PORT from environment (set by Coolify/nixpacks)
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
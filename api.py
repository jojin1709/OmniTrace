import sys
import os
import tempfile
sys.path.insert(0, '.')
from engine.orchestrator import OmniTraceOrchestrator
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder='web', static_url_path='/static')
orchestrator = OmniTraceOrchestrator()


@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response


@app.route('/', methods=['GET'])
def index():
    return send_from_directory('web', 'dashboard.html')


@app.route('/dashboard', methods=['GET'])
def dashboard():
    return send_from_directory('web', 'dashboard.html')


@app.route('/trace', methods=['POST', 'OPTIONS'])
def trace():
    if request.method == 'OPTIONS':
        return jsonify({}), 200

    data = {}
    try:
        if request.form:
            data = request.form.to_dict()
        elif request.get_json(silent=True):
            data = request.get_json(silent=True) or {}
    except Exception:
        data = {}

    if 'photo' in request.files:
        photo = request.files['photo']
        fd, temp_path = tempfile.mkstemp(suffix='.jpg')
        os.close(fd)
        photo.save(temp_path)
        data['photo'] = temp_path

    try:
        dossier = orchestrator.trace(data)
        return jsonify({
            'target': dossier.target,
            'findings': dossier.findings,
            'graph': dossier.graph,
            'confidence': dossier.confidence_score,
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if 'photo' in data and isinstance(data['photo'], str) and os.path.exists(data['photo']):
            try:
                os.remove(data['photo'])
            except Exception:
                pass


@app.route('/check-username', methods=['POST'])
def check_username():
    data = request.get_json(force=True) or {}
    return jsonify({'status': 'stubbed', 'data': data})


@app.route('/identify-place', methods=['POST'])
def identify_place():
    return jsonify({'status': 'stubbed'})


@app.route('/investigate-email', methods=['POST'])
def investigate_email():
    data = request.get_json(force=True) or {}
    return jsonify({'status': 'stubbed', 'data': data})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

import flask
from flask import Flask, jsonify, request, make_response
from uuid import uuid4
import qu_captcha
import time

app = Flask(__name__)

captcha_engine = qu_captcha.CaptchaEngine()
humans = qu_captcha.ExpiringDict(120)
ip_addresses = qu_captcha.ExpiringDict(120)
api_tokens = ['secret_token1', 'secret_token2']


def is_repeating_request():
    ip = request.remote_addr
    val = ip_addresses.get(ip, False)
    ip_addresses.set(ip, True)
    return val


def add_cors(r):
    r.headers['Access-Control-Allow-Origin'] = '*'
    r.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    r.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return r


@app.before_request
def handle_options_request():
    if request.method == 'OPTIONS':
        return add_cors(make_response('', 200))


@app.route('/get_task', methods=['GET'])
def get_task():
    # if is_repeating_request():
    #     time.sleep(1.5)

    user_agent = request.user_agent.string.lower()
    is_mobile = 'mobile' in user_agent

    task_id, image = captcha_engine.get(is_mobile)
    return add_cors(jsonify({
        'task_id': task_id,
        'image': image
    }))


@app.route('/check_task', methods=['POST'])
def check_task():
    answer = request.json
    task_id = answer.get("task_id", None)
    user_dots = answer.get("user_dots", None)

    if not (task_id and user_dots):
        return add_cors(jsonify({"solved": False, "human_token": "", "solution": None}))

    result, solution = captcha_engine.check(task_id, user_dots)
    if result:
        human_token = str(uuid4())
        humans.set(human_token, request.remote_addr)
        return add_cors(jsonify({"solved": True, "human_token": human_token, "solution": None}))

    return add_cors(jsonify({"solved": False, "human_token": "", "solution": solution}))


@app.route('/validate_captcha', methods=['POST'])
def validate_captcha():
    answer = request.json
    api_token = answer.get("api_token", "")
    if api_token not in api_tokens:
        return add_cors(jsonify({"valid": False})), 403
    human_token = answer.get("human_token", "")

    ip = humans.get(human_token, False)
    if ip:
        humans.remove(human_token)
        return add_cors(jsonify({"valid": True, "ip": ip}))
    else:
        return add_cors(jsonify({"valid": False}))


@app.route('/get_api', methods=['GET'])
def get_api():
    return add_cors(flask.send_from_directory('static', 'qu_captcha.js'))


if __name__ == "__main__":
    app.run(debug=True, threaded=True, host='0.0.0.0', port=7000)

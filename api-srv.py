import json
import semver
from flask import Flask, request, jsonify

app = Flask(__name__)

# updates.json ファイルを読み込む関数
def load_version_info():
    with open('updates.json') as f:
        return json.load(f)

@app.route('/check_update', methods=['POST'])
def check_update():
    data = request.json
    game_name = data.get('game_title')  # 'game_name' から 'game_title' に変更
    client_version = data.get('current_version')  # 'version' から 'current_version' に変更
    request_hash = data.get('request_hash', False)
    
    if not game_name or not client_version:
        return jsonify({"error": "game_title and current_version are required"}), 400

    version_info = load_version_info()

    game_info = version_info.get(game_name)
    if not game_info:
        return jsonify({"error": "Game not found"}), 404

    latest_version = game_info["latest_version"]
    update_url = game_info["update_url"]
    update_hash = game_info.get("update_hash", "")

    if semver.compare(client_version, latest_version) < 0:
        response = {
            "update_needed": True,
            "latest_version": latest_version,
            "update_url": update_url
        }
        if request_hash:
            response["update_hash"] = update_hash
        return jsonify(response)
    else:
        return jsonify({"update_needed": False})

if __name__ == '__main__':
    app.run(debug=True)

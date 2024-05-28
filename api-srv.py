from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# updates.jsonファイルを読み込む関数
def load_updates():
    with open('updates.json', 'r') as file:
        return json.load(file)

@app.route('/check_update', methods=['POST'])
def check_update():
    data = request.json
    game_title = data.get('game_title')
    current_version = data.get('current_version')

    if not game_title or not current_version:
        return jsonify({"error": "game_title and current_version are required"}), 400

    updates = load_updates()
    game_info = updates.get('games', {}).get(game_title)

    if not game_info:
        return jsonify({"error": "Game not found"}), 404

    latest_version = game_info.get('latest_version')
    update_url = game_info.get('update_url')

    if current_version == latest_version:
        return jsonify({"message": "No update needed"})
    else:
        return jsonify({"latest_version": latest_version, "update_url": update_url})

if __name__ == '__main__':
    app.run(debug=True)

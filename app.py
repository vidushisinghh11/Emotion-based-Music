from flask import Flask, request, jsonify
from model import detect_emotion
from recommender import recommend_songs

app = Flask(__name__)

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    text = data.get('text', '')
    if not text:
        return jsonify({"error": "Text input is required"}), 400

    emotion = detect_emotion(text)
    songs = recommend_songs(emotion)
    return jsonify({"emotion": emotion, "songs": songs})

if __name__ == '__main__':
    app.run(debug=True)

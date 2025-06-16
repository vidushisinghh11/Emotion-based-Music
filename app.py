from flask import Flask, request, jsonify, render_template
from model import detect_emotion
from recommender import recommend_songs

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        emotions = detect_emotion(text)
        songs = recommend_songs(emotions)
        return render_template('index.html', text=text, emotions=emotions, songs=songs)
    return render_template('index.html')


@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    text = data.get('text', '').strip()
    
    if not text:
        return jsonify({"error": "Text input is required"}), 400

    emotions = detect_emotion(text)
    songs = recommend_songs(emotions)
    
    return jsonify({"emotions": emotions, "songs": songs})

if __name__ == '__main__':
    print("🎵 Emotion-Based Music Recommender Backend is running!")
    app.run(debug=True)

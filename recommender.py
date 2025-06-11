import json

# Load songs from file
with open("songs.json", "r") as file:
    emotion_song_map = json.load(file)

def recommend_songs(emotion):
    return emotion_song_map.get(emotion, ["No songs found for this emotion."])

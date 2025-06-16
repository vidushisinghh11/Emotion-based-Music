from spotify_auth import get_spotify_client

emotion_to_genre = {
    "joy": "happy",
    "sadness": "sad",
    "anger": "rock",
    "fear": "ambient",
    "surprise": "indie",
    "neutral": "chill"
}

def recommend_songs(emotions):
    sp = get_spotify_client()
    results = []
    for emotion in emotions:
        genre = emotion_to_genre.get(emotion, "pop")
        query = f"{genre} music"
        search = sp.search(q=query, type='track', limit=5)
        for item in search['tracks']['items']:
            name = item['name']
            artist = item['artists'][0]['name']
            url = item['external_urls']['spotify']
            results.append(f"{name} by {artist} - [Listen]({url})")
    return results or ["No songs found."]

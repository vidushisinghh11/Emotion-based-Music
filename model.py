from transformers import pipeline

# Load the emotion detection pipeline
classifier = pipeline(
    "text-classification",
    model="bhadresh-savani/distilbert-base-uncased-emotion",
    return_all_scores=True
)

def detect_emotion(text):
    result = classifier(text)
    print("Raw model output:", result)
    # Sort by score, take top 1 or 2 emotions
    top_emotions = sorted(result[0], key=lambda x: x['score'], reverse=True)[:2]
    return [e['label'].lower() for e in top_emotions]

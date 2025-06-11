from transformers import pipeline

# Load the emotion detection model
classifier = pipeline("text-classification", model="mkpvishnu/miniLM-go_Emotions")

def detect_emotion(text):
    result = classifier(text)
    return result[0]['label']

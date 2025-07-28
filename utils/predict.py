import tensorflow as tf
import pickle
import numpy as np

# Load model, tokenizer, and label encoder
model = tf.keras.models.load_model("sentiment_model.h5")

with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

with open("label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)

def predict_sentiment(text):
    seq = tokenizer.texts_to_sequences([text])
    padded = tf.keras.preprocessing.sequence.pad_sequences(seq, maxlen=100)
    pred = model.predict(padded)[0]
    label = label_encoder.inverse_transform([np.argmax(pred)])[0]
    confidence = np.max(pred) * 100
    return label, confidence

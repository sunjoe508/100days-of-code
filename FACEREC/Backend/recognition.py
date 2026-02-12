import face_recognition
import pickle
import os
import numpy as np

DB_PATH = "database.pkl"

def load_db():
    if os.path.exists(DB_PATH):
        with open(DB_PATH, "rb") as f:
            return pickle.load(f)
    return {"encodings": [], "names": []}

def save_db(db):
    with open(DB_PATH, "wb") as f:
        pickle.dump(db, f)

def register_face(image_bytes, name):
    db = load_db()
    image = face_recognition.load_image_file(image_bytes)
    encoding = face_recognition.face_encodings(image)

    if len(encoding) == 0:
        return {"error": "No face detected"}

    db["encodings"].append(encoding[0])
    db["names"].append(name)
    save_db(db)

    return {"status": "registered"}

def recognize_face(image_bytes):
    db = load_db()
    image = face_recognition.load_image_file(image_bytes)
    encoding = face_recognition.face_encodings(image)

    if len(encoding) == 0:
        return {"result": "No face detected"}

    encoding = encoding[0]
    distances = face_recognition.face_distance(db["encodings"], encoding)

    if len(distances) == 0:
        return {"result": "No database entries"}

    best_index = np.argmin(distances)
    confidence = 1 - distances[best_index]

    if confidence > 0.6:
        return {
            "result": db["names"][best_index],
            "confidence": round(confidence * 100, 2)
        }

    return {"result": "Unauthorized"}

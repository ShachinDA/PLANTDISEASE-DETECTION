from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

app = Flask(__name__)

# Upload folder
UPLOAD_FOLDER = os.path.join(os.getcwd(), "static", "uploads")
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Create uploads folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load AI model
model = load_model("plant_disease_model (1).h5")

# Temporary disease names (we will adjust later if needed)
class_names = [
"Apple Scab",
"Apple Black Rot",
"Apple Cedar Rust",
"Apple Healthy",
"Blueberry Healthy",
"Cherry Powdery Mildew",
"Cherry Healthy",
"Corn Cercospora Leaf Spot",
"Corn Common Rust",
"Corn Northern Leaf Blight",
"Corn Healthy",
"Grape Black Rot",
"Grape Esca",
"Grape Leaf Blight",
"Grape Healthy",
"Orange Haunglongbing",
"Peach Bacterial Spot",
"Peach Healthy",
"Pepper Bell Bacterial Spot",
"Pepper Bell Healthy",
"Potato Early Blight",
"Potato Late Blight",
"Potato Healthy",
"Raspberry Healthy",
"Soybean Healthy",
"Squash Powdery Mildew",
"Strawberry Leaf Scorch",
"Strawberry Healthy",
"Tomato Bacterial Spot",
"Tomato Early Blight",
"Tomato Late Blight",
"Tomato Leaf Mold",
"Tomato Septoria Leaf Spot",
"Tomato Spider Mites",
"Tomato Target Spot",
"Tomato Mosaic Virus",
"Tomato Yellow Leaf Curl Virus",
"Tomato Healthy"
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    if "leaf_image" not in request.files:
        return "No file uploaded"

    file = request.files["leaf_image"]

    if file.filename == "":
        return "No file selected"

    filename = secure_filename(file.filename)

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)

    file.save(filepath)

    # Load and prepare image
    img = image.load_img(filepath, target_size=(224, 224))
    img_array = image.img_to_array(img)

    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0

    # Model prediction
    prediction = model.predict(img_array)

    predicted_index = int(np.argmax(prediction))

    # Debug info
    print("Prediction shape:", prediction.shape)
    print("Predicted index:", predicted_index)

    # Safe prediction mapping
    try:
        predicted_class = class_names[predicted_index]
    except IndexError:
        predicted_class = f"Model predicted class index {predicted_index}"

    return render_template(
        "result.html",
        filename=filename,
        prediction=predicted_class
    )


if __name__ == "__main__":
    app.run(debug=True)
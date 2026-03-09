# 🌿 PlantCare AI – Plant Disease Detection using Transfer Learning

PlantCare AI is a deep learning-based system that detects plant diseases from leaf images using **Transfer Learning**. The project uses a pre-trained convolutional neural network to classify plant diseases accurately and efficiently.

This system can assist farmers, researchers, and agricultural experts in identifying plant diseases quickly and taking appropriate action.

---

# 🚀 Features

* Detect plant diseases from leaf images
* Uses **Transfer Learning with MobileNetV2**
* Image preprocessing and augmentation
* Model training and evaluation
* Visualization of training results
* Web interface for disease prediction

---

# 🧠 Model Used

The model used in this project is **MobileNetV2**, a lightweight deep learning architecture trained on the ImageNet dataset.

Transfer learning allows the model to reuse previously learned image features such as edges, textures, and shapes, making training faster and more efficient.

---

# 📂 Dataset

Dataset Used: **New Plant Diseases Dataset (Augmented)**
Source: Kaggle

The dataset contains thousands of images of plant leaves categorized into multiple disease classes.

### Example Classes

* Tomato Early Blight
* Tomato Late Blight
* Potato Early Blight
* Potato Healthy
* Corn Rust
* Corn Healthy

### Dataset Structure

dataset/
│
├── train/
│ ├── class_1
│ ├── class_2
│ └── ...
│
├── valid/
│ ├── class_1
│ ├── class_2
│ └── ...
│
└── test/
├── class_1
├── class_2
└── ...

---

# 🛠 Technologies Used

* Python
* TensorFlow
* Keras
* MobileNetV2
* NumPy
* Matplotlib
* Flask
* Google Colab

---

# ⚙️ Project Workflow

### 1️⃣ Dataset Collection

* Download dataset from Kaggle
* Extract dataset into training folders

### 2️⃣ Data Preprocessing

* Image resizing
* Data augmentation
* Train-validation-test split

### 3️⃣ Model Building

* Load pre-trained MobileNetV2
* Apply transfer learning
* Add custom classification layers

### 4️⃣ Model Training

* Train the model on plant leaf dataset
* Monitor training accuracy and loss

### 5️⃣ Model Evaluation

* Plot accuracy vs epochs
* Plot loss vs epochs
* Evaluate model performance

### 6️⃣ Model Deployment

* Save trained model
* Integrate with Flask web application
* Allow users to upload leaf images and detect diseases

---

# 📊 Training Visualization

The training process generates two important graphs:

* Accuracy vs Epoch
* Loss vs Epoch

These graphs help evaluate how well the model learns from the dataset.

---

# 💻 How to Run the Project

## Step 1 – Clone the Repository

git clone https://github.com/your-username/plantcare-ai.git

cd plantcare-ai

## Step 2 – Install Dependencies

pip install tensorflow flask numpy matplotlib pillow

## Step 3 – Train the Model

Run the training notebook or script to train the deep learning model.

Example:

model.fit(train_generator, validation_data=valid_generator, epochs=2)

## Step 4 – Save the Model

model.save("plant_disease_model.h5")

## Step 5 – Run Flask Application

python app.py

Open the browser and upload a plant leaf image to detect diseases.

---

# 📸 System Workflow

Upload Leaf Image
↓
AI Model Processes Image
↓
Disease Classification
↓
Result Displayed to User

---

# 📁 Project Structure

plantcare-ai/
│
├── dataset/
├── models/
│ └── plant_disease_model.h5
│
├── templates/
│ ├── index.html
│ └── result.html
│
├── static/
│ └── styles.css
│
├── app.py
├── training_notebook.ipynb
└── README.md

---

# 📈 Future Improvements

* Improve model accuracy with more training
* Add more plant species and diseases
* Deploy as a mobile application
* Provide treatment recommendations for detected diseases

---

# 📜 License

This project is created for educational and research purposes.

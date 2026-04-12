# 🌸 Flower Classification System

A deep learning-based web application that classifies flower species from images in real-time using Convolutional Neural Networks (CNN), built with TensorFlow, Keras, and deployed via Streamlit.

---

## 📌 Table of Contents

- [Overview](#overview)
- [Demo](#demo)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Dataset](#dataset)
- [Model Architecture](#model-architecture)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Future Improvements](#future-improvements)
- [Author](#author)

---

## 📖 Overview

The **Flower Classification System** is an end-to-end machine learning project that:
- Takes an input image of a flower
- Preprocesses and augments the data for robust training
- Classifies it into one of several flower species using a trained CNN model
- Displays the prediction result via an interactive Streamlit web interface

This project demonstrates hands-on skills in **Computer Vision**, **Deep Learning**, and **Model Deployment**.

---

## 🎬 Demo

> Upload any flower image through the Streamlit UI and get an instant prediction with confidence score.

```
Input Image → Preprocessing → CNN Model → Predicted Species + Confidence %
```

---

## ✨ Features

- 🌼 Multi-class flower species classification
- 🧹 Data preprocessing and augmentation pipeline
- 📊 Exploratory Data Analysis (EDA) on the dataset
- 🧠 Custom CNN model trained from scratch
- 🚀 Real-time prediction via Streamlit web app
- 📈 92% classification accuracy on test data

---

## 🛠 Tech Stack

| Category         | Tools / Libraries                        |
|------------------|------------------------------------------|
| Language         | Python 3.x                               |
| Deep Learning    | TensorFlow, Keras                        |
| Data Processing  | NumPy, Pandas                            |
| Visualization    | Matplotlib, Seaborn                      |
| Web App          | Streamlit                                |
| Development Env  | Jupyter Notebook, VS Code                |
| Version Control  | Git, GitHub                              |

---

## 📂 Dataset

- **Source**: [TF Flowers Dataset / Kaggle Flowers Dataset]  
- **Classes**: 5 flower species — `daisy`, `dandelion`, `rose`, `sunflower`, `tulip`
- **Total Images**: ~4,300 images
- **Split**:
  - Training: 80%
  - Validation: 10%
  - Testing: 10%

> Data augmentation techniques applied: horizontal flip, rotation, zoom, brightness adjustment.

---

## 🧠 Model Architecture

```
Input Image (224 x 224 x 3)
        │
   Conv2D + ReLU
        │
   MaxPooling2D
        │
   Conv2D + ReLU
        │
   MaxPooling2D
        │
   Conv2D + ReLU
        │
   MaxPooling2D
        │
   Flatten
        │
   Dense (256) + ReLU + Dropout(0.5)
        │
   Dense (5) + Softmax
        │
   Output: Predicted Flower Class
```

- **Loss Function**: Categorical Crossentropy  
- **Optimizer**: Adam  
- **Metrics**: Accuracy  
- **Epochs**: 25  
- **Batch Size**: 32  

---

## 📁 Project Structure

```
flower-classification/
│
├── dataset/
│   ├── daisy/
│   ├── dandelion/
│   ├── rose/
│   ├── sunflower/
│   └── tulip/
│
├── notebooks/
│   ├── EDA.ipynb               # Exploratory Data Analysis
│   └── model_training.ipynb    # CNN Training & Evaluation
│
├── model/
│   └── flower_model.h5         # Saved trained model
│
├── app/
│   └── app.py                  # Streamlit web application
│
├── utils/
│   └── preprocess.py           # Image preprocessing functions
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/flower-classification.git
cd flower-classification
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

**`requirements.txt`**
```
tensorflow==2.x
keras
numpy
pandas
matplotlib
seaborn
streamlit
scikit-learn
Pillow
```

---

## 🚀 Usage

### Run the Streamlit App

```bash
streamlit run app/app.py
```

Open your browser and go to: `http://localhost:8501`

### Steps:
1. Upload a flower image (`.jpg`, `.jpeg`, `.png`)
2. Click **"Classify"**
3. View the **predicted flower species** and **confidence score**

---

## 📊 Results

| Metric              | Value     |
|---------------------|-----------|
| Training Accuracy   | ~94%      |
| Validation Accuracy | ~91%      |
| Test Accuracy       | **92%**   |
| Loss (Test)         | 0.23      |

> Confusion matrix and classification report available in `notebooks/model_training.ipynb`

---

## 🔮 Future Improvements

- [ ] Add more flower classes for broader classification
- [ ] Integrate Transfer Learning (e.g., MobileNetV2, EfficientNet) for higher accuracy
- [ ] Add Grad-CAM visualization to explain model predictions
- [ ] Deploy on cloud platforms (Heroku / AWS / Hugging Face Spaces)
- [ ] Add REST API using FastAPI for programmatic access

---

## 👩‍💻 Author

**Anshu Choudhary**  
📧 anshukumari88260@gmail.com  
🔗 [LinkedIn](https://linkedin.com) | [GitHub](https://github.com)

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

> ⭐ If you found this project helpful, give it a star on GitHub!

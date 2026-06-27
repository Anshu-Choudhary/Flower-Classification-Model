import gradio as gr
import tensorflow as tf
import numpy as np
from tensorflow.keras.models import load_model

model = load_model('Flower_Recog_Model.h5')

flower_names = ['astilbe', 'bellflower', 'black_eyed_susan',
    'calendula', 'california_poppy', 'carnation',
    'common_daisy', 'coreopsis', 'dandelion', 'iris',
    'rose', 'sunflower', 'tulip', 'water_lily']

def classify_image(image):
    input_image = tf.image.resize(image, (100, 100))
    input_image = tf.expand_dims(input_image, 0)
    prediction = model.predict(input_image)
    result = tf.nn.softmax(prediction[0])
    flower = flower_names[np.argmax(result)]
    confidence = round(float(np.max(result)) * 100, 2)
    return f"🌸 This is a **{flower}** with {confidence}% confidence!"

demo = gr.Interface(
    fn=classify_image,
    inputs=gr.Image(type="numpy", label="Upload a Flower Image"),
    outputs=gr.Markdown(label="Prediction"),
    title="🌸 Flower Classification CNN",
    description="Upload a flower image and the CNN model will identify its species.",
    examples=None
)

demo.launch()
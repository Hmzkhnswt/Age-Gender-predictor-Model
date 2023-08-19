import os
from flask import Flask, request, render_template
from PIL import Image
import numpy as np
from keras.models import load_model

app = Flask(__name__)

# Load your pre-trained age and gender prediction model
age_gender_model = load_model("D:\#DATA Science\Deep Learning\Deep Learning Practice\\age_gender\\age_gender_model.h5")

def predict_age_gender(image_path):
    image = Image.open(image_path)
    image = image.resize((200, 200))  # Resize the image to match your model's input size
    image_array = np.array(image) / 255.0  # Normalize pixel values

    # Make prediction using the loaded model
    prediction = age_gender_model.predict(np.expand_dims(image_array, axis=0))

    age_prediction, gender_prediction = prediction[0], prediction[1]

    # Assuming the model output format: [age_prediction, gender_prediction]
    predicted_age = int(age_prediction)
    predicted_gender = "Female" if gender_prediction > 0.5 else "Male"

    return predicted_age, predicted_gender

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        image = request.files['image']
        if image:
            # Get the absolute path to the 'uploads' directory
            uploads_dir = os.path.join(os.path.dirname(__file__), 'uploads')
            os.makedirs(uploads_dir, exist_ok=True)  # Create the directory if it doesn't exist
            image_path = os.path.join(uploads_dir, image.filename)
            image.save(image_path)
            predicted_age, predicted_gender = predict_age_gender(image_path)
            return render_template('result.html', age=predicted_age, gender=predicted_gender, image_path=image.filename)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

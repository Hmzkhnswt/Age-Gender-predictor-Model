# Age and Gender Prediction Flask App

![App Demo](demo.png)

## Overview

This repository contains a Flask web application that utilizes a machine learning model to predict the age and gender of users based on certain input features. The model has been trained on a carefully curated dataset and has been integrated into a user-friendly web interface using Flask, allowing users to input relevant information and receive predictions in real-time.

## Features

- Age and gender prediction using a pre-trained machine learning model.
- User-friendly web interface powered by Flask.
- Data export functionality using Pickle for future analysis.

## Getting Started

### Prerequisites

- Python 3.6 or later
- Flask
- Scikit-learn
- Pandas

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/age-gender-prediction-flask.git
   cd age-gender-prediction-flask
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Run the Flask app:

   ```bash
   python app.py
   ```

2. Open your web browser and navigate to `http://localhost:5000`.

3. Input the necessary features and submit the form to get the age and gender predictions.

4. You can also export the data and predictions using the provided export functionality.

## Model Details

The machine learning model used in this project is a trained model that predicts age and gender based on input features. The model has been trained on a labeled dataset and achieved an accuracy of X% on the validation set.

## Project Structure

- `app.py`: Main Flask application script.
- `model.py`: Contains code for loading the pre-trained machine learning model.
- `templates/`: Contains HTML templates for the web interface.
- `static/`: Contains static files such as CSS and JavaScript.

## Future Improvements

- Include additional features for more accurate predictions.
- Enhance the user interface for better user experience.
- Implement user authentication and data privacy measures.

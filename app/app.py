from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np

model_path = "/root/app/model.keras"
# Load the trained model
model = tf.keras.models.load_model(model_path)

# Define class names
class_names = {
    0: 'Tomato___Bacterial_spot',
    1: 'Tomato___Early_blight',
    2: 'Tomato___Late_blight',
    3: 'Tomato___Leaf_Mold',
    4: 'Tomato___Septoria_leaf_spot',
    5: 'Tomato___Spider_mites Two-spotted_spider_mite',
    6: 'Tomato___Target_Spot',
    7: 'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
    8: 'Tomato___Tomato_mosaic_virus',
    9: 'Tomato___healthy'
}

# Create a Flask app
app = Flask(__name__)

# Define a route for the prediction endpoint


@app.route('/predict', methods=['POST'])
def predict():
    image_path = "./image.jpg"
    file = request.files['image']
    # save the image
    file.save(image_path)
    # load the image using tf and resize it
    image = tf.keras.preprocessing.image.load_img(
        image_path, target_size=(128, 128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])
    # use model for prediction
    predictions = model.predict(input_arr)
    # Get the predicted class
    predicted_class = np.argmax(predictions[0])
    # Get the class name
    class_name = class_names.get(predicted_class, 'Unknown')
    # Return the result as JSON
    return jsonify({'class_name': class_name})


# Run the Flask app
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, debug=True)

import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

model = tf.keras.models.load_model('models/tyre_condition.h5')

def model_predict(img_filepath):

    test_image = image.load_img(img_filepath, target_size = (224, 224)) # Get the image

    transformed_image = image.img_to_array(test_image) # Transform image to array
    transformed_image = np.expand_dims(transformed_image, axis=0) # Expand dims to make a batch of 1 image
    prediction = model.predict(transformed_image)

    print(prediction)

    result = None

    if prediction[0] < 0.5:
        result = True
    else:
        result = False
    
    return result

model_result = model_predict(r"C:\Users\sas\Downloads\tyre3_img.png")
print(model_result)
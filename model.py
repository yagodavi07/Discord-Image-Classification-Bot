from tf_keras.models import load_model
import numpy as np
from PIL import Image

def get_class(model_path, labels_path, image_path):
    model = load_model(model_path, compile=False)

    with open(labels_path, "r") as file:
        labels = [line.strip() for line in file.readlines()]

    image = Image.open(image_path).convert("RGB")
    image = image.resize((224, 224))

    image_array = np.asarray(image)
    normalized_image = (image_array.astype(np.float32) / 127.5) - 1

    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = normalized_image

    prediction = model.predict(data, verbose=0)
    index = np.argmax(prediction)

    class_name = labels[index].split(" ", 1)[1]
    probability = prediction[0][index]

    return class_name + " - " + str(round(probability * 100, 2)) + "%"
import tensorflow as tf
from PIL import Image
import numpy as np


class XceptionNetClassifier:
    def __init__(self):
        self.model_path = 'xception_model.tflite'
        self.class_labels = [
            'Tomato___Late_blight','Orange___Haunglongbing_(Citrus_greening)','Squash___Powdery_mildew','Corn_(maize)___Northern_Leaf_Blight','Tomato___Early_blight',
            'Tomato___Septoria_leaf_spot','Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
            'Strawberry___Leaf_scorch','Apple___Apple_scab','Tomato___Tomato_Yellow_Leaf_Curl_Virus','Tomato___Bacterial_spot',
            'Apple___Black_rot','Cherry_(including_sour)___Powdery_mildew','Peach___Bacterial_spot','Apple___Cedar_apple_rust',
            'Tomato___Target_Spot','Grape___Leaf_blight_(Isariopsis_Leaf_Spot)','Potato___Late_blight',
            'Tomato___Tomato_mosaic_virus','Grape___Black_rot','Potato___Early_blight','Corn_(maize)___Common_rust_',
            'Grape___Esca_(Black_Measles)','Tomato___Leaf_Mold',
            'Tomato___Spider_mites_Two-spotted_spider_mite','Pepper,_bell___Bacterial_spot',
            'Apple___healthy','Blueberry___healthy','Cherry_(including_sour)___healthy','Corn_(maize)___healthy',
            'Grape___healthy','Peach___healthy','Pepper,_bell___healthy','Potato___healthy','Raspberry___healthy','Soybean___healthy',
            'Strawberry___healthy','Tomato___healthy'
        ]

        self.interpreter = tf.lite.Interpreter(model_path=self.model_path)
        self.interpreter.allocate_tensors()

        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()

    def preprocess_image(self, image):
        image = image.convert('RGB')
        input_shape = self.input_details[0]['shape'][1:3]
        image = image.resize(input_shape)
        image_array = np.array(image) / 255.0
        image_array = np.expand_dims(image_array, axis=0)
        return image_array

    def classify_image(self, image):
        image_array = self.preprocess_image(image)
        self.interpreter.set_tensor(self.input_details[0]['index'], image_array.astype(np.float32))
        self.interpreter.invoke()
        output_tensor = self.interpreter.get_tensor(self.output_details[0]['index'])
        predicted_idx = np.argmax(output_tensor)

        print("Predicted index:", predicted_idx)
        print("Number of classes:", len(self.class_labels))

        if predicted_idx >= 0 and predicted_idx < len(self.class_labels):
            predicted_label = self.class_labels[predicted_idx]
        else:
            print("Invalid predicted index:", predicted_idx)
            predicted_label = "Unknown"
    
        treatment, pesticide = self.get_treatment_and_pesticide(predicted_label)
        return predicted_label, treatment, pesticide

    def get_treatment_and_pesticide(self, predicted_label):
        # Add your logic here to map predicted_label to treatment and pesticide
        # Define the treatment and pesticide information based on the predicted_label
        if predicted_label == 'Tomato___Late_blight':
            treatment = 'Remove and destroy infected plant parts, practice crop rotation, provide good air circulation, and avoid overhead watering.'
            pesticide = 'Fungicides containing active ingredients such as chlorothalonil, mancozeb, or copper-based fungicides.'
        elif predicted_label == 'Orange___Haunglongbing_(Citrus_greening)':
            treatment = 'There is no known cure for this disease. Cultural practices like removing and destroying infected plants, controlling insect vectors, and improving plant health are important.'
            pesticide = 'No specific pesticides are effective against Huanglongbing. Insecticides can be used to control the psyllid vector.'
        elif predicted_label == 'Squash___Powdery_mildew':
            treatment = 'Provide proper spacing between plants, promote air circulation, practice good watering techniques, and remove infected plant parts.'
            pesticide = 'Fungicides containing active ingredients like sulfur, potassium bicarbonate, or myclobutanil.'
        elif predicted_label == 'Corn_(maize)___Northern_Leaf_Blight':
            treatment = 'Crop rotation, planting resistant varieties, and providing balanced nutrition can help manage the disease.'
            pesticide = 'Fungicides containing active ingredients such as azoxystrobin, pyraclostrobin, or triazoles.'
        elif predicted_label == 'Tomato___Early_blight':
            treatment = 'Practice crop rotation, remove infected leaves, provide good air circulation, and avoid overhead watering.'
            pesticide = 'Fungicides containing active ingredients like chlorothalonil, mancozeb, or azoxystrobin.'
        elif predicted_label == 'Tomato___Septoria_leaf_spot':
            treatment = 'Remove and destroy infected plant parts, practice crop rotation, and avoid overhead watering.'
            pesticide = 'Fungicides containing active ingredients like chlorothalonil, mancozeb, or azoxystrobin.'
        elif predicted_label == 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot':
            treatment = 'Crop rotation, planting resistant varieties, and providing balanced nutrition can help manage the disease.'
            pesticide = 'Fungicides containing active ingredients such as azoxystrobin, pyraclostrobin, or triazoles.'
        elif predicted_label == 'Strawberry___Leaf_scorch':
            treatment = 'Remove and destroy infected plants, practice crop rotation, and provide proper irrigation and drainage.'
            pesticide = 'Fungicides containing active ingredients like myclobutanil or thiophanate-methyl.'
        elif predicted_label == 'Apple___Apple_scab':
            treatment = 'Remove and destroy infected leaves, practice good sanitation, and use resistant apple varieties.'
            pesticide = 'Fungicides containing active ingredients such as myclobutanil, captan, or thiophanate-methyl.'
        elif predicted_label == 'Tomato___Tomato_Yellow_Leaf_Curl_Virus':
            treatment = 'Use resistant/tolerant tomato varieties and control the whitefly vector.'
            pesticide = 'Insecticides targeting whiteflies, such as neonicotinoids or pyrethroids.'
        elif predicted_label == 'Tomato___Bacterial_spot':
            treatment = 'Remove and destroy infected plant parts, practice crop rotation, avoid overhead watering, and use copper-based sprays.'
            pesticide = 'Copper-based bactericides can be used for control.'
        elif predicted_label == 'Apple___Black_rot':
            treatment = 'Prune and destroy infected branches, remove mummified fruits, practice good sanitation, and use fungicides.'
            pesticide = 'Fungicides containing active ingredients like captan, myclobutanil, or thiophanate-methyl.'
        elif predicted_label == 'Cherry_(including_sour)___Powdery_mildew':
            treatment = 'Prune and destroy infected plant parts, improve air circulation, and use fungicides.'
            pesticide = 'Fungicides containing active ingredients like myclobutanil, sulfur, or potassium bicarbonate.'
        elif predicted_label == 'Peach___Bacterial_spot':
            treatment = 'Prune and destroy infected branches, practice good sanitation, and use copper-based sprays.'
            pesticide = 'Copper-based bactericides can be used for control.'
        elif predicted_label == 'Apple___Cedar_apple_rust':
            treatment = 'Remove and destroy infected galls, practice good sanitation, and use fungicides.'
            pesticide = 'Fungicides containing active ingredients like myclobutanil, thiophanate-methyl, or propiconazole.'
        elif predicted_label == 'Tomato___Target_Spot':
            treatment = 'Remove and destroy infected plant parts, practice good sanitation, and use fungicides.'
            pesticide = 'Fungicides containing active ingredients like chlorothalonil, azoxystrobin, or pyraclostrobin.'
        elif predicted_label == 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)':
            treatment = 'Remove and destroy infected leaves, practice good sanitation, and use fungicides.'
            pesticide = 'Fungicides containing active ingredients like myclobutanil, trifloxystrobin, or pyraclostrobin.'
        elif predicted_label == 'Potato___Late_blight':
            treatment = 'Remove and destroy infected plant parts, practice good sanitation, and use fungicides.'
            pesticide = 'Fungicides containing active ingredients like chlorothalonil, mancozeb, or metalaxyl.'
        elif predicted_label == 'Tomato___Tomato_mosaic_virus':
            treatment = 'Remove and destroy infected plants, control aphid vectors, and practice good sanitation.'
            pesticide = 'No specific pesticides are effective against viruses. Focus on prevention and control of vectors.'
        elif predicted_label == 'Grape___Black_rot':
            treatment = 'Prune and destroy infected plant parts, practice good sanitation, and use fungicides.'
            pesticide = 'Fungicides containing active ingredients like myclobutanil, mancozeb, or captan.'
        elif predicted_label == 'Potato___Early_blight':
            treatment = 'Remove and destroy infected plant parts, practice crop rotation, and use fungicides.'
            pesticide = 'Fungicides containing active ingredients like chlorothalonil, mancozeb, or azoxystrobin.'
        elif predicted_label == 'Corn_(maize)___Common_rust_':
            treatment = 'Remove and destroy infected plant parts, practice good sanitation, and use fungicides.'
            pesticide = 'Fungicides containing active ingredients like triazoles, strobilurins, or propiconazole.'
        elif predicted_label == 'Grape___Esca_(Black_Measles)':
            treatment = 'Prune and destroy infected plant parts, practice good sanitation, and use fungicides.'
            pesticide = 'Fungicides containing active ingredients like tebuconazole, propiconazole, or cyprodinil.'
        elif predicted_label == 'Tomato___Leaf_Mold':
            treatment = 'Provide good air circulation, reduce humidity, and use fungicides.'
            pesticide = 'Fungicides containing active ingredients like chlorothalonil, mancozeb, or azoxystrobin.'
        elif predicted_label == 'Tomato___Spider_mites_Two-spotted_spider_mite':
            treatment = 'Control mite infestations using predatory mites, insecticidal soaps, or horticultural oils.'
            pesticide = 'Acaricides containing active ingredients like abamectin, spiromesifen, or bifenthrin.'
        elif predicted_label == 'Pepper,_bell___Bacterial_spot':
            treatment = 'Remove and destroy infected plant parts, practice crop rotation, and use copper-based sprays.'
            pesticide = 'Copper-based bactericides can be used for control.'
        elif predicted_label == 'Apple___healthy':
            treatment = 'Regular maintenance'
            pesticide = 'Not required'
        elif predicted_label == 'Blueberry___healthy':
            treatment = 'Regular maintenance'
            pesticide = 'Not required'
        elif predicted_label == 'Cherry_(including_sour)___healthy':
            treatment = 'Regular maintenance'
            pesticide = 'Not required'
        elif predicted_label == 'Corn_(maize)___healthy':
            treatment = 'Regular maintenance'
            pesticide = 'Not required'
        elif predicted_label == 'Grape___healthy':
            treatment = 'Regular maintenance'
            pesticide = 'Not required'
        elif predicted_label == 'Peach___healthy':
            treatment = 'Regular maintenance'
            pesticide = 'Not required'
        elif predicted_label == 'Pepper,_bell___healthy':
            treatment = 'Regular maintenance'
            pesticide = 'Not required'
        elif predicted_label == 'Potato___healthy':
            treatment = 'Regular maintenance'
            pesticide = 'Not required'
        elif predicted_label == 'Raspberry___healthy':
            treatment = 'Regular maintenance'
            pesticide = 'Not required'
        elif predicted_label == 'Soybean___healthy':
            treatment = 'Regular maintenance'
            pesticide = 'Not required'
        elif predicted_label == 'Strawberry___healthy':
            treatment = 'Regular maintenance'
            pesticide = 'Not required'
        elif predicted_label == 'Tomato___healthy':
            treatment = 'Regular maintenance'
            pesticide = 'Not required'
        else:
            treatment = 'Unknown treatment'
            pesticide = 'Unknown pesticide'

        return treatment, pesticide


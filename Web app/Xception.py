class XceptionNetClassifier:
    def __init__(self):
        self.model_path = 'xception_model.tflite'
        self.class_labels = [
            'Tomato___Late_blight', 'Orange___Haunglongbing_(Citrus_greening)', 'Squash___Powdery_mildew',
            'Corn_(maize)___Northern_Leaf_Blight', 'Tomato___Early_blight', 'Tomato___Septoria_leaf_spot',
            'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Strawberry___Leaf_scorch',
            'Apple___Apple_scab', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Bacterial_spot',
            'Apple___Black_rot', 'Cherry_(including_sour)___Powdery_mildew', 'Peach___Bacterial_spot',
            'Apple___Cedar_apple_rust', 'Tomato___Target_Spot', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
            'Potato___Late_blight', 'Tomato___Tomato_mosaic_virus', 'Grape___Black_rot', 'Potato___Early_blight',
            'Corn_(maize)___Common_rust_', 'Grape___Esca_(Black_Measles', 'Tomato___Leaf_Mold',
            'Tomato___Spider_mites Two-spotted_spider_mite', 'Pepper,_bell___Bacterial_spot'
        ]

    def print_num_classes(self):
        num_classes = len(self.class_labels)
        print("Number of classes:", num_classes)

# Create an instance of XceptionNetClassifier
classifier = XceptionNetClassifier()

# Call the print_num_classes method to print the number of classes
classifier.print_num_classes()

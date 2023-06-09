from flask import Flask, request, render_template
from XceptionNet_Classifier import XceptionNetClassifier
from PIL import Image

app = Flask(__name__)

# Create an instance of the classifier
classifier = XceptionNetClassifier()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Check if an image file is present in the request
        if 'image' not in request.files:
            return render_template('home.html', error='No image file found')

        image_file = request.files['image']

        if image_file.filename == '':
            return render_template('home.html', error='No image file selected')

        # Save the image file to the 'static' folder
        image_path = 'static/' + image_file.filename
        image_file.save(image_path)
    
        # Load and preprocess the image
        image = Image.open(image_path)
        image = image.resize((224, 224))

        # Classify the image and get the result
        predicted_label, treatment, pesticide = classifier.classify_image(image)

        # Check if treatment and pesticide are not None
        if treatment is not None and pesticide is not None:
            result = {
                'predicted_label': predicted_label,
                'treatment': treatment,
                'pesticide': pesticide
            }
        else:
            result = {
                'predicted_label': predicted_label,
                'treatment': 'Unknown treatment',
                'pesticide': 'Unknown pesticide'
            }

        return render_template('home.html', result=result, image_path=image_path)

    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

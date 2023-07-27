from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Set the path where uploaded photos will be saved
UPLOAD_FOLDER = 'faces'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        register_number = request.form['registerNumber']
        name = request.form['name']
        photo = request.files['photo']

        # Create the path to save the photo
        filename = f"{register_number}_{name}.{photo.filename.split('.')[-1]}"
        save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        # Save the photo to the specified path
        photo.save(save_path)

        # Perform any further processing or database insertion if needed

        return f"Registration successful! Photo saved as: {filename}"

    return render_template('register.html')

@app.route('/start_webcam')
def start_webcam():
    # Redirect to the webpage with the webcam streaming
    return render_template('start_webcam.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

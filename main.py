import cv2
import image_dehazer
import os
import numpy as np

def main():
        # Check if the user uploaded an image file
        if 'image' not in request.files:
            return redirect(request.url)
        
        image_file = request.files['image']
        
        # Check if the file is empty
        if image_file.filename == '':
            return redirect(request.url)
        
        # Check if the file has an allowed extension
        allowed_extensions = {'png', 'jpg', 'jpeg', 'gif'}
        if not (image_file.filename.split('.')[-1].lower() in allowed_extensions):
            return redirect(request.url)
        
        # Read input image
        image = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_COLOR)
        
        # Remove haze from image
        HazeCorrectedImg, haze_map = image_dehazer.remove_haze(image, showHazeTransmissionMap=False)

        # Save the output image to a file
        output_path = "outputImages/result.png"
        cv2.imwrite(output_path, HazeCorrectedImg)

        # Get the URL for the output image
        image_url = os.path.join(app.static_url_path, "outputImages/result.jpg")

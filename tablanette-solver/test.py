import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label
import skimage.io
import skimage.color
import skimage.filters
import numpy as np
import skimage.measure

import matplotlib.patches as mpatches

def detect_objects(image):
    
    gray_image = skimage.color.rgb2gray(image)

    
    blurred_image = skimage.filters.gaussian(gray_image, sigma=4)

   
    threshold = 0.61
    binary_mask = blurred_image < threshold

    
    detected_objects = np.zeros(shape=binary_mask.shape)

    
    detected_objects[binary_mask] = 1

    return detected_objects

def detect_cards(image_path):
    image = cv2.imread(image_path)
    suma=0
    if image is not None:
        
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

       
        blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

        
        _, threshold_image = cv2.threshold(blurred_image, 40, 255, cv2.THRESH_BINARY)

       
        contours, _ = cv2.findContours(threshold_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        
        filtered_contours = []
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 5000:  
                x, y, w, h = cv2.boundingRect(contour)
                aspect_ratio = w / float(h)
                if 0.5 < aspect_ratio < 2:  
                    filtered_contours.append(contour)

      
        for contour in filtered_contours:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
        
            detected_card = gray_image[y:y + h, x:x + w]

           
            card_with_contours = cv2.cvtColor(detected_card, cv2.COLOR_GRAY2BGR)
            

          
            rotated_card_image = cv2.rotate(card_with_contours, cv2.ROTATE_90_COUNTERCLOCKWISE)
       

     
            detected_objects = detect_objects(rotated_card_image)

           
            labeled_image,count = skimage.measure.label(detected_objects, return_num=True)
            
            objects = skimage.measure.regionprops(labeled_image)
            
            

         
            sorted_objects = sorted(objects, key=lambda obj: obj['area'])

            
            
            big_objects = [obj for obj in sorted_objects if 500 < obj['area']]

            suma=suma+len(big_objects)-5

            
            

    else:
        print("Unable to load image. Please check the image path.")
    print(f'Suma je {suma}')

if __name__ == "__main__":
    image_path = "3.jpg"
    detect_cards(image_path)

import streamlit as st
import numpy as np
import object_detection
from PIL import Image

def main():
    st.title('Object Detection for Images')
    file = st.file_uploader('Upload Image', type=['jpg', 'png', 'jpeg'])
    if file is not None:
        st.image(file, caption='Upload Image')
        image = Image.open(file)
        image = np.array(image)
        detections = object_detection.process_image(image)
        processed_image = object_detection.annotate_image(image, detections)
        st.image(processed_image, caption='Processed Image')

if __name__ == "__main__":
    main()

# streamlit run EXERCISES\MODULE-01\exercise-04\2-object-detection\object-detection-app.py

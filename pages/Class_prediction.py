import streamlit as st
import pickle
import numpy as np
from PIL import Image

page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
        background-image: url("https://images.pexels.com/photos/2680270/pexels-photo-2680270.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500");
        background-size: 100%;
        background-position: top left;
        background-attachment: local;
        color: white;
     }}
     [data-testid="stSidebar"] {{
        background-image: url("https://www.stockvault.net/data/2020/09/25/279184/preview16.jpg");
        background-size: 470%;
        background-position: top left;
        background-attachment: local;
    }}
    [data-testid="stHeader"] {{
        background: rgba(0, 0, 0, 0);
    }}
    [data-testid="stToolbar"] {{
        right: 2rem;
    }}
    .st-eb, .st-ec, .st-dd {{
        color: white;
    }}
    </style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

# Load your pre-trained logistic regression model from a pickle file
# Replace 'logistic_regression_model.pkl' with the actual filename of your model file.
model = pickle.load(open('Pickle\logistic_regression.pkl', 'rb'))

st.markdown(
        """
        <div>
            <h1 style="color:white;" >IMAGE CLASSIFICATION</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
st.write('Upload an image and get the model accuracy result.')

uploaded_image = st.file_uploader("Upload an image...", type=["jpg", "png", "jpeg"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Preprocess the image (resize and flatten)
    target_size = (128, 128)  # Change this to the input size your model was trained on
    image = image.resize(target_size)
    image = np.array(image)
    image = image.flatten().reshape(1, -1)  # Flatten and reshape the image to 1D array with 2 features

    # Make predictions using the loaded logistic regression model
    predicted_class = model.predict(image)
    
    st.write(f"Predicted Class: {predicted_class[0]}")

    # You can display additional information such as class labels, class probabilities, etc., based on your model.

    # You may also display the predicted class label if you have a mapping from class index to class label.

    # Display model accuracy (you need to replace 'your_accuracy' with the actual accuracy metric)
    # st.write(f"Model Accuracy: {your_accuracy}%")
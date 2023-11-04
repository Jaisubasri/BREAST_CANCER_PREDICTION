import streamlit as st
import pickle
import io
from PIL import Image
import numpy as np

page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
        background-image: url("https://thumbs.dreamstime.com/b/abstract-gradient-blue-light-background-retro-colors-lot-space-text-composition-art-image-website-magazine-97327659.jpg");
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

# Create a Streamlit sidebar with options
st.sidebar.title("Choose a Model")
selected_model = st.sidebar.selectbox(
    "Select a Model",
    ("Logistic Regression", "K Nearest Neighbors", "Support Vector Machine", "Convolutional Neural Networks - Inception", "Convolutional Neural Networks - Dense Net")
)

# Define a dictionary of model accuracies (you can replace these with actual accuracy values)
model_accuracies = {
    "Logistic Regression": 0.57,
    "K Nearest Neighbors": 0.92,
    "Support Vector Machine": 0.90,
    "Convolutional Neural Networks - Inception" : 0.90,
    "Convolutional Neural Networks - Dense Net" : 0.90
}

# Main Streamlit app
st.title("Machine Learning Model Predictions")

# Display the accuracy when a model is selected
if selected_model in model_accuracies:
    with st.expander("Model Accuracy"):
        st.write(f"Accuracy for {selected_model}: {model_accuracies[selected_model]}")

# Load the corresponding pickle file based on the selected model
model_file = None
if selected_model == "Logistic Regression":
    model_file = "logistic_regression_model.pkl"
elif selected_model == "K Nearest Neighbors":
    st.image("images\\acc_knn.png", use_column_width=True)  
elif selected_model == "Support Vector Machine":
    st.image("images\\acc_svm.png", use_column_width=True) 
else:
    # Add file for CNN models if needed
    if selected_model == "Convolutional Neural Networks - Inception":
        st.image("images\inception.png", use_column_width=True) 
    elif selected_model == "Convolutional Neural Networks - Dense Net":
        st.image("images\\acc.png", use_column_width=True)  

# Display images for CNN models
if selected_model == ["Convol"]:
    st.image("image_path_here.jpg", use_column_width=True)  
# Preprocess the uploaded image (modify this according to your model's requirements)
def preprocess_image(image):
    # Modify this function to preprocess the image for your specific model
    img = np.array(image)
    # Perform necessary preprocessing here
    return img

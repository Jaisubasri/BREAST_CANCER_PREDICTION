import streamlit as st

page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
        background-image: url("https://e0.pxfuel.com/wallpapers/1001/83/desktop-wallpaper-ipad-pro-12-9-ideas-in-2021-iphone-ipad-pro-12-9-apple-ipad-pro-black-thumbnail.jpg");
        background-size: 100%;
        background-position: top left;
        background-attachment: local;
        color: white;
     }}
     [data-testid="stSidebar"] {{
        background-image: url("https://img.freepik.com/premium-photo/green-blue-background-with-green-background-that-says-green_873925-17389.jpg?w=360");
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

# Main Streamlit app
st.markdown(
        """
        <div>
            <h1 style="color:white;" >VISUALIZATION</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

# Display images for different models
st.image("images\CALC.png", caption="DISTRIBUTION OF CALCIFICATION CANCER", use_column_width=True)
st.image("images\BENIGN.png", caption="Right and Left Case Benign Distribution", use_column_width=True)
st.image("images\DIST.png", caption="Distribution of items in the DataSet", use_column_width=True)
st.image("images\FIG1.png", caption="Types of calcification cancer", use_column_width=True)
st.image("images\IMG_ROI.png", caption="Image and ROI file count", use_column_width=True)
st.image("images\MALIGNANT.png", caption="Right and Left Case Malignant Distribution", use_column_width=True)
st.image("NAN.png", caption="NaN Body Part Distribution", use_column_width=True)
st.image("images\mass_cancer.png", caption="MASS - CANCER DISTRIBUTION", use_column_width=True)
st.image("images\mass_margin.png", caption="MASS - MARGIN DISTRIBUTION", use_column_width=True)
st.image("images\dense1.png", caption="CNN - DENSE NET ", use_column_width=True)
st.image("images\dense2.png", caption="CNN - DENSE NET", use_column_width=True)
st.image("images\log1.png", caption="LOGISTIC REGRESSION", use_column_width=True)
st.image("images\log2.png", caption="LOGISTIC REGRESSION", use_column_width=True)
st.image("images\log3.png", caption="LOGISTIC REGRESSION", use_column_width=True)

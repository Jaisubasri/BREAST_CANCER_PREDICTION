import streamlit as st

page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
        background-image: url("https://www.dentons.com/-/media/images/website/background-images/regions/united-states/us_regional_image_v7.ashx?sc_lang=en");
        background-size: 100%;
        background-position: top left;
        background-attachment: local;
        color: white;
     }}
     [data-testid="stSidebar"] {{
        background-image: url("https://png.pngtree.com/thumb_back/fh260/background/20221229/pngtree-blurred-background-brown-brass-sidebar-abstract-photo-image_20947710.jpg");
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


def about_breast_cancer_detection():
    st.markdown(
        """
        <div>
            <h1 style="color:white;" >About Breast Cancer Detection</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    with st.sidebar:
        st.markdown("Navigation")
        nav_selection = st.radio("Go to", ["About", "Problem", "Data", "Models", "Developers", "Disclaimer"])
    
    if nav_selection == "About":
        with st.expander("About"):
            st.markdown(
                """
                <span style="color: white;">This Streamlit app is designed for breast cancer detection using machine learning models like KNN,SVM AND CONVOLUTION MODELS.</span>
                """,
                unsafe_allow_html=True
            )

    if nav_selection == "Problem":
        with st.expander("Problem Statement"):
            st.markdown(
                """
                <span style="color: white;">Breast cancer is one of the most common cancers among women worldwide. Early detection
                plays a crucial role in improving the prognosis and chances of survival. This app aims to
                assist in the early detection of breast cancer by providing predictions based on machine
                learning models.</span>
                """,
                unsafe_allow_html=True
            )

    if nav_selection == "Data":
        with st.expander("Data"):
            st.markdown(
                """
                <span style="color: white;">The models used in this app are trained on a dataset containing features extracted from
                digitized breast cancer biopsies. This dataset includes information such as texture, radius,
                and more, which are used to predict whether a tumor is malignant or benign.</span>
                """,
                unsafe_allow_html=True
            )

    if nav_selection == "Models":
        with st.expander("Machine Learning Models"):
            st.markdown(
                """
                <span style="color: white;">The app utilizes machine learning models, including Logistic Regression, K Nearest Neighbors (KNN),
                Support Vector Machine (SVM), and potentially Convolutional Neural Networks (CNN), to make predictions
                based on the input data.</span>
                """,
                unsafe_allow_html=True
            )

    if nav_selection == "Developers":
        with st.expander("Developers"):
            st.markdown(
                """
                <span style="color: white;">This app is developed by JAISUBASRI K and HARSHINI TS with the goal of providing a tool for early breast
                cancer detection. If you have any questions or feedback, please feel free to contact us.</span>
                
<span style="color: white;">Our team of dedicated professionals is deeply committed to the field of healthcare and medical imaging. With a passion for improving breast health, we bring together a wealth of experience in machine learning, medical imaging, and data analysis. We continuously explore the latest advancements in the field to ensure that we provide the most reliable and cutting-edge solutions.</span>

<span style="color: white;">In this project, we harnessed our collective expertise to analyze medical images and data related to breast health. Leveraging advanced machine learning and computer vision techniques, we dissected the intricacies of breast cancer prediction. Our goal was to deliver insights that empower healthcare professionals and individuals with the ability to detect breast cancer early.</span>

<span style="color: white;">Through our analysis, we unveiled critical insights into breast health risk factors, diagnostic accuracy, and the efficacy of various predictive models. Our findings contribute to improved early detection, reduced false positives, and more informed medical decisions.</span>

<span style="color: white;">We thank you for considering our services, and we are eager to collaborate with you to make a significant impact on breast health and contribute to the well-being of individuals.</span>
                """,
                unsafe_allow_html=True
            )

    if nav_selection == "Disclaimer":
        with st.expander("Disclaimer"):
            st.markdown(
                """
                <span style="color: white;">Our mission is to provide accurate and reliable breast cancer prediction solutions that empower individuals and healthcare professionals with the tools and insights they need to make informed decisions about breast health. We are dedicated to leveraging the latest advancements in machine learning and computer vision to deliver state-of-the-art predictive models.</span>

<span style="color: white;">Our team of data scientists and healthcare experts is committed to offering comprehensive and personalized breast cancer risk assessments. We analyze medical images and data with the utmost precision, ensuring early detection and timely intervention for those at risk. We aim to contribute to the well-being of individuals by providing accessible and user-friendly tools for breast cancer prediction.</span>

<span style="color: white;">We are at the forefront of innovation, continuously researching and developing new models and techniques. Our goal is to enable early detection, reduce false positives, and improve the overall accuracy of breast cancer prediction. Our mission is to make a positive impact on breast health by providing cutting-edge solutions that save lives and empower individuals with the knowledge they need to make important decisions about their health.</span>
                """,
                unsafe_allow_html=True
            )

if __name__ == "__main__":
    about_breast_cancer_detection()

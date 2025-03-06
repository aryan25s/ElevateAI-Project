import streamlit as st
from PIL import Image
import os

def load_image(image_path):
    """Safe image loading with error handling"""
    try:
        return Image.open(image_path)
    except FileNotFoundError:
        st.error(f"Image not found: {image_path}")
        return None
    except Exception as e:
        st.error(f"Error loading image: {str(e)}")
        return None
    
def main():
    st.set_page_config(
        page_title="Kartikeya Prasad - Portfolio",
        page_icon="🎓",
        layout="wide"
    )
    
    # content
    # --- Header Section ---
    col1, col2 = st.columns([1, 2])
    with col1:
        img_path = "Images/image01.jpg"  # Assuming images folder is in the same directory
        profile_img = load_image(img_path)
        if profile_img:
            st.image(profile_img, width=250, caption="Profile Picture")
    with col2:
        st.title("Kartikeya Prasad")
        st.header("AI/ML Undergraduate Student")
        st.write("🔗 [LinkedIn](https://www.linkedin.com/in/kartikeya-prasad-41468b28b/) | 💻 [GitHub](https://github.com/kartikf4) | 📧 kartikeyaprasad407@email.com")
        st.markdown("---")
        st.write("""
        🚀 Passionate AI/ML undergraduate with expertise in:
        - Natural Language Processing
        - Computer Vision
        - Deep Learning Architectures
        - Data Science Applications
        """)    
    st.markdown("## 🎓 Education & Qualifications")
    
    edu_col1, edu_col2 = st.columns(2)
    
    with edu_col1:
        st.subheader("B.Tech in Artificial Intelligence & Machine Learning")
        st.caption("Dronacharya Group of Institutions | 2022-2026 (Expected)")
        st.write("""
        - **Relevant Coursework**:
          - Deep Learning
          - Neural Networks
          - Statistical Modeling
          - Big Data Analytics
        """)
    st.markdown("## 💻 Technical Skills")
    
    skills_col1, skills_col2, skills_col3 = st.columns(3)
    
    with skills_col1:
        st.markdown("### 🤖 Machine Learning")
        st.write("""
        - TensorFlow
        - PyTorch
        - Scikit-learn
        - OpenCV
        """)
        
    with skills_col2:
        st.markdown("### 📊 Data Science")
        st.write("""
        - Pandas
        - NumPy
        - SQL
        - Tableau
        """)
        
    with skills_col3:
        st.markdown("### 🛠 Development")
        st.write("""
        - Python
        - Java
        - Docker
        - Git/GitHub
        """)
    
    # --- Projects & Achievements ---
    st.markdown("## 🏆 Notable Projects & Achievements")
    with st.expander("SIH Finalist"):
        st.write("""
        **Finalist of Smart India Hackathon**
        - Developed novel hybrid model using Unet 
        - Achieved 98% accuracy
        """)
        img_path = "Images/Image02.jpg"  # Assuming images folder is in the same directory
        profile_img2 = load_image(img_path)
        if profile_img2:
            st.image(profile_img2, width=300, caption="SIH")

    with st.expander("Community Leader"):
        st.write("""
        **GDG On campus Dronacharya Group of Insitution**
        - Lead for communiy 2024-25
        - Responsible for orchestrating events
        """)
        img_path = "Images/Image03.jpg"  # Assuming images folder is in the same directory
        profile_img = load_image(img_path)
        if profile_img2:
            st.image(profile_img2, width=300, caption="Community image")
    
    # --- Footer ---
    st.markdown("---")
    st.markdown("""
    <style>
    .footer {
        text-align: center;
        padding: 20px;
        margin-top: 30px;
    }
    </style>
    <div class="footer">
        Made with ❤️ by Kartikeya Prasad | © 2024 All rights reserved
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
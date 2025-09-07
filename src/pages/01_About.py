import streamlit as st
from PIL import Image
import os

def load_image(image_name):
    """Universal image loader for local/cloud"""
    try:
        # Get current script location
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Path construction for Streamlit Cloud
        cloud_path = os.path.join(
            os.path.dirname(current_dir),  # Goes up from /pages to /src
            "Images",
            image_name
        )
        
        # Path for local development
        local_path = os.path.join("src", "Images", image_name)
        
        # Try both paths
        for path in [cloud_path, local_path]:
            try:
                return Image.open(path)
            except FileNotFoundError:
                continue
                
        st.error(f"Image '{image_name}' not found in: {cloud_path} | {local_path}")
        return None
        
    except Exception as e:
        st.error(f"Image loading error: {str(e)}")
        return None
    
def main():
    st.set_page_config(
        page_title="Aryan Pradhan - Portfolio",
        page_icon="🎓",
        layout="wide"
    )
    
    # content
    # --- Header Section ---
    col1, col2 = st.columns([1, 2])
    with col1:
        profile_img = load_image("image1.jpg")
        if profile_img:
            st.image(profile_img, width=250, caption="Profile Picture")
    with col2:
        st.title("Aryan Pradhan")
        st.header("CSE-AI/ML Undergraduate Student")
        st.write("🔗 [LinkedIn](https://www.linkedin.com/in/aryanp25/) | 💻 [GitHub](https://github.com/aryan25s) | 📧 aruupradhan2025@gmail.com")
        st.markdown("---")
            
    st.markdown("## 🎓 Education & Qualifications")
    
    edu_col1, edu_col2 = st.columns(2)
    
    with edu_col1:
        st.subheader("B.Tech in Computer Science and Engineering with Artificial Intelligence & Machine Learning")
        st.caption("Dronacharya Group of Institutions | 2022-2026 (Expected)")
        
    st.markdown("## 💻 Technical Skills")


    skills_col1, skills_col2, skills_col3 = st.columns(3)

    with skills_col1:
        st.markdown("### 🤖 AI & Machine Learning")
        st.markdown("""
        - Large Language Models (LLMs)  
        - Gemini API  
        - AI Tools (Content Generation, SEO Optimization)  
        - Sentiment & Data Trend Analysis  
        """)

    with skills_col2:
        st.markdown("### 📊 Data Science & Analysis")
        st.markdown("""
        - Pandas (Basic)  
        - NumPy (Basic)  
        - Data Preprocessing & Visualization  
        - Beginner-level Data Analysis  
        """)

    with skills_col3:
        st.markdown("### 🛠 Development & Tools")
        st.markdown("""
        - Swift (Intermediate), C++, C, Python (Basic)  
        - iOS App Development (Storyboard & SwiftUI)  
        - Firebase (Integration, Offline-first Design, Network Monitoring)  
        - Git & GitHub, Xcode, VS Code  
        """)
    
    
        
    
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
        Made with ❤️ by Aryan Pradhan | © 2025 All rights reserved
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
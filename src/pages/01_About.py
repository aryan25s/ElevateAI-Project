import streamlit as st

def main():
    # Page config MUST be first command
    st.set_page_config(
        page_title="About Elevate.AI",
        page_icon="🎈"
    )
    
    # Your content
    st.title("About me")
    st.header("Hello Everyone,I'm Kartkeya Prasad")
    st. write(
        """
     I'm currently purusing my undergraduation in artifical intelligence and machine learning.
"""
    )


# REQUIRED: This makes the page work
if __name__ == "__main__":
    main()
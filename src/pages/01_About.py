import streamlit as st

def main():
    # Page config MUST be first command
    st.set_page_config(
        page_title="About Elevate.AI",
        page_icon="🎈"
    )
    
    # Your content
    st.title("Elevate.AI")
    st.header("Elevating businesses by leveraging LLMs")


# REQUIRED: This makes the page work
if __name__ == "__main__":
    main()
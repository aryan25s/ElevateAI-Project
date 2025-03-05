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
    
    # CSS with relative path
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    local_css("D:/NewElevate.ai/Newelevateai/src/styles/style.css")  # Not absolute path!
    
    # Animation
    animation_symbol = "❄"
    st.markdown(
        f"""
        <div class="snowflake">{animation_symbol}</div>
        """,
        unsafe_allow_html=True,
    )

# REQUIRED: This makes the page work
if __name__ == "__main__":
    main()
#import required libraries
import streamlit as st
#Main page 

about_Page = st.Page(
    page="D:/NewElevate.ai/Newelevateai/src/About.py", 
    title="About",
    icon="🎈",
    default=True
)
about_ai_data_page = st.Page(
    page ="D:/NewElevate.ai/Newelevateai/src/AiDataScitenist.py",
    title="AI Data Scientist Agent",
    icon="🤖",
)
about_ai_blog_page=st.Page(
    page="D:/NewElevate.ai/Newelevateai/src/AIBlog.py",
    title ="👨‍🎓 AI Blog Generator",
    icon ="👨‍🎓"
)
about_ai_seoassistant_page = st.Page(
    page="D:/NewElevate.ai/Newelevateai/src/AISEOAssistant.py",
    title="AI SEO Assistant",
    icon="👨🏻‍💼"
)

about_ai_sentiment_page= st.Page(
    page="D:/NewElevate.ai/Newelevateai/src/aicustomerfeedback.py",
    title="Feedback Generation",
    icon="🤷‍♂️"
)

#naviagtion stepup 
pg =st.navigation({
    "INFO":[about_Page],
    "AI TOOLS":[about_ai_data_page,about_ai_blog_page,about_ai_seoassistant_page,about_ai_sentiment_page],
})
pg.run()



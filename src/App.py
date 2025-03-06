#import required libraries
import streamlit as st
#Main page 

def main():
    st.set_page_config(page_title="Elevate.AI", page_icon="🎈")
    st.title(" 🎢 Elevate.AI")
    st.header("Elevating businesses by leveraging LLMs")
    st.write("Elevate.AI leverages LLM to support small startup and student innovation hub"             """
     Join us for this amazing journey
     Elevate.AI leverages Gemini Api to provide you quick responses and this is just a visison as of now. we are working to improve this application
     day by day""")
    st.markdown("## 🚀 How Elevate.AI Transforms Your Journey")
    with st.expander("1. **AI Data Scientist Agent**"):
     st.write("""
       **Small Businesses:**
     - Cost-Effective Insights: Replace expensive data analysts with AI-driven analytics to uncover trends in sales, customer behavior, or operational efficiency.
     - Predictive Modeling: Forecast demand, optimize inventory, and reduce waste using automated machine learning.
              
       **Student Startups:**
     - Validate Ideas: Test hypotheses with data-driven validation (e.g., market size, pricing strategies).
     - No-Code Analytics: Build models without coding—perfect for non-technical founders.""")
    
    with st.expander("## 2. **AI Blog Generator**"):
        st.write("""
        **Small Businesses:**
      - Content at Scale: Generate SEO-friendly blogs, product descriptions, or social media posts in minutes.
      - Brand Voice Consistency: Maintain a professional online presence effortlessly.
                 
        **Student Startups:**
      - Pitch Perfect: Create compelling content for crowdfunding campaigns, investor pitches, or MVP launches.
      - Time-Saving: Focus on building your product while AI handles content creation.
""")
    with st.expander("## 3. **AI SEO Assistant**"):
       st.write("""
       **Small Businesses:**
      - Rank Higher, Faster: Optimize website content with keyword suggestions, meta-tags, and competitor analysis.
                
       **Student Startups:**
      - Budget-Friendly: Avoid costly SEO agencies—let AI do the heavy lifting.
""")
    with st.expander("## 4. **Sentiment Analysis (Customer Feedback)** "):
       st.write("""
       **Small Businesses:**
      - Real-Time Feedback: Analyze reviews, surveys, or social media to gauge customer satisfaction.
      - Improve Retention: Identify pain points and address them proactively.
       
        **Student Startups:**
      - Validate Product-Market Fit: Understand early user reactions to refine your MVP.
      - Build Loyalty: Respond to feedback quickly to foster trust and community.
""")
       
    st.caption("**Start Elevating Today 🌟**")

if __name__ == "__main__":
    main()


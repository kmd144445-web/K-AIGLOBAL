import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="K-AI", layout="wide")
st.title("🤖 K-AI")
st.markdown("### নির্মাতা ও মালিক: খোরশেদ আলম স্যার")

# আপনার API Key
genai.configure(api_key="AIzaSyDSyAP-S6whAKFCIi1AWQ7C8XuBjitYXfE")

# এটি অটোমেটিক মডেল খুঁজে নিবে
model = genai.GenerativeModel('gemini-pro') 

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("নির্দেশ দিন, খোরশেদ আলম স্যার..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # Gemini 3 এর মতো বুদ্ধিমান উত্তর দিতে মালিকের নাম মনে করিয়ে দেওয়া
            response = model.generate_content(f"তোমার নাম K-AI। মালিক খোরশেদ আলম স্যার। তাকে শ্রদ্ধা করে উত্তর দাও: {prompt}")
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error("গুগল সার্ভার কানেকশন নিচ্ছে না। অনুগ্রহ করে কিছুক্ষণ পর চেষ্টা করুন।")
            

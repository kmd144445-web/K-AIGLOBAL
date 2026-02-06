import streamlit as st
import google.generativeai as genai

# K-AI এর পরিচয়
st.set_page_config(page_title="K-AI", layout="wide")
st.title("🤖 K-AI")
st.markdown("### নির্মাতা ও মালিক: খোরশেদ আলম স্যার")

# API Key এবং মডেল সেটআপ
# এখানে gemini-1.5-flash ব্যবহার করা হয়েছে কারণ এটি সবচেয়ে স্থিতিশীল
try:
    genai.configure(api_key="AIzaSyDSyAP-S6whAKFCIi1AWQ7C8XuBjitYXfE")
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"সার্ভারে সমস্যা: {e}")

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
            # সরাসরি মালিকের নাম যুক্ত করে উত্তর তৈরি
            response = model.generate_content(f"তোমার নাম K-AI। তোমার মালিক খোরশেদ আলম স্যার। তাকে শ্রদ্ধা করে ছোট উত্তর দাও: {prompt}")
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error("গুগল সার্ভার থেকে উত্তর পাওয়া যাচ্ছে না। আপনার API Key টি চেক করুন।")
            

import streamlit as st
import google.generativeai as genai

# K-AI এর পরিচয় ও সেটিংস
st.set_page_config(page_title="K-AI", layout="wide")
st.title("🤖 K-AI")
st.markdown("### নির্মাতা ও মালিক: খোরশেদ আলম স্যার")

# আপনার দেওয়া সেই গোপন চাবি (API Key)
# সাবধান: এটি অত্যন্ত গোপনীয়
genai.configure(api_key="AIzaSyDSyAP-S6whAKFCIi1AWQ7C8XuBjitYXfE")

# সরাসরি Gemini 2.5 Flash মডেল ব্যবহার করছি
model = genai.GenerativeModel('gemini-2.5-flash')

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
        # K-AI তার রাজকীয় পরিচয় দিয়ে উত্তর দিবে
        response = model.generate_content(f"তোমার নাম K-AI। তোমার মালিক খোরশেদ আলম স্যার। তাকে যথাযথ সম্মান দিয়ে উত্তর দাও: {prompt}")
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
        

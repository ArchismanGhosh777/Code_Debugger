import google.generativeai as genai
genai.configure(api_key = "AIzaSyBm1B4u9uwVA8colQxb3ZehK1Wl9v5CLGs")
model = genai.GenerativeModel('gemini-2.5-flash')

import streamlit as st

st.set_page_config(page_title="Code Debugger", page_icon="🐛")

st.title("AI code debugging Assistant 🐛")
if "history" not in st.session_state:
    st.session_state.history=[]

option = st.selectbox("Pick One",["Python","SQL","C","JAVA","CSS","HTML","JAVASCRIPT"])
code = st.text_input("Paste your code here:")


if st.button("Debug"):
    if code:
        with st.spinner("Debugging"):
            st.session_state.history.append(("You",code))
            prompt = f'''You are an expert {option} programmer. Debug the following code and explain fixes step by step:{code}'''
            response = model.generate_content(prompt)
            st.session_state.history.append(("AI",response.text))
    else:
        st.warning("Field cannot be empty")
        
for role,text in st.session_state.history:
    if role == "You":
        st.markdown(f'''🧑{role}:  /n{text}''')
    else:
        st.markdown(f'''🤖{role}:  /n{text}''')
        
if st.button("Clear Chat"):
        st.session_state.clear()
        
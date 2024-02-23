import streamlit as st

st.header("Contact Me")

with st.form(key="email_forms"):
    user_mail = st.text_input("your email address")
    message = st.text_area("your message")
    button = st.form_submit_button("Submit")
    if button:
        message = message + user_mail
        
        print(button)
        print(" I was pressed")

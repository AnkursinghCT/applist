import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_forms"):
    user_mail = st.text_input("your email address")
    message = st.text_area("your message")
    message = message + "\n" + user_mail
    button = st.form_submit_button("Submit")
    print(button)
    if button:
        send_email(message)
        


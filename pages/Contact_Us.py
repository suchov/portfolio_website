import streamlit as st
from send_email import send_email
import pandas

df = pandas.read_csv("topics.csv")

st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    user_topic = st.selectbox("What topic do you want to discuss?",
                              df["topic"])
    message = st.text_area("Your message here")
    message = message = "\n" + user_email + user_topic
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("The message was sent")

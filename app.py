import streamlit as st
import joblib
model=joblib.load("spam_detector.pkl")
st.title("SPAM DETECTOR")
st.write("Check if a message is a spam")
user_input=st.text_area("Write the message here: ")
if st.button("Analyze"):
    if user_input.strip()=="":
        st.warning("Please enter a valid message")
    else:
        prediction = model.predict([user_input])[0]

    if prediction==1:
        st.error("This is a SPAM !!!")
    else:
        st.success('Not a SPAMM')



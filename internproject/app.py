import streamlit as st
import pickle

# Load model and vectorizer
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# App title
st.title("📩 SMS Spam Detection App")

# Input message
input_sms = st.text_area("Enter the message:")

if st.button('Predict'):
    # Preprocessing
    transformed_sms = vectorizer.transform([input_sms])
    
    # Prediction
    result = model.predict(transformed_sms)[0]
    
    # Output
    if result == 1:
        st.error("🚫 This is a Spam Message!")
    else:
        st.success("✅ This is a Ham (Safe) Message!")

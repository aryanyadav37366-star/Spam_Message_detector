import streamlit as st
import pickle

# Load model
model = pickle.load(open("model.pkl","rb"))
cv = pickle.load(open("vectorizer.pkl","rb"))

st.title("Spam Email Detection")

st.write("Name: Aryan Yadav")
st.write("SPN: 2403106")

msg = st.text_area("Enter Message")

if st.button("Predict"):
    data = cv.transform([msg])
    result = model.predict(data)

    if result[0] == 1:
        st.error("Spam Message")
    else:
        st.success("Not Spam")
from google import genai
import streamlit as st

client = genai.Client(api_key="AQ.Ab8RN6LW1gHnYc0H6fpMOwITd503Hk5DibaXSHeEqKk0EvrMpw")

st.title("Talk to Agent")
st.write("This app demonstrates a conversational agent.")

user_input = st.text_input("Ask a question:")

if st.button("Submit"):
    with st.spinner("Agent is thinking..."):
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=user_input
        )

    st.write(response.text)
from dotenv import load_dotenv
load_dotenv()

import os
import streamlit as st
from PIL import Image
import google.generativeai as genai

# Configure API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


model = genai.GenerativeModel('gemini-1.5-flash')

def model_response(input_prompt, image, input_text):
    if image is not None:
        
        result = model.generate_content([input_prompt, image, input_text])
    else:
        
        result = model.generate_content([input_prompt, input_text])
    return result.text


prompt = """
You are an expert nutritionist tasked with analyzing food items from an image to calculate the total calories. Additionally, you should provide details of every food item with its calorie intake in the following format:

1. Item 1 - number of calories
2. Item 2 - number of calories
----
----

If no image is given, respond to the user's query with an estimated answer. For example, if a user asks about the calories in 1/2 kg of boiled chicken, provide an estimated calorie count.

If a user asks about the calorie count for a particular item shown in the image, calculate and provide the calorie content for that specific item.
"""


# Streamlit page config
st.set_page_config(page_title="Calorie Tracker")

st.header("Health Monitoring App")

input_text = st.text_input("Ask me...")

uploaded_file = st.file_uploader("Choose an Image...", type=['jpg', 'jpeg', 'png'])

submit = st.button("Enter")

if submit:
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width = True)
        response = model_response(prompt, image, input_text)
        st.write(response)
    elif input_text:
        response = model_response(prompt, None, input_text)
        st.write(response)
    else:
        st.write("Please upload an image or enter a query.")

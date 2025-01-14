# Health Monitoring App

## Overview
This Streamlit-based Health Monitoring App leverages the power of Google's generative AI to analyze food items either from text queries or directly from images to estimate calorie content. It's designed to assist users in tracking their calorie intake conveniently by using advanced image recognition and natural language processing technologies.

## Features
- **Image Analysis**: Users can upload images of food items, and the app will analyze these images to identify food items and estimate their calorie content.
- **Text Query**: Users can also enter text queries about specific food items to receive calorie estimates without the need for images.
- **Interactive UI**: The app offers a user-friendly interface where users can easily upload images, enter queries, and receive responses directly on the web page.

## How It Works
The application uses the `gemini-1.5-flash` model from Google's generative AI to process both image data and text input. Here's a breakdown of its functionality:

1. **Load Environment and Libraries**:
    - The application starts by loading necessary Python libraries and environment variables, including the API key for accessing the generative AI model.

2. **Model Configuration**:
    - It configures the `genai` library with the API key to authenticate and use the Gemini model.

3. **Image and Text Processing**:
    - If an image is uploaded, the app displays the image and sends it along with any accompanying text to the Gemini model.
    - The model processes the input to identify food items in the image and calculate their calorie content.
    - If no image is uploaded, the app simply sends the text query to the model to get an estimated calorie count based on the description provided.

4. **User Interface**:
    - Users interact with the app through a simple interface where they can upload images, type queries, and view responses.
    - The interface is built using Streamlit, which facilitates rapid web application development with Python.

## Usage
To use the app:
1. Navigate to the web page.
2. Use the text input box to ask about calorie content of specific foods.
3. Optionally, upload an image of food items.
4. Click "Enter" to submit your query or image.
5. View the calorie estimates and details displayed on the page.

## Installation
To run this app locally, you'll need Python installed along with Streamlit and the necessary libraries mentioned in the script. Clone the repository and install dependencies:



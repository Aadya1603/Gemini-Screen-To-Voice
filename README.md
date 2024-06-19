# Gemini-Screen-To-Voice

A web-based application that uses Google Generative AI to analyze screenshots taken from the user's screen. The application allows the user to start and stop the screenshot analysis process  Users can input their Google API key for authentication.

## Prerequisites

- Python 3.x
- Flask
- PIL (Pillow)
- pyttsx3
- google-generativeai
- keyboard

## Usage
Start the Flask server:
```
python app.py
```
Open your web browser and navigate to http://localhost:8000.

Enter your Google API key in the provided input field.

Click "Start Application" to begin the screenshot analysis process.

Use "Ctrl + Space" to take screenshots and have them analyzed by the application.

Click "Stop Application" to stop the screenshot analysis process.

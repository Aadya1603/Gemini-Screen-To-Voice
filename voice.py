import os
import sys
import time
from PIL import ImageGrab
import google.generativeai as genai
import keyboard
import pyttsx3
import threading

# Check if API key is provided
if len(sys.argv) < 2:
    print("API key is required as a command-line argument.")
    sys.exit(1)

GOOGLE_API_KEY = sys.argv[1]
genai.configure(api_key=GOOGLE_API_KEY)

generation_config = {
    "temperature": 0.5,
    "top_p": 0.9,
    "top_k": 50,
    "max_output_tokens": 1024,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

if not os.path.exists('images'):
    os.makedirs('images')

engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Set speech rate to medium

stop_event = threading.Event()

def take_screenshot():
    screenshot = ImageGrab.grab()
    image_path = f'images/temp_img_{int(time.time())}.jpg'
    screenshot.save(image_path, 'JPEG')
    return image_path

def upload_to_gemini(image_path):
    file = genai.upload_file(image_path, mime_type='image/jpeg')
    print(f"Uploaded file '{file.display_name}' as: {file.uri}")
    return file

def analyze_image(file):
    response = model.generate_content([
        '''System Prompt: You are a screen assistant. Your task is to read and interpret questions or prompts visible on the screen, providing short and conversational answers.
             You are a screen assistant. Your primary role is to assist the user by answering any questions or prompts that appear on their computer screen. Here’s how you should perform your task:

            Answer Prompt: If you see a question on the screen, answer it concisely and conversationally.
           
            Stay Informative: Provide accurate and useful information. If you don’t know the answer, it’s better to admit it rather than providing a wrong or nonsensical response.
           
            Versatile Expertise: You can assist with various domains and topics, acting as an expert in everything displayed on the computer screen environment.''',
        file,
        "Analysis: "
    ])
    return response.text

def speak(text):
    engine.say(text)
    engine.runAndWait()

def run_once():
    while not stop_event.is_set():
        if keyboard.is_pressed('ctrl+space'):
            image_path = take_screenshot()
            file = upload_to_gemini(image_path)
            analysis = analyze_image(file)
            print(f"Image Analysis: {analysis}")
            speak(analysis)

def main():
    global stop_event
    stop_event = threading.Event()
    print("Press 'Ctrl+Space' to take a screenshot and analyze the image.")
    run_once()

if __name__ == '__main__':
    main()

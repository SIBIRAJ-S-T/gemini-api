from fastapi import FastAPI
import google.generativeai as genai
import uvicorn
import os

# Get API Key from Render Environment Variable
API_KEY = os.getenv("AIzaSyCmrNE8Mb4U4xRWJzXG2rXzoU6W7SoWAwE")  # Ensure this matches your Render ENV variable

# Configure Gemini AI with API Key
if API_KEY:
    genai.configure(api_key=API_KEY)
else:
    raise ValueError("API Key is missing. Set GEMINI_API_KEY in Render environment variables.")

# Use a valid Gemini model
MODEL_NAME = "models/gemini-1.5-pro"  # Change if needed

app = FastAPI()

@app.get("/generate/")
def generate_code(prompt: str):
    try:
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(prompt)
        return {"generated_code": response.text}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

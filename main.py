from fastapi import FastAPI
import google.generativeai as genai
import os
import uvicorn

app = FastAPI()

# Configure Gemini AI with API Key from Environment Variables
API_KEY = os.getenv("AIzaSyCmrNE8Mb4U4xRWJzXG2rXzoU6W7SoWAwE")  # Set this in Render Dashboard
genai.configure(api_key=API_KEY)

@app.get("/generate/")
def generate_code(prompt: str):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")  # Use a valid model
        response = model.generate_content(prompt)
        return {"generated_code": response.text}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

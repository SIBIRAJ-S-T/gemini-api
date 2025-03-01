from fastapi import FastAPI
import google.generativeai as genai
import uvicorn
import os

# Configure Gemini AI with API Key from Render Environment Variable
API_KEY = os.getenv("AIzaSyCmrNE8Mb4U4xRWJzXG2rXzoU6W7SoWAwE")
genai.configure(api_key=API_KEY)

app = FastAPI()

@app.get("/generate/")
def generate_code(prompt: str):
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        return {"generated_code": response.text}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

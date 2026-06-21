from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from google import genai
from PIL import Image
import io
import os
import json

load_dotenv()

app = FastAPI(title="AI Product Analyzer")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

@app.get("/")
def home():
    return {
        "status": "running",
        "message": "AI Product Analyzer API"
    }

@app.post("/analyze")
async def analyze(image: UploadFile = File(...)):

    image_bytes = await image.read()
    pil_image = Image.open(io.BytesIO(image_bytes))

    prompt = """
    Analyze this product image.

    Return ONLY valid JSON:

    {
      "category":"",
      "description":"",
      "tags":[]
    }
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[prompt, pil_image]
    )

    cleaned = (
        response.text
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    return json.loads(cleaned)
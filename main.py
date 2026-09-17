import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="AI Video Generator API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class VideoRequest(BaseModel):
    prompt: str

@app.post("/api/generate-video")
async def generate_video(request: VideoRequest):
    try:
        return {
            "status": "success",
            "message": "Video generado correctamente",
            "video_url": "https://assets.mixkit.co/videos/preview/mixkit-tree-in-the-field-1197-large.mp4"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

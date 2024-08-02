from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List, Dict, Any

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

def process_data(data: List[str]):
    data = data['data']
    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]
    highest_alphabet = [max(alphabets, key=lambda s: s.lower())] if alphabets else []
    return numbers, alphabets, highest_alphabet

@app.post("/bfhl")
async def handle_post(data_request: Request):
    try:
        numbers, alphabets, highest_alphabet = process_data(await data_request.json())
        response = {
            "is_success": True,
            "user_id": "john_doe_17091999",
            "email": "john@xyz.com",
            "roll_number": "ABCD1234",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": highest_alphabet
        }
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/bfhl")
def handle_get():
    return {"operation_code": 1}

app.mount("/", StaticFiles(directory="frontend/build", html=True), name="static")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

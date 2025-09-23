from pathlib import Path
import shutil

from fastapi.responses import FileResponse
from fastapi import FastAPI, File, UploadFile, HTTPException, status

app = FastAPI()

@app.post("/uplaodfile")
async def upload_file(file: UploadFile = File(...)):

    with open(
        f"uploads/{file.filename}", "wb"
    ) as buffer:
        shutil.copyfileobj(file.file , buffer)

    return{
        "Uploaded File Name": file.filename 
    }

@app.get("/downloadfile/{filename}", response_class= FileResponse)
async def download_file(
    filename: str
):
    if not Path(f"uploads/{filename}").exists():
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND
        )
    
    return FileResponse(
        path= f"uploads/{filename}", filename= filename
    )
    
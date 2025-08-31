import json
from fastapi import FastAPI, HTTPException, status, Request
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.exceptions import RequestValidationError
import books
import author

app = FastAPI()

app.include_router(books.router)
app.include_router(author.router)

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code = exc.status_code, 
        content={
            "message": "Oops! Something went wrong"
        }
    )




@app.get("/error_endpoint")
async def raise_exception():
    raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST)



@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):
    return PlainTextResponse(
        "This is plain text response"
        f" \n{json.dumps(exc.errors(), indent=2)}",
        status_code = status.HTTP_400_BAD_REQUEST
        
        )
from fastapi import FastAPI
import books
import author

app = FastAPI()

app.include_router(books.router)
app.include_router(author.router)





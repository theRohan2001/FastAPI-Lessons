from fastapi import APIRouter
from models.book import Book, BookResponse

router = APIRouter()

#path paratemer
@router.get("/books/{book_id}")
async def read_book(book_id: int):
    return{
        "book_id": book_id,
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien"
    }

#Query parameter
@router.get("/books")
async def read_books(year: int | None = None):
    if year:
        return{
            "year": year,
            "books": {"book1", "book2"}
        }
    return {"books": ["All Books"]}

# create a book using pydantic model
@router.post("/book")
async def create_book(book: Book):
    return book


@router.get("/allbooks", response_model=list[BookResponse])
async def read_all_books():
    return[
            {
                "title" : "1984", 
                "author" : "George Orwell",
                "year" : 1923

            },
            {
                "title" : "LOR", 
                "author" : "J.R.R. Tolkien", 
                "year" : 1923
                
            }
        ]
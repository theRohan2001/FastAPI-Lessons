from fastapi import APIRouter

router = APIRouter()


@router.get("/books/{book_id}")
async def read_book(book_id: int):
    return{
        "book_id": book_id,
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien"
    }

@router.get("/books")
async def read_books(year: int | None = None):
    if year:
        return{
            "year": year,
            "books": {"book1", "book2"}
        }
    return {"books": ["All Books"]}
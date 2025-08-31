from fastapi import APIRouter

router = APIRouter()

@router.get("/author/{author_id}")
async def read_author(author_id: int):
    return{
        "author_id": author_id,
        "name": "Manu S. Pillai"
    }

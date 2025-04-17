from fastapi import APIRouter, Depends, HTTPException, Query, Request
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from database.models import MovieModel
from schemas.movies import MovieDetailResponseSchema, MovieListResponseSchema
from database import get_db

router = APIRouter()

# Write your code here
@router.get("/movies/{movie_id}/", response_model=MovieDetailResponseSchema)
async def get_movies(movie_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(MovieModel).where(MovieModel.id == movie_id))
    movie = result.scalar_one_or_none()
    if not movie:
        raise HTTPException(status_code=404, detail="Movie with the given ID was not found.")
    return movie

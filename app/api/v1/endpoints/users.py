from typing import Any, List

from fastapi import APIRouter, HTTPException

from app.schemas.user import User, UserCreate, UserUpdate

router = APIRouter()

@router.get("/", response_model=List[User])
def read_users() -> Any:
    """
    Retrieve users.
    """
    # This would typically interact with a database
    return [{"id": 1, "email": "user@example.com", "is_active": True}]

@router.post("/", response_model=User)
def create_user(user: UserCreate) -> Any:
    """
    Create new user.
    """
    # This would typically interact with a database
    return {"id": 2, "email": user.email, "is_active": True}

@router.get("/{user_id}", response_model=User)
def read_user(user_id: int) -> Any:
    """
    Get user by ID.
    """
    # This would typically interact with a database
    return {"id": user_id, "email": f"user{user_id}@example.com", "is_active": True}
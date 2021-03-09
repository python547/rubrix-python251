from fastapi import APIRouter, Depends
from rubric.server.security.api import get_current_active_user

from .model import User

router = APIRouter(tags=["users"])


@router.get(
    "/me",
    response_model=User,
    operation_id="whoami",
)
async def whoami(current_user: User = Depends(get_current_active_user)):
    """
    User info endpoint

    Parameters
    ----------
    current_user:
        The current request user

    Returns
    -------
        The current user

    """
    return current_user

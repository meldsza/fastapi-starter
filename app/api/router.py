from fastapi.routing import APIRouter
import app.models as models
from typing import List
from app.util.list_files import list_files as list_files_utility

api_router = APIRouter()

# Get list of all files in files directory
@api_router.get('/files', response_model=List[models.File])
def list_files():
    file_list = list_files_utility()
    return file_list

# TODO: Write an API route to retrieve a particular file and stream it
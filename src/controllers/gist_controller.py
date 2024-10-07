from src.controllers.exceptions.gist_exceptions import GistControllerException
from src.controllers.models.create_gist import Gist, GistResponse
from src.services.gist_service import GistService
from fastapi import APIRouter, HTTPException


router = APIRouter()

@router.post("/gist/", response_model=GistResponse)
async def create_gist(gist: Gist):
    """
    Retorna url referente ao Gist criado.
    - **city**: Nome da cidade.
    - **country**: Sigla do pais, exemplo Brasil -> br
    """
    if not gist.city or gist.city == "":
        raise HTTPException(status_code=400, detail="O campo 'city' não pode estar vazio.")
    if not gist.country or gist.country == "":
        raise HTTPException(status_code=400, detail="O campo 'country' não pode estar vazio.")
    try:
        gist_service = GistService()
        url = gist_service.create_new_gist(gist.city,gist.country)
        return {"url":url}
    except Exception as e:
        raise GistControllerException(e)
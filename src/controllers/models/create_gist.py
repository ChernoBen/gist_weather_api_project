from pydantic import BaseModel

class Gist(BaseModel):
    city:str
    country:str

class GistResponse(BaseModel):
    url:str

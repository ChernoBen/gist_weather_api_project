from src.adapters.exceptions.pygithub_exceptions import PyGitHubException
from src.adapters.exceptions.weather_exceptions import WeatherException
from src.utils.logging import log_error
from fastapi import HTTPException


class GistControllerException:
    def __init__(self, exception):
        if isinstance(exception,PyGitHubException):
            raise HTTPException(status_code=400,detail="Erro ao processar a solicitação ao github.")
        elif isinstance(exception,WeatherException):
            raise HTTPException(status_code=400,detail="Erro ao processar a solicitação ao servico de clima.")
        else:
            log_error(exception)
            raise HTTPException(status_code=422,detail="Erro ao processar a solicitação. Verifique os dados fornecidos.")
from src.adapters.exceptions.pygithub_exceptions import PyGitHubException
from src.utils.envs import EnvironmentConfig as envs
from github import Github


class PyGitHubAdapter:
    def __init__(self,access_token:str):
        try:
            self.gitHub = Github(access_token)
            self.gist_id = envs.get("GIST_ID")
        except Exception as e:
            raise PyGitHubException(e)
        
    def add_comment_to_gist(self,comment: str) -> str:
        """
        Adiciona um comentário a um gist existente.
        :param comment: O texto do comentário a ser adicionado.
        :raises PyGitHubException: Se ocorrer um erro ao adicionar o comentário.
        """
        if not comment:
            raise PyGitHubException("O comentário não pode estar vazio.")

        try:
            gist = self.gitHub.get_gist(self.gist_id)
            gist.create_comment(comment)
            return gist.html_url
        except Exception as e:
            raise PyGitHubException(f"Erro ao adicionar comentário ao gist {self.gist_id}: {e}")
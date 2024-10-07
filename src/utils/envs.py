import os
from .logging import log_error,log_info


class EnvironmentConfig:
    @staticmethod
    def get(key,default=None):
        try:
            res=os.getenv(key,default)
            return res

        except Exception as e:
            log_error(f"failed while trying to load env vars: {e}","red")
            raise e

    
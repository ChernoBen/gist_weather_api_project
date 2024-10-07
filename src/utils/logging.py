class LogColors:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'

def log_error(message):
    print(f"{LogColors.RED}[ERROR]{LogColors.RESET} {message}")

def log_info(message):
    print(f"{LogColors.GREEN}[INFO]{LogColors.RESET} {message}")

def log_warning(message):
    print(f"{LogColors.YELLOW}[WARNING]{LogColors.RESET} {message}")
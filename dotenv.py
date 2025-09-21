# Very simple parser for the .env file (We're using a .env file to make sure we're not committing secrets to git)

import os
import logging
import secrets

def load_dotenv() -> None:
    try:
        with open("./.env", "r") as f:
            for row in f:
                row = row.split("=")
                key = str(row[0])
                value = str(row[1])
                os.environ[key] = value
                
            f.close()
    except FileNotFoundError:
        logging.warning("No .env file found") # This does not currently do much since logging hasn't been implemented across the project TODO add proper logging
        if not os.getenv("SECRET"):
            _generate_dotenv() # Generating a new .env file if one doesn't exist and the "SECRET" environment variable doesn't exist
        
def _generate_dotenv() -> None:
    if os.path.exists("./.env"):
        logging.error(".env file already exists! Skipping file creation")
    else:
        logging.info("Generating a new .env file")
        with open("./.env", "w") as f:
            secret = secrets.token_hex()
            f.write(f"SECRET={secret}")
            os.environ["SECRET"] = secret # setting the SECRET variable if it doesn't exist
            f.close()
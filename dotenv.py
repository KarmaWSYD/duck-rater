# Very simple parser for the .env file (We're using a .env file to make sure we're not committing secrets to git)

import os
import logging

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
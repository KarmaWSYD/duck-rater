# Very simple parser for the .env file (We're using a .env file to make sure we're not committing secrets to git)
# Normally we could use python-dotenv, but project requirements do not allow it as a dependency. Feel free to remove this file and install python-dotenv instead, the project should be compatible with it.

import os
import secrets

def load_dotenv() -> None:
    try:
        with open("./.env", "r") as f:
            for row in f:
                if len(row) > 0 and row[0] != "#": # ignore rows with comments
                    row = row.split("=")
                    key = str(row[0])
                    value = str(row[1])
                    os.environ[key] = value
                
            f.close()
    except FileNotFoundError:
        print("WARNING: No .env file found")
        if not os.getenv("SECRET"):
            _generate_dotenv() # Generating a new .env file if one doesn't exist and the "SECRET" environment variable doesn't exist
        
def _generate_dotenv() -> None:
    if os.path.exists("./.env"):
        print("ERROR: .env file already exists! Skipping file creation")
    else:
        print("INFO: Generating a new .env file")
        with open("./.env", "w") as f:
            secret = secrets.token_hex()
            f.write(f"SECRET={secret}")
            os.environ["SECRET"] = secret # setting the SECRET variable if it doesn't exist
            f.close()
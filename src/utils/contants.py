import os
from dotenv import load_dotenv

load_dotenv()

PROJECT = os.getenv("PROJECT")


if __name__ == "__main__":
    print(PROJECT)

# import os

# BASE_DIR = os.path.dirname(__file__)

# UPLOAD_DIR = os.path.join(
#     BASE_DIR,
#     "uploads"
# )

# os.makedirs(
#     UPLOAD_DIR,
#     exist_ok=True
# )

import os
from dotenv import load_dotenv


load_dotenv()


# Directories
BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)


UPLOAD_DIR = os.path.join(
    BASE_DIR,
    "uploads"
)
os.makedirs(UPLOAD_DIR, exist_ok=True)


FAISS_DIR = os.path.join(
    BASE_DIR,
    "faiss_storage"
)


INDEX_FILE = os.path.join(
    FAISS_DIR,
    "index.faiss"
)


METADATA_FILE = os.path.join(
    FAISS_DIR,
    "metadata.pkl"
)


# Gemini
GEMINI_API_KEY = os.getenv(
    "GEMINI_API_KEY"
)
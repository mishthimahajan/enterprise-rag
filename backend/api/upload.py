import os

from fastapi import APIRouter, UploadFile, File

from config import UPLOAD_DIR

from services.parser import (
    parse_pdf,
    parse_docx,
    parse_ppt
)

from services.chunker import create_chunks

from services.embedder import create_embeddings

from db.store import add_documents


router = APIRouter()


@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...)
):

    # Save file
    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )
    import os

    os.makedirs(UPLOAD_DIR, exist_ok=True)

    file_path = os.path.join(
    UPLOAD_DIR,
    file.filename
    )

    with open(file_path, "wb") as f:

        f.write(
            await file.read()
        )


    # Detect type
    extension = file.filename.split(".")[-1].lower()


    if extension == "pdf":

        text = parse_pdf(
            file_path
        )


    elif extension == "docx":

        text = parse_docx(
            file_path
        )


    elif extension == "pptx":

        text = parse_ppt(
            file_path
        )


    else:

        return {
            "error": "Unsupported file type"
        }


    print("\n===== DOCUMENT TEXT =====")
    print(text[:500])


    # Create chunks
    chunks = create_chunks(
        text
    )


    print(
        "Total chunks:",
        len(chunks)
    )


    # Create embeddings
    embeddings = create_embeddings(
        chunks
    )


    print(
        "Embedding count:",
        len(embeddings)
    )


    # Store into FAISS
    add_documents(
        chunks,
        embeddings,
        file.filename
    )


    return {

        "status": "success",

        "filename": file.filename,

        "characters": len(text),

        "chunks": len(chunks),

        "message": "Document indexed in FAISS successfully"

    }



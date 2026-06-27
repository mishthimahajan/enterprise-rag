# from langchain_text_splitters import RecursiveCharacterTextSplitter


# def create_chunks(text):

#     splitter = RecursiveCharacterTextSplitter(
#         chunk_size=1000,
#         chunk_overlap=200
#     )

#     return splitter.split_text(text)

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)


def create_chunks(text: str):

    splitter = (
        RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " "
            ]
        )
    )


    chunks = splitter.split_text(
        text
    )


    return [
        chunk.strip()
        for chunk in chunks
        if chunk.strip()
    ]
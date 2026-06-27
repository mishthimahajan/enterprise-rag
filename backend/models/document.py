from dataclasses import dataclass


@dataclass
class DocumentChunk:

    id: int

    filename: str

    page: int

    text: str
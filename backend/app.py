# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

# from api.upload import router as upload_router
# from api.query import router as query_router

# app = FastAPI(
#     title="Enterprise RAG Assistant",
#     description="Document Q&A using RAG",
#     version="1.0.0"
# )

# # CORS Configuration
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=[
#         "http://localhost:3000",
#         "http://127.0.0.1:3000",
#     ],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Health Check
# @app.get("/")
# def root():
#     return {
#         "message": "Enterprise RAG Backend Running"
#     }

# # Register Routes
# app.include_router(upload_router)
# app.include_router(query_router)

from fastapi import FastAPI

from fastapi.middleware.cors import (
    CORSMiddleware
)

from api.upload import (
    router as upload_router
)

from api.query import (
    router as query_router
)


app = FastAPI(
    title="Enterprise RAG API"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
        "https://enterprise-rag-sepia.vercel.app/"
        "https://enterprise-q6i3qovuy-mishthimahajan0-gmailcoms-projects.vercel.app/"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    upload_router,
    prefix="/api",
    tags=["Upload"]
)


app.include_router(
    query_router,
    prefix="/api",
    tags=["Query"]
)


@app.get("/")
def home():

    return {
        "message":
        "Enterprise RAG API Running"
    }
import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from module import (
    users_module,
    groups_module,
    expenses_module
)
from db.database import *
from html_response_codes import *

app = FastAPI(title="Splitwise clone")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
async def startup():
    try:
        await database.connect()
    except Exception:
        return ErrorResponseModel(500, "Internal Server Error")


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


# routing swagger api documentation to default path
@app.get("/")
def index():
    return RedirectResponse(url="/docs")

# Attaching a dentalstall scaper router file for layered architecture, Example - can accomodate multiple router for diff scrapers
app.include_router(users_module.router, prefix="/users", tags=["User Data"])
app.include_router(groups_module.router, prefix="/groups", tags=["Group Data"])
app.include_router(expenses_module.router, prefix="/expenses", tags=["Expense Data"])

# health check for the application database, can also do it for in-memory redis db
@app.get("/health")
async def health_check():
    try:
        await database.connect()
        await database.disconnect()
        return "Ok"
    except Exception:
        return "Connection Failed!"

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port="8000")

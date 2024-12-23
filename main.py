from fastapi import FastAPI
from starlette.responses import FileResponse

app = FastAPI()

@app.get("/")
def main():
    return FileResponse("./Busan_districts.svg")
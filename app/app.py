from fastapi import FastAPI, Header, HTTPException
from typing import Union
from fastapi import FastAPI
from mangum import Mangum
from fastapi.responses import JSONResponse
import uvicorn
from typing import Union

app = FastAPI()
handler = Mangum(app)

@app.get("/")
def read_root():
    return {"message": "This is a public endpoint"}

@app.get("/profile")
def read_profile(x_username: str = Header(None)):
    if not x_username:
        raise HTTPException(status_code=400, detail="x-username header not found")
    return {"username": x_username}


if __name__ == "__main__":
   uvicorn.run(app, host="0.0.0.0", port=8080)

# myapp/main.py
from typing import Optional
from website import app
import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", port=8001, reload=True)

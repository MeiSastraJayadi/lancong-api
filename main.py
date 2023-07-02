from dotenv import load_dotenv
from fastapi import FastAPI
import os

app = FastAPI()
load_dotenv()

@app.get("/")
def hello() : 
    return "Hello World"

url = os.getenv('DATABASE_URL')
print(url)


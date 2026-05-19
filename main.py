from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Self-Healing CI/CD Backend Running"}
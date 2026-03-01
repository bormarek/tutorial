from fastapi import FastAPI

app = FastAPI(title="My App", version="1.0.0")

@app.get("/")
def root():
    return {"message": "Hello from Docker!", "status": "ok"}

@app.get("/health")
def health():
    return {"status": "healthy"}

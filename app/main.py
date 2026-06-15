from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API Running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/products")
def products():
    return [
        {"id": 1, "name": "Laptop"},
        {"id": 2, "name": "Phone"}
    ]


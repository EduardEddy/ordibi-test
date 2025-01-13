from fastapi import FastAPI

app = FastAPI()

__all__ = ["app"]

# Inicializar configuraciones globales si es necesario
@app.get("/")
def health_check():
    return {"status": "OK"}

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "Hola, mi nombre es" : "Angel Morales",
        "Y esta es la solucion de la prueba, agradezco mucho la oportunidad, gracias por tener en cuenta mi perfil y espero poder ser parte de Smart Talent",
        "Saludos cordiales, estare atento a su respuesta"
    }

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

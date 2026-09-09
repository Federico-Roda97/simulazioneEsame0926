# pip install fastapi uvicorn
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
import uvicorn

from db import fetchall

app = FastAPI()

@app.get("/api/ordini/{citta}")
def get_ordini_by_city(citta:str):
  result = fetchall(
    """
    SELECT *
    FROM ordini AS o
    JOIN carrello AS ca ON o.id_carrello = ca.id_carrello
    JOIN utenti AS u ON ca.id_utente = u.id_utente 
    WHERE u.citta LIKE %s
    """, [f"%{citta}%"])
  return result



app.mount("/", StaticFiles(directory="statics"), )

uvicorn.run(app, host="127.0.0.1", port=8000)

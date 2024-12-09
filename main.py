# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os
from typing import Optional

app = FastAPI()

DATA_FILE = "clients.json"

class ClientBase(BaseModel):
    name: str
    email: str
    phone: str

class ClientCreate(ClientBase):
    pass

class ClientBaseUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None

class Client(ClientBase):
    id: int

    class Config:
        orm_mode = True

def read_clients():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def write_clients(clients):
    with open(DATA_FILE, "w") as f:
        json.dump(clients, f, indent=4)

@app.post("/clients/", response_model=Client)
def create_client(client: ClientCreate):
    clients = read_clients()
    new_id = len(clients) + 1
    new_client = {**client.dict(), "id": new_id}
    clients.append(new_client)
    write_clients(clients)
    return new_client

@app.get("/clients/{client_id}", response_model=Client)
def read_client(client_id: int):
    clients = read_clients()
    for client in clients:
        if client["id"] == client_id:
            return client
    raise HTTPException(status_code=404, detail="Client not found")

@app.patch("/clients/{client_id}", response_model=Client)  # Changed to PATCH
def update_client(client_id: int, client: ClientBaseUpdate):
    clients = read_clients()
    for idx, existing_client in enumerate(clients):
        if existing_client["id"] == client_id:
            updated_client = existing_client.copy()  
            if client.name is not None:
                updated_client["name"] = client.name
            if client.email is not None:
                updated_client["email"] = client.email
            if client.phone is not None:
                updated_client["phone"] = client.phone
            clients[idx] = updated_client
            write_clients(clients)
            return updated_client
    raise HTTPException(status_code=404, detail="Client not found")

@app.delete("/clients/{client_id}")
def delete_client(client_id: int):
    clients = read_clients()
    for idx, existing_client in enumerate(clients):
        if existing_client["id"] == client_id:
            clients.pop(idx)
            write_clients(clients)
            return {"detail": "Client deleted"}
    raise HTTPException(status_code=404, detail="Client not found")

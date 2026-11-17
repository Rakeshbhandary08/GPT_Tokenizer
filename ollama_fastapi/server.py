from fastapi import FastAPI,Body;
from ollama import Client;

app=FastAPI() #server created
client=Client("http://localhost:11434")

@app.get("/")
def read_root():
    return {"Hello":"World"}

@app.get("/me")
def read_root():
    return {"Rakesh Bhandary"}


#create the endpoint for ollama
@app.post("/chat")
def chat(message:str=Body(...,embed=True,description="The message")):

    response=client.chat(model="llama3.2:1b",messages=[{"role":"user","content":message}])

    return {"response":response.message.content}

    
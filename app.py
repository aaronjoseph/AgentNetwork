from fastapi import FastAPI, Form

app = FastAPI()


@app.get("/hello")
def read_root(prompt: str = Form(...)):
    return {"message": "Hello World!"}

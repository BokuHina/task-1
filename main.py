from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI()


@app.get('/')

def read_root():
    return {"Hello": "World"}



@app.get('/helth')

def helth():
    return JSONResponse({'status':'ok'}, status_code=200)
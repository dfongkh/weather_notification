from fastapi import FastAPI
from send import send

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello" : "world"}

@app.get("/abc")
def abc_view():
    return {"Hello" : "abc"}

@app.post("/weather_notification")
def weather_notification():
    send()
    return {"Notification" : "Sent"}
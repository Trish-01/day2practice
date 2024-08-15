from fastapi import  FastAPI

app=FastAPI()

@app.get("/")
def get_user():
    return {"message": "This is your message for day 2 practice"}
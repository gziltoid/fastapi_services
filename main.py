from fastapi import FastAPI
from schemas import Phone


app = FastAPI()


@app.post('/unify_phone_from_json')
def unify_phone_from_json(phone: Phone):
    return phone.number

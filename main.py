from fastapi import FastAPI, Form, Cookie
from fastapi.responses import PlainTextResponse
from schemas import Phone


app = FastAPI()


@app.post('/unify_phone_from_json', response_class=PlainTextResponse)
def unify_phone_from_json(phone: Phone):
    return format_phone(phone.phone)


@app.post('/unify_phone_from_form', response_class=PlainTextResponse)
def unify_phone_from_form(phone: str = Form(...)):
    return format_phone(phone)


@app.get('/unify_phone_from_query', response_class=PlainTextResponse)
def unify_phone_from_query(phone: str):
    return format_phone(phone)


@app.get('/unify_phone_from_cookies', response_class=PlainTextResponse)
def unify_phone_from_cookies(phone: str = Cookie(...)):
    return format_phone(phone)


def format_phone(phone):
    phone_digits = ''.join(ch for ch in phone if ch.isdigit())

    if len(phone_digits) not in [10, 11] \
            or phone_digits[0] not in '789' \
            or phone_digits[-10] != '9':
        return phone_digits

    return '8 (9{}{}) {}{}{}-{}{}-{}{}'.format(*phone_digits[-9:])

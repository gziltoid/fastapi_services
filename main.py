from fastapi import FastAPI
from schemas import Phone


app = FastAPI()


@app.post('/unify_phone_from_json')
def unify_phone_from_json(phone: Phone):
    return format_phone(phone.phone)


def format_phone(phone):
    phone_digits = ''.join(ch for ch in phone if ch.isdigit())

    if len(phone_digits) not in [10, 11] \
            or phone_digits[0] not in '789' \
            or phone_digits[-10] != '9':
        return phone_digits

    return '8 (9{}{}) {}{}{}-{}{}-{}{}'.format(*phone_digits[-9:])

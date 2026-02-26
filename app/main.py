from fastapi import FastAPI

app = FastAPI(title='FreelanceHub API')

# app.include_router()


@app.get('/', status_code=200)
def root():
    return {'status': 'ok'}

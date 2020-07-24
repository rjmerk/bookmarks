from fastapi import FastAPI
import uvicorn

import views

app = FastAPI()
app.include_router(views.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

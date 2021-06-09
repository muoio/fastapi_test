from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def home():
	return "Đây là nhà"

@app.get("/Ti")
async def ti():
	return "Đây là Tí"

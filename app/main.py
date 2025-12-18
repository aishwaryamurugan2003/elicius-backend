from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from app.email_sender import send_email

app = FastAPI()

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/contact/")
async def contact_form(
    name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    company: str = Form(""),
    interest: str = Form(...),  
    message: str = Form(...)
):
    try:
        send_email(name, email, phone, company, interest, message)

        return {
            "status": "success",
            "message": "Your message has been sent!"
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

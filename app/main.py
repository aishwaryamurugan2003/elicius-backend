from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from app.email_sender import send_email

app = FastAPI()

# CORS settings (allows frontend → backend API calls)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to your frontend domain when deployed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/contact/")
async def contact_form(
    name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    company: str = Form(""),
    message: str = Form(...)
):
    try:
        # Call function that sends the Gmail SMTP email
        send_email(name, email, phone, company, message)

        return {
            "status": "success",
            "message": "Your message has been sent!"
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

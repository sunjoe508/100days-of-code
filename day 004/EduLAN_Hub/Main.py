from fastapi import FastAPI, Depends, Form, UploadFile, File, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base
from models import User
from auth import hash_password, verify_password
from datetime import datetime
import shutil
import os

Base.metadata.create_all(bind=engine)

app = FastAPI()

templates = Jinja2Templates(directory="templates")

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
def login(request: Request, username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.password):
        return templates.TemplateResponse("login.html", {"request": request, "error": "Invalid credentials"})
    
    user.last_active = datetime.utcnow()
    db.commit()

    response = RedirectResponse("/dashboard", status_code=302)
    response.set_cookie(key="user", value=username)
    return response

@app.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):
    username = request.cookies.get("user")
    if not username:
        return RedirectResponse("/")
    
    files = os.listdir(UPLOAD_FOLDER)
    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "files": files,
        "user": username
    })

@app.post("/upload")
def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return RedirectResponse("/dashboard", status_code=302)

@app.get("/register")
def register_user(db: Session = Depends(get_db)):
    # Default admin account for MVP
    if not db.query(User).filter(User.username == "admin").first():
        user = User(username="admin", password=hash_password("admin123"), role="admin")
        db.add(user)
        db.commit()
    return {"message": "Admin created (admin / admin123)"}

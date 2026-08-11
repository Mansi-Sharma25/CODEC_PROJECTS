from flask import Flask,request,render_template            
from pdf_parser import parse_resume
import sqlite3                      


def get_db_connection():                    
    conn = sqlite3.connect("resume_parser.db")
    return conn


def create_table():
    conn = get_db_connection()
    conn.execute(""" 
        CREATE TABLE IF NOT EXISTS candidates(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            phone TEXT,
            skills TEXT,
            education TEXT
        )
        """)
    conn.commit()
    conn.close()

app = Flask(__name__)                 

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload",methods=["POST"])
def upload():
    file = request.files["file"]

    if not file.filename.lower().endswith(".pdf"):             
            return "Please upload a PDF file."

    if not file or file.filename == "":                
        return "Please select a resume."
    
    file.save("uploads/resume.pdf")
    resume_data = parse_resume("uploads/resume.pdf")              

    conn = get_db_connection()
    existing = conn.execute("SELECT id FROM candidates WHERE email = ?",(", ".join(resume_data["E-mail"]),)).fetchone()

    if existing:
        conn.close()
        return "This resume is already stored in the database."

    conn.execute("""
        INSERT INTO candidates (name, email, phone, skills, education)
        VALUES (?, ?, ?, ?, ?)
    """, (
        resume_data["Name"],
        ", ".join(resume_data["E-mail"]),
        ", ".join(resume_data["Phone"]),
        ", ".join(resume_data["Skills"]),
        ", ".join(resume_data["Education"])
    ))

    conn.commit()
    conn.close()
    
    return render_template("result.html", data=resume_data)


@app.route("/search")
def search():
    query = request.args.get("q", "")
    conn = get_db_connection()

    candidates = conn.execute("""
        SELECT * FROM candidates
        WHERE name LIKE ?
        OR email LIKE ?
        OR skills LIKE ?
        OR education LIKE?
    """, (
        f"%{query}%",
        f"%{query}%",
        f"%{query}%",
        f"%{query}%"
    )).fetchall()

    conn.close()
    return render_template("index.html",candidates=candidates,query=query)


create_table() 
app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for, session, flash, send_file
import sqlite3
from datetime import date
import matplotlib.pyplot as plt
from fpdf import FPDF
import random
import io
import os
 
DB_NAME = "aceest_fitness.db"
app = Flask(__name__)
app.secret_key = "supersecretkey"
 
# ---------- DATABASE INITIALIZATION ----------
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT,
        role TEXT
    )
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE,
        age INTEGER,
        height REAL,
        weight REAL,
        program TEXT,
        calories INTEGER,
        target_weight REAL,
        target_adherence INTEGER,
        membership_status TEXT,
        membership_end TEXT
    )
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS progress (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_name TEXT,
        week TEXT,
        adherence INTEGER
    )
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS workouts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_name TEXT,
        date TEXT,
        workout_type TEXT,
        duration_min INTEGER,
        notes TEXT
    )
    """)
    # Default admin
    cur.execute("SELECT * FROM users WHERE username='admin'")
    if not cur.fetchone():
        cur.execute("INSERT INTO users VALUES ('admin','admin','Admin')")
    conn.commit()
    conn.close()
 
# ---------- UTILITY ----------
def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn
 
program_templates = {
    "Fat Loss": ["Full Body HIIT", "Circuit Training", "Cardio + Weights"],
    "Muscle Gain": ["Push/Pull/Legs", "Upper/Lower Split", "Full Body Strength"],
    "Beginner": ["Full Body 3x/week", "Light Strength + Mobility"]
}
 
# ---------- ROUTES ----------
@app.route("/", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"].strip()
        conn = get_db_connection()
        user = conn.execute("SELECT * FROM users WHERE username=? AND password=?", (username,password)).fetchone()
        conn.close()
        if user:
            session["user"] = username
            session["role"] = user["role"]
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid credentials", "danger")
    return render_template("login.html")
 
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
 
    conn = get_db_connection()
    clients = conn.execute("SELECT * FROM clients ORDER BY name").fetchall()
    conn.close()
 
    return render_template("dashboard.html",
                           user=session["user"],
                           role=session["role"],
                           clients=clients)
 
@app.route("/add_client", methods=["POST"])
def add_client():
    name = request.form.get("client_name")
    if name:
        conn = get_db_connection()
        conn.execute("INSERT OR IGNORE INTO clients (name,membership_status) VALUES (?,?)",(name,"Active"))
        conn.commit()
        conn.close()
        flash(f"Client {name} added!", "success")
    return redirect(url_for("dashboard"))
 
@app.route("/generate_program/<client>")
def generate_program(client):
    program_type = random.choice(list(program_templates.keys()))
    program_detail = random.choice(program_templates[program_type])
    conn = get_db_connection()
    conn.execute("UPDATE clients SET program=? WHERE name=?", (program_detail, client))
    conn.commit()
    conn.close()
    flash(f"Program for {client}: {program_detail}", "success")
    return redirect(url_for("dashboard"))
 
@app.route("/generate_pdf/<client>")
def generate_pdf(client):
    conn = get_db_connection()
    client_data = conn.execute("SELECT * FROM clients WHERE name=?", (client,)).fetchone()
    conn.close()
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial","B",16)
    pdf.cell(0,10,f"ACEest Client Report - {client}",ln=True)
    pdf.set_font("Arial","",12)
    cols = ["ID","Name","Age","Height","Weight","Program","Calories","Target Weight","Target Adherence","Membership","End"]
    for i,col in enumerate(cols):
        pdf.cell(0,10,f"{col}: {client_data[i]}",ln=True)
    pdf_path = f"{client}_report.pdf"
    pdf.output(pdf_path)
    return send_file(pdf_path, as_attachment=True)
 
@app.route("/membership/<client>")
def membership(client):
    conn = get_db_connection()
    status, end = conn.execute("SELECT membership_status,membership_end FROM clients WHERE name=?", (client,)).fetchone()
    conn.close()
    return f"Membership: {status}<br>Renewal Date: {end if end else 'N/A'}"
 
@app.route("/chart/<client>")
def chart(client):
    conn = get_db_connection()
    data = conn.execute("SELECT week,adherence FROM progress WHERE client_name=? ORDER BY id", (client,)).fetchall()
    conn.close()
    if not data:
        return "No data to display"
    weeks = [d["week"] for d in data]
    adherence = [d["adherence"] for d in data]
    fig, ax = plt.subplots()
    ax.plot(weeks, adherence, marker="o")
    ax.set_title("Weekly Adherence")
    ax.set_ylabel("%")
    ax.set_ylim(0,100)
    ax.grid(True)
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close(fig)
    return send_file(img, mimetype='image/png')
 
@app.route("/add_workout/<client>", methods=["GET","POST"])
def add_workout(client):
    if request.method == "POST":
        date_str = request.form["date"]
        workout_type = request.form["type"]
        duration = int(request.form["duration"])
        notes = request.form["notes"]
        conn = get_db_connection()
        conn.execute("INSERT INTO workouts (client_name,date,workout_type,duration_min,notes) VALUES (?,?,?,?,?)",
                     (client,date_str,workout_type,duration,notes))
        conn.commit()
        conn.close()
        flash("Workout added!", "success")
        return redirect(url_for("dashboard"))
    return render_template("add_workout.html", client=client)
 
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))
 
# ---------- RUN ----------
if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)
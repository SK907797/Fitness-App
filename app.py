from flask import Flask, request, jsonify, render_template, redirect
import sqlite3
from datetime import date

app = Flask(__name__)
DB_NAME = "aceest_fitness.db"


def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


# ---------- UI ROUTES ----------

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/clients-page")
def clients_page():
    conn = get_db()
    clients = conn.execute("SELECT * FROM clients").fetchall()
    conn.close()
    return render_template("clients.html", clients=clients)


@app.route("/add-client", methods=["POST"])
def add_client_ui():
    name = request.form.get("name")

    conn = get_db()
    conn.execute("INSERT INTO clients (name, membership_status) VALUES (?,?)",
                 (name, "Active"))
    conn.commit()
    conn.close()

    return redirect("/clients-page")


@app.route("/workouts-page")
def workouts_page():
    return render_template("workouts.html")


# ---------- API ROUTES (for DevOps testing) ----------

@app.route("/api/clients", methods=["GET"])
def get_clients():
    conn = get_db()
    data = conn.execute("SELECT * FROM clients").fetchall()
    conn.close()
    return jsonify([dict(row) for row in data])


@app.route("/api/clients", methods=["POST"])
def add_client_api():
    data = request.json
    conn = get_db()
    conn.execute("INSERT INTO clients (name) VALUES (?)", (data["name"],))
    conn.commit()
    conn.close()
    return jsonify({"message": "Client added"}), 201


# ---------- RUN ----------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
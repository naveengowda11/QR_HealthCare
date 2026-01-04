from flask import Flask, request, jsonify, send_file, session, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import qrcode, base64, os
from io import BytesIO

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_REPORTS = os.path.join(BASE_DIR, "uploads/reports")
UPLOAD_TEAM = os.path.join(BASE_DIR, "uploads/team")
os.makedirs(UPLOAD_REPORTS, exist_ok=True)
os.makedirs(UPLOAD_TEAM, exist_ok=True)

app = Flask(__name__)
app.secret_key = "qr-health-secret"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///qr_health.db"
db = SQLAlchemy(app)

# ---------------- MODELS ----------------
class Hospital(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hospital_id = db.Column(db.Integer)
    full_name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    blood_group = db.Column(db.String(10))
    allergies = db.Column(db.String(300))
    chronic_conditions = db.Column(db.String(300))
    emergency_contact = db.Column(db.String(20))

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer)
    filename = db.Column(db.String(200))
    filepath = db.Column(db.String(300))

with app.app_context():
    db.create_all()

# ---------------- AUTH ----------------
@app.route("/api/hospital/register", methods=["POST"])
def hospital_register():
    data = request.json
    if Hospital.query.filter_by(email=data["email"]).first():
        return jsonify({"error": "exists"}), 400
    h = Hospital(name=data["name"], email=data["email"], password=data["password"])
    db.session.add(h)
    db.session.commit()
    return jsonify({"success": True})

@app.route("/api/hospital/login", methods=["POST"])
def hospital_login():
    data = request.json
    h = Hospital.query.filter_by(email=data["email"], password=data["password"]).first()
    if not h:
        return jsonify({"error": "invalid"}), 401
    session["hospital_id"] = h.id
    session["hospital_name"] = h.name
    return jsonify({"success": True, "name": h.name})

@app.route("/api/logout")
def logout():
    session.clear()
    return jsonify({"success": True})

@app.route("/api/session")
def session_info():
    if "hospital_id" not in session:
        return jsonify({"logged": False})
    return jsonify({"logged": True, "name": session["hospital_name"]})

# ---------------- PATIENT + QR ----------------
@app.route("/api/patient/create", methods=["POST"])
def create_patient():
    if "hospital_id" not in session:
        return jsonify({"error": "unauthorized"}), 401

    p = Patient(
    hospital_id=session["hospital_id"],
    full_name=request.form.get("full_name"),
    age=request.form.get("age"),
    gender=request.form.get("gender"),
    blood_group=request.form.get("blood_group"),
    phone=request.form.get("phone"),
    emergency_contact=request.form.get("emergency_contact"),
    allergies=request.form.get("allergies"),
    chronic_conditions=request.form.get("chronic_conditions"),
    medications=request.form.get("medications"),
    surgeries=request.form.get("surgeries"),
    family_history=request.form.get("family_history"),
    height=request.form.get("height"),
    weight=request.form.get("weight"),
    bp=request.form.get("bp"),
    disabilities=request.form.get("disabilities"),
    notes=request.form.get("notes")
)

    
    db.session.add(p)
    db.session.commit()

    for f in request.files.getlist("reports"):
        if f.filename:
            name = secure_filename(f.filename)
            path = os.path.join(UPLOAD_REPORTS, name)
            f.save(path)
            db.session.add(Report(patient_id=p.id, filename=name, filepath=path))
    db.session.commit()

    qr_url = f"http://127.0.0.1:5000/emergency.html?id={p.id}"
    img = qrcode.make(qr_url)
    buf = BytesIO()
    img.save(buf, format="PNG")
    qr = base64.b64encode(buf.getvalue()).decode()

    return jsonify({"qr": qr})

# ---------------- EMERGENCY ----------------
@app.route("/api/emergency/<int:pid>")
def emergency(pid):
    p = Patient.query.get_or_404(pid)
    return jsonify({
        "Name": p.full_name,
        "Blood Group": p.blood_group,
        "Allergies": p.allergies,
        "Conditions": p.chronic_conditions,
        "Emergency Contact": p.emergency_contact
    })

# ---------------- FILE SERVE ----------------
@app.route("/uploads/reports/<path:p>")
def serve_report(p):
    return send_file(os.path.join(UPLOAD_REPORTS, p))

# ---------------- FRONTEND ----------------
@app.route("/<path:p>")
def frontend(p):
    return send_file(os.path.join("frontend", p))

@app.route("/")
def root():
    return redirect("/login.html")
@app.route("/uploads/team/<path:filename>")
def serve_team_image(filename):
    return send_file(os.path.join("uploads/team", filename))

if __name__ == "__main__":
    app.run(debug=True)

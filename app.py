
import io
from flask import Flask, render_template, request, Response, send_file, abort
from converter import excel_to_txt

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")

@app.post("/convert")
def convert():
    file = request.files.get("file")
    if not file or file.filename == "":
        return abort(400, "Geen bestand geüpload.")
    try:
        txt = excel_to_txt(file.read())
    except Exception as e:
        # Show a friendly error to the user with the Python exception in logs
        return abort(400, f"Kon bestand niet verwerken: {e}")
    # Prepare a download
    out_name = "cue_export.txt"
    return Response(
        txt,
        mimetype="text/plain; charset=utf-8",
        headers={"Content-Disposition": f"attachment; filename={out_name}"}
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

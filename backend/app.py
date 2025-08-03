from flask import Flask, render_template
from routes.voice import voice_bp

app = Flask(__name__)

# Register the voice blueprint
app.register_blueprint(voice_bp)

@app.route("/")
def home():
    return render_template("ui.html")

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

# Old way: Runs pygame locally (you can keep or remove this)
@app.route('/run-simulation')
def run_simulation():
    subprocess.run(["python", "simulation.py"])
    return "✅ Simulation finished! (Check the simulation window)"

# New way: Serve simulation page in browser
@app.route("/simulation")
def simulation():
    return render_template("simulation.html")

if __name__ == "__main__":
    app.run(debug=True)

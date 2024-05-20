from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)

@app.route("/")
def index():
  return render_template('dashboard.html')

@app.route("/verifikasi")
def verifikasi():
   return render_template('verifikasi.html')

if __name__ == "__main__": 
    app.run(debug=True)
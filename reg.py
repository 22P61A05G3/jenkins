from flask import Flask, render_template, request
import os 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("form.html")

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get("name")
    email = request.form.get("email")
    age = request.form.get("age")
    return render_template("result.html", name=name, email=email, age=age)

if __name__ == '__main__':
    debug_mode = os.getenv('FLASK_ENV') != 'production'  # Disable debug if running in production
    app.run(debug=debug_mode)
    

from flask import Flask, render_template, request, jsonify



app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('homePage.html')

@app.route("/About")
def About():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
from flask import Flask

app = Flask(__name__)

@app.route('/') #URL where to view website, / means homepage
def home():
    return "Website Test"

@app.route('/about/')
def about():
    return "About page"

if __name__ == "__main__":
    app.run(debug = True)
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') #URL where to view website, / means homepage
def home():
    return render_template("index.html")
    
@app.route('/about/')
def about():
    return render_template("achievement0.html")

@app.route('/STEMCompetition/')
def stem():
    return render_template("STEM.html")

@app.route('/EagleScout/')
def eagle():
    return render_template("EagleScout.html")

@app.route('/SATRO/')
def satro():
    return render_template("SATRO.html")

@app.route('/NHS/')
def nhs():
    return render_template("NHS.html")



if __name__ == "__main__":
    app.run(debug = True)
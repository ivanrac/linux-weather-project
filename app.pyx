
fom flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Ahoj toto je moja prva Flask appka"

app.run(host="0.0.0.0" , port=5000)

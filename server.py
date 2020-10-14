from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
  return "<h1>Testing App</h1>"

@app.route("/testing")
def testing():
  return "<h1>Hello world!</h1>"

if __name__ == "__main__":
  app.run()
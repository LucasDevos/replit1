from flask import Flask

app = Flask("MaWebapp")

@app.route("/")
def page_principale():
  return "coucou"

app.run("0.0.0.0", "3904")
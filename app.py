from unittest import result
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/cap3/<string:sentence>")
def cap3(sentence):
  z = list(sentence)
  for x in range(2, len(z),3):  
     z[x] = z[x].upper()
  cap3_string = ''.join(z)
  result = {
   
    "cap3_string":cap3_string,
    "string": sentence

  }
  return jsonify(result)

if __name__ == "__main__":
  app.run(debug=True)
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
  sentence = ''.join(z)
  return sentence

if __name__ == "__main__":
  app.run(debug=True)

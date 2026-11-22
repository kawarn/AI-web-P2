from flask import Flask, request, render_template

app = Flask(__name__)

lastrev="none"

@app.route("/")
def start():
    return render_template('start.html')

@app.route("/reversed")
def reversed():
    global lastrev
    rev = request.args['rev'][::-1]
    resp= render_template('reversed.html', rev=rev, lastrev=lastrev)
    lastrev=rev
    return resp

if __name__ == "__main__":
    app.run(debug=True)
    
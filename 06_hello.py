from flask import Flask, request

# run this program with:
#
# > python 06_hello.py
#
# or
# > flask --app=06_hello.py run
#
# Stop the server with Ctrl-C in the terminal.

app = Flask(__name__)

@app.route("/")
def start():
    return """<h1>Hello world.</h1>
    <img src='https://www.uni-osnabrueck.de/fileadmin/_processed_/3/3/csm_Logo-IKW-en_RGB_b344d26ec3.png'>

    <p>OK.</p>
    <a href='/about'>About</a>"""

@app.route("/about")
def about():
    return "<p>About!</p>"

if __name__ == "__main__":
    app.run(debug=True)

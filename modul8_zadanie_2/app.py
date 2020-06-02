from flask import Flask
from flask import request, redirect
from flask import render_template
from datetime import time

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template("main_page.html", timestamp=time())


@app.route('/me')
def about_me():
    return render_template("about_me.html", timestamp=time())


@app.route('/contact', methods=['GET'])
def contact():
    return render_template("contact.html", timestamp=time())


@app.route('/contactme', methods=['GET', 'POST'])
def contact_sheet():
    if request.method == 'GET':
        return render_template("contact_me.html", timestamp=time())
    elif request.method == 'POST':
        data = request.form
        username = data.get("firstname")
        return f"Dziękujemy {username}"



if __name__ == '__main__':
    app.run()

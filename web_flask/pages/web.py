from web_flask.pages import web
from flask import render_template

@web.route('/howto', strict_slashes=False)
def howto():
    return render_template("howto.html")

@web.route('/faq', strict_slashes=False)
def faq():
    return render_template("faq.html")

if __name__ == '__main__':
    app.run(debug=True)

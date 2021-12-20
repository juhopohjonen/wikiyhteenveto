import re
from flask import Flask, render_template, request
from flask.typing import ResponseValue

from markupsafe import escape
from werkzeug.wrappers import response
import wikipedia
from wikipedia.wikipedia import page, summary

app = Flask(__name__)

styleurl = "jou.html"
wikipedia.set_lang("fi")

@app.route("/")
def index():
    return render_template("homepage.html")



@app.route("/search")
def search():
    query = escape(request.args.get("q"))

    response = wikipedia.search(query, results=50)

    return render_template("searchtemplate.html", queryToShow=query, responseToShow=response, hrefToOriginal=str("https://fi.wikipedia.org/wiki/" + query))
    
@app.route("/pages/<notEscapedPagename>")
def getPage(notEscapedPagename):

    pagename = escape(notEscapedPagename)

    try:
        response = wikipedia.page(pagename)
        imgUrls = escape(response.images)

        return render_template("pagetemplate.html", aihe=pagename, summary=str(response.summary))
    except:
        return f"<h1>Ei löydy!</h1>"




if "__main__" == __name__:
    app.run(debug=True)
from flask import Blueprint, render_template

# This allow you to create "webpages" in views.py and then pull them in to app.py to be displayed by the server
views = Blueprint(__name__,"views")

# Home page.  "/" will always be home page for your website.
# Every "webpage" needs a defined route. The route is created with the decorator @views.route("").
# What is in between the "" in the above statement is route of the "webpage".  All routes start with "/".
@views.route("/")
# Every "webpage" needs a function within them.
def home():
    # Every function should have a return statement.  render_template() simply displays an html page from the
    # templates folder.
    return render_template("index.html", name="Tim")

# This route creates the "webpage" called examples.
@views.route("/examples")
def examples():
    return render_template("Examples.html")




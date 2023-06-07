from flask import Flask, render_template
from views import views

# This is creating the Flask server
app = Flask(__name__)
# This is registering views.py as the location we will be pull the webpage information from.
app.register_blueprint(views, url_prefix="/")


@app.route('/leaflet')
def root():
    markers=[
        {
        'lat':0,
        'lon':0,
        'popup':'This is the middle of the map.'
        }
    ]
    return render_template('leaflet.html',markers=markers )

# Basic statement to help the script run safely.
if __name__ == '__main__':
    # The function runs the Flask server.  debug=True runs the server in debug mode.
    # This allows you to edit the script while the script is running.
    app.run(host="localhost", port=8080, debug=True)
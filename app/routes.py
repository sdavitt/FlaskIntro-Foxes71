# need to import our background app from init
from app import app
from flask import render_template


# each route function describes a url endpoint or a process run during refresh

# syntax of the route function decorator
# @<appname/blueprintname>.route('<url endpoint>', [methods=['GET', 'POST', 'PUT']])
@app.route('/', methods=['GET'])
def home():
    animals_list=['Fennec Fox', 'Shrew', 'Arctic Fox', 'Polar Bear', 'Toad', 'Orca', 'Mallard Duck']
    return render_template('index.html', animals=animals_list)

# @app.route('/url') decorator tells the function what URL it should be associated with
@app.route('/otheranimals', methods=['GET'])
def otheranimals():
    animals_list=['Arctic Fox', 'Mandarin Duck', 'Angry Goose', 'Grizzly', 'Ocelot']
    # render_template() tells the function(or the route) what html file it should show at that url with what info
    return render_template('index.html', animals=animals_list)

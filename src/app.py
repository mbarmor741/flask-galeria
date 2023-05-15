# From https://github.com/datademofun/heroku-basic-flask
# Nota: en ese tutorial se ve como hacerlo
# - con Heroku CLI
# - sin usar GitHub
# Aunque luego al final lo manda a GitHub


from flask import Flask, render_template
from datetime import datetime
import locale




app = Flask(__name__)
locale.setlocale(locale.LC_TIME, '')




@app.route('/')
def homepage():


the_time = datetime.now().strftime("%A, %d %b %Y %H:%M")


# Render HTML with variable
return render_template("index.html", the_time=the_time, tema="dogs")



if __name__ == '__main__':
app.run(debug=True, use_reloader=True)

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


#creating flask instance
app = Flask(__name__)
app.config['SECRET_KEY'] = "Trotty is gay"

# creating a form class
class NamerForm(FlaskForm):
    name = StringField("What is your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")

# creating routes
@app.route('/')
def index():
    first_name = 'Chris'
    stuff = "This is <strong>Bold</strong> text"

    favorite_pizza = ['Pepperoni', 'Chreese', 'Sausage', 41]
    return render_template('index.html', first_name=first_name, stuff=stuff, favorite_pizza=favorite_pizza)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    # validating
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''

    return render_template('name.html', name=name, form=form)


# running the server with debug by hitting play 
if __name__ == '__main__':
    app.run(debug=True)
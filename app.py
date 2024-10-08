from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


#creating flask instance
app = Flask(__name__)
# creating database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# every flask has to have this
app.config['SECRET_KEY'] = "Trotty is gay"
# initalizing database
db = SQLAlchemy(app)

# creating the model
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    # create a string
    def __repr__(self):
        return '<Name %r>' % self.name

    # need this for the databse intialization    
    with app.app_context():     
        db.create_all()

# creating a form class
class UserForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    submit = SubmitField("Submit")

# creating a form class
class NamerForm(FlaskForm):
    name = StringField("What is your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")

@app.route('/user/add', methods=['GET', 'POST'])
def add_user():
    name = None
    form = UserForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first
        if user is None:
            user = Users(name=form.name.data, email=form.email.data)
            db.session.add(user)
            db.session.commit()
        name = form.name.data
        form.name.data = ''
        form.email.data = ''
        flash('User Added Successfully!!')
    our_users = Users.query.order_by(Users.date_added)    
    return render_template('add_user.html', form=form, name=name, our_users=our_users)

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
        flash('Form Submitted Successfully!')

    return render_template('name.html', name=name, form=form)


# running the server with debug by hitting play 
if __name__ == '__main__':
    app.run(debug=True)
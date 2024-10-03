from flask import Flask, render_template


#creating flask instance
app = Flask(__name__)

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

# running the server with debug by hitting play 
if __name__ == '__main__':
    app.run(debug=True)
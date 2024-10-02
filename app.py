from flask import Flask, render_template


#creating flask instance
app = Flask(__name__)

# creating routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return "<h1>Hello {}!!!</h1>".format(name)

# running the server with debug by hitting play 
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask
from flask import render_template

# creates a Flask application, named app
app = Flask(__name__)

# a route where we will display a welcome message via an HTML template
@app.route("/")
def hello():
    message = "Hello, World"
    return render_template('index.html', message=message)

@app.route("/home")
def home():
    message = "Hello, World"
    return render_template('index.html', message=message)

@app.route("/about-us")
def about():
    message = "Hello, World"
    return render_template('about.html', message=message)

@app.route("/datasets")
def datasets():
    message = "Hello, World"
    return render_template('datasets.html', message=message)


@app.route("/donate")
def donate():
    message = "Hello, World"
    return render_template('donate.html', message=message)

@app.route("/volunteer")
def volunteer():
    message = "Hello, World"
    return render_template('volunteer.html', message=message)



# run the application
if __name__ == "__main__":
    app.run(debug=True)

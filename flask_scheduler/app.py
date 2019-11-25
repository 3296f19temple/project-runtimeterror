from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/schedule')
def output_page():
    return '<h1>Schedule Page</h1>'

if __name__ == '__main__':
    app.run()
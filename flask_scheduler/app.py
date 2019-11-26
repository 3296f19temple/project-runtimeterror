from flask import Flask, render_template
app = Flask(__name__)

classes = [
    {
        'crn':'11111',
        'name':'class name 1',
        'meeting_time':'MWF 5:00-5:50'
    },
    {
        'crn':'2222',
        'name':'class name 2',
        'meeting_time':'MWF 6:00-6:50'
    }
]

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/schedule')
def output_page():
    return render_template('schedule.html',title='Schedule Maker - Schedule',classes=classes)

if __name__ == '__main__':
    app.run()
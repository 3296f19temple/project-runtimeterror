from flask import Flask, render_template, url_for
from forms import ScheduleForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'aae3d59542630a35356332ea6ca60652'

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
def home():
    form = ScheduleForm()
    return render_template('home.html',title='Schedule Maker - Home', form = form)

@app.route('/schedule')
def schedule():
    return render_template('schedule.html',title='Schedule Maker - Schedule',classes=classes)

if __name__ == '__main__':
    app.run()
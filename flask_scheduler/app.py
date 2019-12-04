from flask import Flask, render_template, url_for, flash, redirect
from forms import ScheduleForm
from make_schedules import makeSchedule
app = Flask(__name__)

app.config['SECRET_KEY'] = 'aae3d59542630a35356332ea6ca60652'

@app.route('/',methods=['GET','POST'])
def home():
    form = ScheduleForm()
    checkValidation = form.validate_on_submit()
    if checkValidation:
        flash(f'Schedule will be made for {form.class1.data}, {form.class2.data}, {form.class3.data}','success')
        classes = []
        classes.append(form.class1.data)
        classes.append(form.class2.data)
        classes.append(form.class3.data)
        classes.append(form.class4.data)
        classes.append(form.class5.data)
        classes.append(form.class6.data)
        classes.append(form.class7.data)
        sched = makeSchedule()
        schedList = sched.create_schedule(classes)
        print(schedList)
        print(classes)
        length = len(schedList)
        return render_template('schedule.html',title='Schedule Maker - Schedule',schedules=schedList, length=length)
    print(form.errors)
    print(checkValidation)
    return render_template('home.html',title='Schedule Maker - Home', form = form)

@app.route('/schedule')
def schedulePage():
    return render_template('schedule.html',title='Schedule Maker - Schedule',classes=classes)

if __name__ == '__main__':
    app.run(debug=True)

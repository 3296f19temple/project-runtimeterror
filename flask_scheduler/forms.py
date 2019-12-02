from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ScheduleForm(FlaskForm):
    class1 = StringField('Class 1')
    class2 = StringField('Class 2')
    class3 = StringField('Class 3')
    class4 = StringField('Class 4')
    class5 = StringField('Class 5')
    submit = SubmitField('Schedule')

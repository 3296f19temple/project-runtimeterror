from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ScheduleForm(FlaskForm):
    class1 = StringField('Class 1', validators=[DataRequired()])
    class2 = StringField('Class 2', validators=[DataRequired()])
    class3 = StringField('Class 3', validators=[DataRequired()])
    class4 = StringField('Class 4', validators=[DataRequired()])
    class5 = StringField('Class 5', validators=[DataRequired()])
    submit = SubmitField('Schedule')

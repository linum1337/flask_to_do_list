from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class TableForm(FlaskForm):
    list_days_names = ['' for i in range(31)]
    list_days_text = ['' for j in range(31)]
    name_month = StringField('название месяца', validators=[DataRequired()])
    submit_save = SubmitField('Сохранить')

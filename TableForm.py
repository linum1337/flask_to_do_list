from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class TableForm(FlaskForm):
    list_days_text = []
    list_days_names = []
    for i in range(31):
        list_days_names.append(StringField('название дня', validators=[DataRequired()]))
        list_days_text.append(StringField('', validators=[DataRequired()]))
    name_month = StringField('название месяца', validators=[DataRequired()])
    submit_save = SubmitField('Сохранить')

from flask_wtf import FlaskForm
from wtforms import SubmitField, FieldList, TextAreaField, DateTimeField
from wtforms.validators import DataRequired


class TableForm(FlaskForm):
    list_days = FieldList(TextAreaField('название дня'), min_entries=35)
    list_dates = FieldList(DateTimeField(''), min_entries=35)
    submit_save = SubmitField('Сохранить')

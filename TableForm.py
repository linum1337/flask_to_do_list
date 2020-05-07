from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList
from wtforms.validators import DataRequired


class TableForm(FlaskForm):
    list_days = FieldList(StringField('название дня'), min_entries=31)
    submit_save = SubmitField('Сохранить')

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class TableForm(FlaskForm):
    list_days = []
    dn1 = StringField('название дня')
    dn2 = StringField('название дня')
    dn3 = StringField('название дня')
    dn4 = StringField('название дня')
    dn5 = StringField('название дня')
    dn6 = StringField('название дня')
    dn7 = StringField('название дня')
    dn8 = StringField('название дня')
    dn9 = StringField('название дня')
    dn10 = StringField('название дня')
    dn11 = StringField('название дня')
    dn12 = StringField('название дня')
    dn13 = StringField('название дня')
    dn14 = StringField('название дня')
    dn15 = StringField('название дня')
    dn16 = StringField('название дня')
    dn17 = StringField('название дня')
    dn18 = StringField('название дня')
    dn19 = StringField('название дня')
    dn20 = StringField('название дня')
    dn21 = StringField('название дня')
    dn22 = StringField('название дня')
    dn23 = StringField('название дня')
    dn24 = StringField('название дня')
    dn25 = StringField('название дня')
    dn26 = StringField('название дня')
    dn27 = StringField('название дня')
    dn28 = StringField('название дня')
    dn29 = StringField('название дня')
    dn30 = StringField('название дня')
    dn31 = StringField('название дня')
    list_days_text = ['' for i in range(31)]
    list_days_names = ['' for j in range(31)]
    submit_save = SubmitField('Сохранить')

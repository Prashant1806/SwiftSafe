from wtforms import Form, StringField, validators

class InstagramComparisonForm(Form):
    account1 = StringField('First Instagram Account', validators=[validators.InputRequired()])
    account2 = StringField('Second Instagram Account', validators=[validators.InputRequired()])

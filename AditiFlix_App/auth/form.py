from flask_wtf import FlaskForm, RecaptchaField
from wtforms import (StringField,
                     TextAreaField,
                     SubmitField,
                     PasswordField,
                     DateField,
                     SelectField)
from wtforms.validators import (DataRequired,
                                Email,
                                EqualTo,
                                Length,
                                URL)

...

class SignupForm(FlaskForm):
    """Sign up for a user account."""
    username = StringField('Username', [
        DataRequired(message='Your username is required'),
        Length(min=4, message='Your username is too short')])
    password = PasswordField('Password', [
        DataRequired(message="Please enter a password."),
    ])
    # confirmPassword = PasswordField('Repeat Password', [
    #         EqualTo(password, message='Passwords must match.')
    #         ])
    #recaptcha = RecaptchaField()
    submit = SubmitField('Submit')
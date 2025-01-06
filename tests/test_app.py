from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with your secret key

class TestForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = TestForm()
    if form.validate_on_submit():
        return f"Hello, {form.name.data}!"
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)

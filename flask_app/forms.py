from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError

class SearchForm(FlaskForm):
    search_query = StringField('champion name', validators=[InputRequired(), Length(min=1,max=30)])
    submit = SubmitField('Submit')

class ChampionNoteForm(FlaskForm):
    name = StringField('Name/Alias', validators=[InputRequired(), Length(min=1, max=50)])
    text = TextAreaField('Content of Review', validators=[InputRequired(), Length(min=1, max=500)])
    submit = SubmitField('Submit')
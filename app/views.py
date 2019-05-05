from app import app
from flask import render_template, redirect, flash, session
from app.forms import ConverterForm
from converter import *

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    title = 'Converter arabic nums to rome'
    return render_template('index.html',
                           title=title,
                          )


@app.route('/convert', methods=['GET', 'POST'])
def convert():
    form = ConverterForm()
    if form.validate_on_submit():
        try:
            arab = int(form.arab_num.data)
            if arab > 4999:
                raise
            rome = arab_to_rome(arab)

        except:
            flash('Эти данные не могут быть корректно переведены в римское число!')
            rome=''
        return render_template('converter.html',
                           form=form,
                           rome=rome,
                           title='Converter arabic nums to rome'
                           )
    return render_template('converter.html',
                           form=form,
                           title='Converter arabic nums to rome'
                           )

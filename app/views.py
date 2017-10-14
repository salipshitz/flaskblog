from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

current_user = None

users = [
    {'nickname': 'Mark Anthony',
     'path': '/users/VivirMiVida',
     'account_name': '@VivirMiVida'},
    {'nickname': 'Julian CremeSalad',
     'path': '/users/jcream',
     'account_name': '@jcream'},
    {'nickname': 'But Brutus is an honourable man.',
     'path': '/users/realBrutalBrutus',
     'account_name': '@realBrutalBrutus'},
    {'nickname': 'Queso-us',
     'path': '/users/NotCassius',
     'account_name': '@NotCassius'},
    {'nickname': 'John Pizza',
     'path': '/users/JoPizza',
     'account_name': '@JoPizza'}
]
posts = [
    {
        'author': users[0],
        'body': 'Voy a reir, voy a bailar when Julian CremeSalad is the king'
    },
    {
        'author': users[3],
        'body': 'Stab dat salad 23 time bro!'
    },
    {
        'author': users[0],
        'body': 'Friends, salads, croutonmen, lend me your ears. I come to bury CremeSalad, not to praise him, cause Brutal is an honourable man.'
    },
    {
        'author': users[4],
        'body': 'Climate change is a hoax and the Antarctican government is torching the ice caps'
    }
]
    

@app.route("/")
@app.route("/index")
def home():
    return render_template('index.html',
                           user=current_user,
                           pg='/users',
                           link_text='Users',
                           posts=posts)
@app.route("/users")
def users():
    return render_template('members.html',
                           title='Users',
                           index='/index',
                           users=users)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for openid = "%s", remember_me = %s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect("/index")
    return render_template('login.html',
                           title='Sign in',
                           form=form)

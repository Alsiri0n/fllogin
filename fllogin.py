"""
Login submodule for flask application
"""
from flask import Blueprint,render_template,request,flash, session, redirect, url_for

fllogin = Blueprint('fllogin', __name__, template_folder='templates', static_folder='static')


@fllogin.route('/', methods=["GET", "POST"])
def index():
    """
    Index page for fllogin
    """
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and \
         request.form['username'] == 'adm1n' and \
         request.form['psw'] == "123":
         session['userLogged'] = request.form['username']
        # For url_for used fullname flprofile.profile
         return redirect(url_for('flprofile.profile', username=session['userLogged']))
    return render_template('fllogin/login.html', title='Авторизация')

@fllogin.route('/register', methods=["GET", "POST"])
def register():
    """
    Registration page for fllogin
    """
    return render_template('fllogin/register.html', title='Регистрация')


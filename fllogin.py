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
         return redirect(url_for('profile', uysername=session['userLogged']))
    return render_template('fllogin/login.html', title='Авторизация')
 
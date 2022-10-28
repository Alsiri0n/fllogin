"""
Login submodule for flask application
"""
from flask import Blueprint,render_template,request,flash, session, redirect, url_for, g
from werkzeug.security import generate_password_hash

fllogin = Blueprint('fllogin', __name__, template_folder='templates', static_folder='static')

dbase = None


@fllogin.before_request
def before_request():
    """
    Establish connection to DB before execution request
    """
    global dbase
    dbase = g.get('link_db')


@fllogin.teardown_request
def teardown_request(request):
    """
    Close connection to database, if connected
    """
    global dbase
    dbase = None
    return request


@fllogin.route('/', methods=['GET', 'POST'])
def index():
    """
    Index page for fllogin
    """
    if 'userLogged' in session:
        return redirect(url_for('flprofile.profile', username=session['userLogged']))
    elif request.method == 'POST' and \
         request.form['username'] == 'adm1n' and \
         request.form['psw'] == "123":
         session['userLogged'] = request.form['username']
        # For url_for used fullname flprofile.profile
         return redirect(url_for('flprofile.profile', username=session['userLogged']))
    return render_template('fllogin/login.html', title='Авторизация')

@fllogin.route('/register', methods=['GET', 'POST'])
def register():
    """
    Registration page for fllogin
    """
    if request.method == 'POST':
        if (
            len(request.form['username']) > 4 and len(request.form['email']) > 4 and \
            len(request.form['psw']) > 4 and request.form['psw'] == request.form['psw2']
            ):
            hash = generate_password_hash(request.form['psw'])
            res = dbase.addUser(request.form['username'], request.form['email'], hash)
            if res:
                flash('Вы успешно зарегистрированы','success')
                return redirect(url_for('fllogin.index'))
            else:
                flash('Ошибка добавления в БД','error')
        else:
            flash('Неверно заполнены поля','error')
    return render_template('fllogin/register.html', title='Регистрация')


@fllogin.route('/logout', methods=["GET", "POST"])
def logout():
    """
    Implement logout
    """
    session.pop('userLogged')
    return redirect(url_for('.index'))
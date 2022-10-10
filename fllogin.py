"""
Test submodule working for Jenkins CI/CD
"""
from flask import Blueprint,render_template,request,flash

fllogin = Blueprint('fllogin', __name__, template_folder='templates', static_folder='static')


@fllogin.route('/', methods=["GET", "POST"])
def index():
    """
    Test index page for submodule
    """
    if request.method == 'POST':
        if len(request.form['username']) > 2:
            flash('Сообщение отправлено', category="success")
        else:
            flash('Ошибка отправки', category="error")
    return render_template('fllogin/login.html', title='Логин')

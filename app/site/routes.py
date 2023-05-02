from flask import Blueprint, render_template
from models import User, db, check_password_hash, Post
from flask import Blueprint, render_template, request, redirect, url_for, flash
from forms import UserLoginForm

# imports for flask login 
from flask_login import login_user, logout_user, LoginManager, current_user, login_required

auth = Blueprint('auth', __name__, template_folder='auth_templates')

site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/', methods = ['GET', 'POST'])
def home():
    form = UserLoginForm()
    return render_template('index.html', form = form )

@site.route('/profile', methods = ['GET', 'POST'])
def profile():
    return render_template('profile.html')
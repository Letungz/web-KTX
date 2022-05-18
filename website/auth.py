import email
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Sinhvien, User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/')
def start():
    return redirect(url_for('auth.login'))


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            return redirect(url_for('auth.login'))

    return render_template("sign_up.html", user=current_user)

@auth.route('/dknoitru', methods=['GET', 'POST'])
@login_required
def dknoitru():
    if request.method == 'POST':
        email = request.form.get('email')
        studentId = request.form.get('studentId')
        studentName = request.form.get('studentName')
        dob = request.form.get('dob')
        course = request.form.get('course')
        department = request.form.get('department')
        studentClass = request.form.get('studentClass')
        nationalId = request.form.get('nationalId')
        issuedDt = request.form.get('issuedDt')
        phone = request.form.get('phone')
        religion = request.form.get('religion')
        gender = request.form.get('gender')
        issuedPlace = request.form.get('issuedPlace')
        ethnic = request.form.get('ethnic')
        Address = request.form.get('Address')
        dormId = request.form.get('dormId')
        sv = User.query.filter_by(email=email).first()
        if sv:
            new_sv = Sinhvien(email=email, studentId=studentId, studentName=studentName, dob=dob, course=course, department=department, 
            studentClass=studentClass, nationalId=nationalId, issuedDt=issuedDt, phone=phone, religion=religion, gender=gender, 
            issuedPlace=issuedPlace, ethnic=ethnic, Address=Address, dormId=dormId)
            db.create_all()
            db.session.add(new_sv)
            db.session.commit()
            return redirect(url_for('views.home'))
        else:
            flash('Email does not exist.', category='error')
    return render_template("dknoitru.html", user=current_user)


@auth.route('/dondk')
@login_required
def don():
    return render_template("dondk.html", values=Sinhvien.query.all())


@auth.route('/profile')
def profile():
    return render_template("profile.html", user=current_user)

#@auth.route('/thanhtoan', methods=['GET', 'POST'])
#@login_required
#def dknoitru():
#   if request.method == 'POST':
 #       studentId = request.form.get('studentId')
#        sv = User.query.filter_by(studentId=studentId).first()
#        if sv:
#            return redirect(url_for('auth.thanhtoan'))
#        else:
#            flash('Student does not exist.', category='error')
#    return render_template("thanhtoan.html", user=current_user)



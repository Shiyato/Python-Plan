from flask import render_template, redirect
from flask_login import login_user, logout_user, current_user
from forms import PlanForm, RegisterForm, LoginForm
from init import app, login_manager, db
from db import User, Plan, create_user, create_plan


@login_manager.user_loader
def user_loader(id):
    return User.query.filter_by(id=id).first()


@app.route('/', methods=['GET', 'POST'])
def index():
    form = PlanForm()
    user = current_user
    if form.validate_on_submit() and current_user.is_authenticated:
        form = PlanForm()
        obj_container = {
            'pf1': form.pf1.data,
            'pf2': form.pf2.data,
            'pf3': form.pf3.data,
            'pf4': form.pf4.data,
            'pf5': form.pf5.data,
            'pf6': form.pf6.data,
            'pf7': form.pf7.data,
            'pf8': form.pf8.data,
            'pf9': form.pf9.data,
            'pf10': form.pf10.data,
            'pf11': form.pf11.data,
            'pf12': form.pf12.data,
            'pf13': form.pf13.data,
            'pf14': form.pf14.data,
            'pf15': form.pf15.data,
            'pf16': form.pf16.data,
            'pf17': form.pf17.data,
            'pf18': form.pf18.data,
            'pf19': form.pf19.data,
            'pf20': form.pf20.data,
            'pf21': form.pf21.data,
            'pf22': form.pf22.data,
            'pf23': form.pf23.data,
            'pf24': form.pf24.data,
            'pf25': form.pf25.data,
            'pf26': form.pf26.data,
            'pf27': form.pf26.data
        }
        checked = ''
        for key, value in obj_container.items():
            if value:
                checked += key + ';'
        plan_query = Plan.query.filter_by(user_id=current_user.id)
        if plan_query.first():
            plan_query.update({'plan_numbers': checked[:-1]})
            db.session.commit()
        else:
            create_plan(current_user.id, checked[:-1])
    if current_user.is_authenticated:
        plan = Plan.query.filter_by(user_id=current_user.id).first()
        if plan:
            checked_items = list(map(lambda item: int(item[2:]), plan.plan_numbers.split(';')))
        else:
            checked_items = []
    else:
        checked_items = []
    return render_template('index.html', range=range, str=str, form=form, user=user, checked_items=checked_items)


@app.route('/education-materials')
def education():
    return render_template('education.html')


@app.route('/additions')
def additions():
    return render_template('additions.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/')
    form = LoginForm()
    errors = set()
    if form.validate_on_submit():
        user = User.query.filter_by(login=form.login.data).first()
        if not user:
            errors.add(4)
        else:
            if form.password.data != user.password:
                errors.add(5)
            else:
                login_user(user, remember=True)
                return redirect('/')
    else:
        try:
            errors.add(*form.password.errors)
        except:
            pass
        try:
            errors.add(*form.login.errors)
        except:
            pass
    return render_template('login.html', form=form, errors=errors)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect('/')
    errors = set()
    form = RegisterForm()
    if form.validate_on_submit():
        if not User.query.filter_by(login=form.login.data).first():
            create_user(form.login.data, form.password.data)
            user = User.query.filter_by(login=form.login.data).first()
            login_user(user, remember=True)
            return redirect('/')
        else:
            errors.add(4)
    else:
        try:
            errors.add(*form.password.errors)
        except:
            pass
        try:
            errors.add(*form.login.errors)
        except:
            pass
    return render_template('register.html', form=form, errors=errors)


@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
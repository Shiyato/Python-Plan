from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, PasswordField
from wtforms.validators import DataRequired
from wtforms import ValidationError
from db import User


class RegisterForm(FlaskForm):
    login = StringField('login', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('submit')

    def validate_login(self, login):
        if len(login.data) >= 255:
            raise ValidationError(1)
        elif len(login.data) < 3:
            raise ValidationError(1)
        elif ' ' in login.data:
            raise ValidationError(2)

    def validate_password(self, password):
        if len(password.data) >= 255:
            raise ValidationError(1)
        elif len(password.data) < 4:
            raise ValidationError(1)


class LoginForm(FlaskForm):
    login = StringField('login', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('submit')

    def validate_login(self, login):
        if len(login.data) >= 255:
            raise ValidationError(1)
        elif len(login.data) < 3:
            raise ValidationError(2)
        elif ' ' in login.data:
            raise ValidationError(3)

    def validate_password(self, password):
        if len(password.data) >= 255:
            raise ValidationError(1)
        elif len(password.data) < 3:
            raise ValidationError(2)
        elif ' ' in password.data:
            raise ValidationError(3)


class PlanForm(FlaskForm):
    pf1 = BooleanField()
    pf2 = BooleanField()
    pf3 = BooleanField()
    pf4 = BooleanField()
    pf5 = BooleanField()
    pf6 = BooleanField()
    pf7 = BooleanField()
    pf8 = BooleanField()
    pf9 = BooleanField()
    pf10 = BooleanField()
    pf11 = BooleanField()
    pf12 = BooleanField()
    pf13 = BooleanField()
    pf14 = BooleanField()
    pf15 = BooleanField()
    pf16 = BooleanField()
    pf17 = BooleanField()
    pf18 = BooleanField()
    pf19 = BooleanField()
    pf20 = BooleanField()
    pf21 = BooleanField()
    pf22 = BooleanField()
    pf23 = BooleanField()
    pf24 = BooleanField()
    pf25 = BooleanField()
    pf26 = BooleanField()
    pf27 = BooleanField()
    submit = SubmitField('')

    labels_container = {
        'ru1': '[m]Как работает язык и чем отличается от других',
        'ru2': '[m]Синтаксис',
        'ru3': '[m]Типы данных и операции с ними',
        'ru4': '[s]Числа',
        'ru5': '[s]Строки',
        'ru6': '[s]Списки',
        'ru7': '[s]Кортежи',
        'ru8': '[s]Словари',
        'ru9': '[s]Множества',
        'ru10': '[s]Логический тип ',
        'ru11': '[m]Ветвления и циклы',
        'ru12': '[s]Условные операторы',
        'ru13': '[s]Проверка условий - if else',
        'ru14': '[s]Цикл while',
        'ru15': '[s]Цикл for',
        'ru16': '[s]Исключения',
        'ru17': '[m]Фунции',
        'ru18': '[s]Как работают функции',
        'ru19': '[s]Аргументы',
        'ru20': '[s]Итерации и итераторы',
        'ru21': '[s]Генераторы',
        'ru22': '[m]Модули',
        'ru23': '[m]ООП',
        'ru24': '[s]Классы и объекты',
        'ru25': '[s]Подклассы',
        'ru26': "[s]'Магические' функции'",
        'ru27': '[s]Декораторы'
    }

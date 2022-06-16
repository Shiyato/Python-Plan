from sqlalchemy import ForeignKey
from flask_login import UserMixin
from init import db


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=True, nullable=False)


class Plan(db.Model, UserMixin):
    __tablename__ = "plan"
    id = db.Column(db.Integer, primary_key=True)
    plan_numbers = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True)


def update_tables():
    db.metadata.drop_all(db.engine)
    db.metadata.create_all(db.engine)


def create_user(login:str, password:str):
    user = User(login=login, password=password)
    db.session.add(user)
    db.session.commit()


def create_plan(user_id:int, plan_numbers:str):
    plan = Plan(plan_numbers=plan_numbers, user_id=user_id)
    db.session.add(plan)
    db.session.commit()
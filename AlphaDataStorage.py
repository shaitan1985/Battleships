import os

from datetime import datetime
import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Query, scoped_session, sessionmaker


#################### setup ######################
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    __repr_attrs__ = ['name'] #отображение в результате запроса

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String)
    passw = sa.Column(sa.String)
    created_at = sa.Column(sa.DateTime, default=datetime.now())


class Game(Base):
    __tablename__ = 'game'
    __repr_attrs__ = ['frst_user', 'scnd_user', 'begining_date']

    id = sa.Column(sa.Integer, primary_key=True)
    user1_id = sa.Column(sa.Integer, sa.ForeignKey('user.id'))
    user2_id = sa.Column(sa.Integer, sa.ForeignKey('user.id'))
    begining_date = sa.Column(sa.DateTime, default=datetime.now())
    finished = sa.Column(sa.Boolean, default=False)

class Ship(Base):
    __tablename__ = 'ship'
    __repr_attrs__ = ['game_id', 'user_id', 'level']

    id = sa.Column(sa.Integer, primary_key=True)
    game_id = sa.Column(sa.Integer, sa.ForeignKey('game.id'))
    user_id = sa.Column(sa.Integer, sa.ForeignKey('user.id'))
    level = sa.Column(sa.Integer)
    coords = sa.Column(sa.String)
    killed = sa.Column(sa.Boolean, default=False)

class Action(Base):
    __tablename__ = 'action'
    __repr_attrs__ = ['game_id', 'user_id', 'shot_coord']

    id = sa.Column(sa.Integer, primary_key=True)
    game_id = sa.Column(sa.Integer, sa.ForeignKey('game.id'))
    user_id = sa.Column(sa.Integer, sa.ForeignKey('user.id'))
    shot_coord = sa.Column(sa.String)
    date = sa.Column(sa.DateTime, default=datetime.now())


#################### setup ORM ######################

db_file = os.path.join(os.path.dirname(__file__), 'db.sqlite')
engine = create_engine('sqlite:///{}'.format(db_file), echo=True)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

session = scoped_session(sessionmaker(bind=engine))

#################### setup some data ######################
uii = User(name='ii', passw='0000')
session.add(uii)
session.commit()


u1 = User(name='Vasya', passw='123')
session.add(u1)
session.commit()

u2 = User(name='Petya', passw='345')
session.add(u2)
session.commit()

game = Game(
    user1_id=u1.id,
    user2_id=u2.id
)

ship1 = Ship(
    game_id=game.id,
    user_id=u1.id,
    level=4
)


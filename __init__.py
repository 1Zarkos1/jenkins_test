# from flask import Flask, request, render_template
# from flask_uploads import IMAGES, UploadSet, configure_uploads

# app = Flask(__name__)
# app.config['UPLOADED_PHOTOS_DEST'] = 'uploads/'
# app.app_context().push()

# photos = UploadSet('photos', IMAGES)
# configure_uploads(app, (photos,))

# print('furter import')

# @app.route('/', methods=["POST", "GET"])
# def some():
#     if request.method == 'POST':
#         filename = photos.save(request.files['try'])
#     return render_template('index.html')

# print('after decorator')
#%%
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, create_engine, Table
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.sql.schema import MetaData

eng = create_engine('sqlite:///edx.db', echo=True)
metadata = MetaData(bind=eng)

movie = Table('Movie', metadata, autoload=True)


# class User(Base):
#     __tablename__ = 'user name'

#     id = Column(Integer, primary_key=True)
#     name = Column(String(50), nullable=False)
#     email = Column(String(50))

# Base.metadata.create_all(eng)

# sus = User(name='Susan', email='sus@gmail.com')

#%%
from sqlalchemy.sql import select

s = eng.execute(movie.select().where(movie.c.mID==101)).fetchone()
# %%
s.mID
# %%
session.query(User).all()[0].name
# %%

# %%
import hashlib

str(hashlib.sha224())
# %%
from werkzeug.security import generate_password_hash

generate_password_hash('some')
# %%
JENKINS_URL/job/test-project/build?token=TOKEN_NAME
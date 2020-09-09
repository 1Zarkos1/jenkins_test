import datetime

from flask import Flask, render_template, request
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime

engine = create_engine('sqlite:///exm.db')
db_session = scoped_session(sessionmaker(bind=engine, autocommit=False, 
                                         autoflush=False))
Base = declarative_base(bind=engine)
Base.query = db_session.query_property()

class Task(Base):

    __tablename__ = 'task'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    date_due = Column(DateTime)
    date_completed = Column(DateTime)
    description = Column(String)

    def __repr__(self):
        return f'Task - №{id}'

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def show_tasks():
    if request.method == 'POST':
        f = request.form
        date_t = datetime.datetime.strptime(f['date_d'], '%Y-%m-%d')
        t = Task(title=f['title'], date_due=date_t, description=f['desc'])
        db_session.add(t)
        db_session.commit()
        db_session.remove()
    query = Task.query
    result = query.all()
    return render_template('index.html', result=result)
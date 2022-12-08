from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
db = SQLAlchemy(app)


class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(80), unique=True, nullable=False)
    done = db.Column(db.String(120), unique=True, nullable=False)

    def repr(self):
        return f"Todo('{self.id}','{self.label}', '{self.done}')"

    def serialize(self):
        return {
            "id": self.id,
            "label": self.label,
            "done": self.done,
        }
        #return f"Todo('{self.id}','{self.label}', '{self.done}')"
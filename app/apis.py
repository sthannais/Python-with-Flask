from app import app
from flask import Flask, jsonify, request, Blueprint
from .models import db, Todo

@app.route('/todo', methods=['GET'])
def getTodo():
   result = Todo.query.all()
   data = list(map(lambda dataTodo: dataTodo.serialize(), result))
   return jsonify(data), 200

@app.route('/todo', methods=['POST'])
def saveTodo():
   data_request = request.get_json()
   result = Todo(label=data_request['label'],done=data_request['done'])
   db.session.add(result)
   db.session.commit()
   return jsonify("Todo creado de forma exitosa"), 200

@app.route('/todo/<int:id>', methods=['DELETE'])
def deleteTodo(id):
   todo = Todo.query.filter_by(id=id).first()
   if not todo:
      return jsonify({'message': 'Id not found'})
   db.session.delete(todo)
   db.session.commit()
   return jsonify({'message': 'The todo has been deleted'})
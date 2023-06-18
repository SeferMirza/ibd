from pathlib import Path

from jsonschema import validate
import sys, json

path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

from flask import Flask, jsonify, request
from db.Store import DB, DataNotFoundException
from . import schemas

class API:
   def __init__(self):
      self.app = Flask(__name__)
      dbName = "test"
      self.__dbContext = DB(dbName)

      # Routes
      self.app.route('/worklog/all', methods=['GET'])(self.getAllLog)
      self.app.route('/worklog/remove/<int:id>', methods=['DELETE'])(self.removeLog)
      self.app.route('/worklog/<int:id>', methods=['GET'])(self.getById)
      self.app.route('/worklog/customer/<customer>', methods=['GET'])(self.getByCustomer)
      self.app.route('/worklog/work/<work>', methods=['GET'])(self.getByWork)
      self.app.route('/worklog/<int:id>', methods=['PUT'])(self.update)
      self.app.route('/worklog/new', methods=['POST'])(self.add)

   def getAllLog(self):
      return jsonify({})

   def removeLog(self, id):
      try:
         popedItem = self.__dbContext.remove(id)
         self.__dbContext.save()
         return popedItem
      except DataNotFoundException as d:
         return jsonify({'error': str(d)}), 500

   def getById(self, id):
      return jsonify(self.__dbContext.getById(id))

   def getByCustomer(self, customer):
      return jsonify(self.__dbContext.getByObject({"müşteri": customer}))

   def getByWork(self, work):
      return jsonify(self.__dbContext.getByObject({"work": work}))

   def update(self, id):
      return jsonify(self.__dbContext.update(id, json.loads(request.data)))

   def add(self):
      try:
         validate(instance=json.loads(request.data), schema=schemas.task)
         return jsonify(self.__dbContext.getAll())
      except Exception as t:
         return jsonify({'error': str(t)}), 500

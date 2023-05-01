from flask import Flask, jsonify, request
from datetime import datetime
from pathlib import Path

import sys, json
path_root = Path(__file__).parents[1]
print(path_root)
sys.path.append(str(path_root))

from db.Store import DB

api = Flask(__name__)
dbName = "test"

dbContext = DB(dbName)

# Routes
@api.route('/worklog/all', methods=['GET'])
def getAllLog():
   return jsonify(dbContext.getAll())

@api.route('/worklog/remove/<int:id>', methods=['DELETE'])
def removeLog(id):
   popedItem = dbContext.remove(id)
   dbContext.save()
   return popedItem

@api.route('/worklog/<int:id>', methods=['GET'])
def getById(id):
   return jsonify(dbContext.getById(id))

@api.route('/worklog/customer/<customer>', methods=['GET'])
def getByCustomer(customer):
   return jsonify(dbContext.getByObject({
      "müşteri": customer
   }))

@api.route('/worklog/work/<string:work>', methods=['GET'])
def getByWork(work):
   return jsonify(dbContext.getAll())

@api.route('/worklog/<int:id>', methods=['PUT'])
def update(id):
   return jsonify(dbContext.getAll())

@api.route('/worklog/new', methods=['POST'])
def add():
   dbContext.add(datetime.now(), json.loads(request.data))
   dbContext.save()
   return request.data

if __name__ == '__main__':
   api.debug = True
   api.run() #go to http://localhost:5000/ to view the page.
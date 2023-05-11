from datetime import datetime
from pathlib import Path

import sys, json
path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

from flask import Flask, jsonify, request
from db.Store import DB
class API:
    def __init__(self):
        self.app = Flask(__name__)
        dbName = "test"

        dbContext = DB(dbName)

        # Routes
        @self.app.route('/worklog/all', methods=['GET'])
        def getAllLog():
           return jsonify(dbContext.getAll())

        @self.app.route('/worklog/remove/<int:id>', methods=['DELETE'])
        def removeLog(id):
           popedItem = dbContext.remove(id)
           dbContext.save()
           return popedItem

        @self.app.route('/worklog/<int:id>', methods=['GET'])
        def getById(id):
           return jsonify(dbContext.getById(id))

        @self.app.route('/worklog/customer/<customer>', methods=['GET'])
        def getByCustomer(customer):
           return jsonify(dbContext.getByObject({
              "müşteri": customer
           }))

        @self.app.route('/worklog/work/<work>', methods=['GET'])
        def getByWork(work):
           return jsonify(dbContext.getByObject({
              "work": work
           }))

        @self.app.route('/worklog/<int:id>', methods=['PUT'])
        def update(id):
           return jsonify(dbContext.update(id, json.loads(request.data)))

        @self.app.route('/worklog/new', methods=['POST'])
        def add():
           dbContext.add(datetime.now(), json.loads(request.data))
           dbContext.save()
           return request.data
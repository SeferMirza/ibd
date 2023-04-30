from flask import Flask, jsonify
from datetime import datetime
from pathlib import Path
import sys
path_root = Path(__file__).parents[1]
print(path_root)
sys.path.append(str(path_root))
from db.Store import DB

api = Flask(__name__)
dbName = "test"

dbContext = DB(dbName)
dbContext.Add(datetime.now(), {"sefer": "mirza"})

@api.route('/log/<int:Number>', methods=['GET'])
def get_log(Number):
   dbContext.Save()
   return jsonify(dbContext.context)

if __name__ == '__main__':
   api.debug = True
   api.run() #go to http://localhost:5000/ to view the page.
from flask import Flask, jsonify

api = Flask(__name__)

@api.route('/log/<int:Number>', methods=['GET'])
def get_log(Number):
    return jsonify({'name': 'alice',
                       'email': 'alice@outlook.com',
                       'Number': Number})

if __name__ == '__main__':
    api.debug = True
    api.run() #go to http://localhost:5000/ to view the page.
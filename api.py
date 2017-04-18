#!flask/bin/python
import json
from flask import Flask, jsonify, abort, make_response, request
import demotank

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'not found'}), 404)

@app.route('/api/tanks', methods=['GET'])
def get_tanks():
    '''Example: curl -i http://localhost:5000/api/tanks'''
    with open('simtanks.json', 'r') as jfile:
        tanks = json.load(jfile)
    
    return jsonify({'tanks': tanks})

@app.route('/api/tank/fill/', methods=['GET'])
def fill_tank():
    '''Example: curl -i http://localhost:5000/api/tank/fill/?id=01&amt=50'''
    # args = request.args
    # print(args) # For debugging
    arg1 = request.args.get('id')
    arg2 = request.args.get('amt')
    dtank = demotank.DemoTank()
    dtank.fillsimtank(int(str(arg1)), int(str(arg2)))   #send int values to fillsimtank function
    #TODO: Format return json to something more useful that indicates result
    return jsonify(dict(data=[arg1, arg2])) # or whatever is required

@app.route('/api/tanks/<string:tank_id>', methods=['GET'])
def get_tank(tank_id):
    '''Example: curl -i http://localhost:5000/api/tanks/s02'''
    with open('simtanks.json', 'r') as jfile:
        tanks = json.load(jfile)
    try:
        tank = tanks[str(tank_id).upper()][0]
    except KeyError:
        return jsonify({'error': 'invalid key request'})
    if len(tank) == 0:
        abort(404)
    
    return jsonify(tank)

if __name__ == '__main__':
    app.run(debug=True)

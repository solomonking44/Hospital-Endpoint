from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import json

#creating the flask app
app = Flask(__name__)

#creating API
api = Api(app)

#routing to home page
@app.route('/')
def home():
    return render_template('index.html')

#grand oak resource
class GrandOak(Resource):
    def get(self):
        return GRAND_OAKS
            
#pine valley resource            
class PineValley(Resource):
    def get(self):
        return PINE_VALLEY

#adding resources to the API
api.add_resource(GrandOak, '/grandoak')
api.add_resource(PineValley, '/pinevalley')

#grand oaks data source
grandoak = open('grandoak.json')
GRAND_OAKS = json.load(grandoak)

#pine valley data source
pinevalley = open('pinevalley.json')
PINE_VALLEY = json.load(pinevalley)


if __name__ == '__main__':
    app.run(debug=True)


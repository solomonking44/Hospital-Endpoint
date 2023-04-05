from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import json
from xml.dom import minidom

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
#xml resource
class XmlFile(Resource):
    def get(self):
        return xml_data

#adding resources to the API
api.add_resource(GrandOak, '/grandoak')
api.add_resource(PineValley, '/pinevalley')
api.add_resource(XmlFile, '/xmlfile')

#grand oaks data source
grandoak = open('grandoak.json')
GRAND_OAKS = json.load(grandoak)

#pine valley data source
pinevalley = open('pinevalley.json')
PINE_VALLEY = json.load(pinevalley)

#importing xml file
#xml_file = minidom.parse('file.xml')
#getting elementbytag
#xml_data = xml_file.getElementsByTagName('request')

if __name__ == '__main__':
    app.run(debug=True)


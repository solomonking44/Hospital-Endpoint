from flask import Flask, request, jsonify, render_template
from flask_restful import Api, Resource
import json
#from xml.dom import minidom

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
#class XmlFile(Resource):
 #   def get(self):
  #      return XML_DATA

#data mapper json
class DataMapper(Resource):
    def get(self):
        return DATA_MAPPER_INPUT


#all hospital records of doctors
class Hospital(Resource):
    def get(self):
        return HOSPITAL_RECORDS

#complex data mapper scenario
class DataMapperComplex(Resource):
    def get(self):
        return DATA_MAPPER_COMPLEX

#adding resources to the API
api.add_resource(GrandOak, '/grandoak')
api.add_resource(PineValley, '/pinevalley')
#api.add_resource(XmlFile, '/xmlfile')
api.add_resource(DataMapper, '/datamapper')
api.add_resource(Hospital, '/hospital')
api.add_resource(DataMapperComplex, '/datamappercomplex')

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


#data mapper json input
data_mapper_input = open('dataMapperInput.json')
DATA_MAPPER_INPUT = json.load(data_mapper_input)

#hospital json file
hospital_file = open('hospital.json')
HOSPITAL_RECORDS = json.load(hospital_file)

#data mapper complex file
data_mapper_complex = open('jsonFileTest.json')
DATA_MAPPER_COMPLEX = json.load(data_mapper_complex)

if __name__ == '__main__':
    app.run(debug=True)


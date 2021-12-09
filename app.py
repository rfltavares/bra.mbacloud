import os

from flask import Flask, json, jsonify



app = Flask(__name__)



@app.route('/')

def home():

   filename = os.path.join(app.static_folder, 'infos.json')

   with open(filename) as test_file:

     data = json.load(test_file)



   return jsonify(data)



if __name__ == '__main__':

 app.run()
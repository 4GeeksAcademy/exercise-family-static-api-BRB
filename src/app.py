"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_hello():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {
        "message": "member added successfully",
        "family": members
    }


    return jsonify(response_body), 200



# GET /member/<int:member_id>
@app.route('/member', methods=['GET'])
def get_member():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_member()
    # response_body = {
    #     "message": "member received successfully",
    #     "family": members
    # }


    return jsonify(members), 200


@app.route('/members', methods=['POST'])
def add_member():
    body = request.json
    members = jackson_family.add_member(body)
    print(body, "here is bodyyy!!")
    return jsonify("member added successfully"), 200

 

# POST /member

# REQUEST BODY (content_type: application/json):
# {
#         id: Int,
#         first_name: String,
#         age: Int,
#         lucky_numbers: []
# }

# RESPONSE (content_type: application/json):

# status_code: 200 if success. 400 if a bad request (wrong info). 500 if the server encounters an error

# # this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)

from flask import Flask, request, Response
import mariadb
import dbcreds
import json

app = Flask(__name__)
animals = ["Panda", "Koala bear", "Tiger", "Cheetah", "Grizzly Bear"]
@app.route('/animals', methods =["GET", "POST", "PATCH", "DELETE"])
def animals():
    if request.method == "GET":
      return Response(json.dumps(animals, default=str), mimetype="application/json", status=200)
    elif request.method == "POST": 
          return Response("Elk Inserted Successfully!", mimetype="text/html", status=201)
    elif request.method == "PATCH":
          return Response("Changed 'tiger' to 'Lion' successfully", mimetype="text/html", status=204)
    elif request.method == "DELETE":
          return Response("Deleted 'Grizzly bear' successfully ", mimetype="text/html", status=204)
    else:
          return Response("Error has occured! ", mimetype="text/html", status=500)

from gevent import monkey;
monkey.patch_all()
from flask import Flask, Response, request,jsonify, make_response
from flask_restful import Api
from routes.route import initialize_routes

app=Flask(__name__)


api=Api(app)
initialize_routes(api)

if __name__ == "__main__":
    app.run()
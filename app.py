from flask import Flask,jsonify
from imagesearch.scraper import fetch_image_urls
app = Flask(__name__)
@app.route("/<string:query>/<int:num>")
def imagesearchhandler(query,num):
    try:
        query = str(query)
        quantity = int(num)
    except Exception as err:
        print(err)
        error = {"error":"Invalid parametres"}
        return jsonify(error)
    try:
        images = list(fetch_image_urls(query,quantity))
        response = {"images":images}
        return jsonify(response)
    except Exception as err:
        print(err)
        error = {"error":"failed to get image"}
        return jsonify(error)






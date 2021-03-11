import requests
from flask import Flask, jsonify, request
from detect import detect_filetype

app = Flask(__name__)


# Default view with instructions on use
@app.route('/')
def default():
    return jsonify({
        'error': 'To check catalogue file format, enter localhost:5000/evaluate/?= followed by url source.'
    }), 400


# URL evaluation view
@app.route('/evaluate/')
# fetch link as argument, if not found return "incomplete" error message
def catalog_type():
    link = request.args.get('link')
    if not link:
        return jsonify({
            "incomplete": "Add ?link= followed by catalogue url to make the detection."
        }), 400

    try:
        extension = detect_filetype(link)

        return jsonify({
            "url": link,
            "format": extension
        }), 200

    except requests.RequestException:
        return jsonify({
            "url": link,
            "error": "File format unknown or unrecognizable."
        }), 400

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
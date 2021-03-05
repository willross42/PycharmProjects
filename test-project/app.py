import requests
from flask import Flask, request, jsonify
import detect

app = Flask(__name__)


@app.route('/api/v1/catalog-type')
def catalog_type():
    source = request.args.get('source')
    if not source:
        return jsonify({
            "error": "Please, add the parameter source to make the detection."
        }), 400

    try:
        format = detect_catalog_type(source)
        if format is None:
            return jsonify({
                "url": source,
                "error": "File format unknown or not recognizable.",
            })
        else:
            return jsonify({
                "url": source,
                "format": format,
            })
    except requests.RequestException:
        return jsonify({
            "url": source,
            "error": "Couldn't download the file from the given source.",
        })


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
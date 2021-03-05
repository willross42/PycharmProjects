from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def default():
    return jsonify({
        'error': 'To check catalogue file format, enter /evaluate/ followed by url.'
    }), 400

@app.route('/evaluate/<url>')
def evaluate(url):
    lenurl = len(url)
    end_of_url = url[lenurl -3:lenurl]
    return jsonify({
        "extension": end_of_url
    }), 400

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

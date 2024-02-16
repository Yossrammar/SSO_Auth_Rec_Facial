from flask import *
#Flask, request,jsonify
app = Flask(__name__)

@app.route('/api',methode=['GET'])
def home():
    Query=str(request.args['Query'])
    return Query

if __name__=="__main__":
    app.run(debug=True)
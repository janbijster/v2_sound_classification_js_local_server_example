from flask import Flask, request #import main Flask class and request object

app = Flask(__name__) #create the Flask app

@app.route('/data', methods=['POST']) #GET requests will be blocked
def json_example():
    req_data = request.get_json()

    # do something with the data...
    print(req_data)

    # return confirmation
    return 'Data received.'

if __name__ == '__main__':
    app.run(debug=True, port=5000) #run app in debug mode on port 5000
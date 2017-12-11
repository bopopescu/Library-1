from flask import Flask


testapp = Flask(__name__)

@testapp.route('/')
def testflask():
    return "It's working"

if __name__  == '__main__':
    testapp.run(debug=True)





# Importing the Flask module is mandatory.
# An object of the Flask class represents our WSGI application.
from flask import Flask

# Create an instance of the Flask class, using the __name__ of the script file.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call the associated function.
@app.route('/')
# The '/' URL is bound to the `hello_world()` function.
def hello_world():
    return 'Hello, World!'

# Main driver function
if __name__ == '__main__':
    # The `run()` method of the Flask class runs the application
    # on the local development server.
    app.run(host="0.0.0.0")

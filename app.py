# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Hello, World!"

# if __name__ == "__main__":
#     app.run(debug=True)  
# #creating a simple hello world 

# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("index.html")

# if __name__ == "__main__":
#     app.run(debug=True)
# #  Adding HTML Templates

# from flask import Flask, render_template, jsonify
# import requests

# app = Flask(__name__)

# @app.route("/")
# def home():
#     # Fetch data from a sample API
#     response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
#     data = response.json()
#     return jsonify(data)  # Sends JSON directly

# if __name__ == "__main__":
#     app.run(debug=True)
# # Fetching an External API in Flask

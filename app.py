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

# from flask import Flask, render_template
# import requests

# app = Flask(__name__)

# @app.route("/")
# def home():
#     response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
#     data = response.json()
#     return render_template("api.html", todo=data)

# if __name__ == "__main__":
#     app.run(debug=True)
# # Showing API Data in HTML

# Multiple pages
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "This is Home Page"

@app.route("/about")
def about():
    return "This is About Page"

@app.route("/contact")
def contact():
    return "This is Contact Page"

if __name__ == "__main__":
    app.run(debug=True)

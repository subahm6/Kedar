from flask import Flask, render_template, request, jsonify
import json


#mongodb_client = MongoClient(host="localhost:27017", connect=True)
#database = mongodb_client["admin"]
#collection = database.get_collection("user_credentials")









app = Flask(__name__)

@app.route('/')
def index():
    return render_template("main.html")

@app.route("/login_Page")
def login_page():
    return render_template("login.html")

#@app.route('/login', methods=['POST'])
#def login():
#    data = request.get_json()
#    username = data.get('username')
#    password = data.get('password')
#
 #   dataset=  get_data(collection=collection,user=username,passw=password)
#
 #   # Here you would normally validate the credentials with your user database
  #  if dataset == True :
   #     return jsonify({'message': 'Login successful'}), 200
    #else:
     #   return jsonify({'message': 'Invalid credentials'}), 401
    
@app.route("/contact_page")
def contact_page():
    return render_template("contact.html")

@app.route("/register_page")
def register_page():
    return render_template("register.html")

#@app.route('/regisdata', methods=['POST'])
#def regisdata():
 #   
  #      data = request.get_json()
   #     
#
 #       username = data.get('mail')
  #      password = data.get('pass')
#
 #       user_data = {
  #          "user": username,
   #         "pass": password
    #    } 
    #    startup_db_client(collection=collection,document=user_data)

     #   return jsonify({"message": "Data saved successfully"}), 200

@app.route("/service_page")
def service_page():
    return render_template("service.html")

    


if __name__ == "__main__":
    app.run(host="127.0.0.1",debug=True,port=80)

    


if __name__ == "__main__":
    app.run(host="127.0.0.1",debug=True,port=80)

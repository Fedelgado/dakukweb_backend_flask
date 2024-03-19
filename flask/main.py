from flask import Flask, jsonify, request, render_template
from markupsafe import escape

app = Flask(__name__)
@app.route('/')

def root():
    return "<p>HELLO WORLD</p>"

@app.route('/users/<user_id>')
def get_user(user_id):
    user = {'id':user_id,'name':"test", 'phone':"222-222-5124"}
    #users/2654?query=query_test
    query = request.args.get("query")
    if query:
        user["query"] = query
    return jsonify(user), 200   

@app.route('/user/<name>')
def greet(name):
    return "Bienvenido " + name + ", sos un usuario!!!"

@app.route('/user/<name>/Dashboard')
def dshBrd(name):
    return "Aca vas a poder ver todas las cosas divertidas que tengas "+ name +""

@app.route('/user/<name>/escapate')
def asde(name):
    return f"ESCAPATE!!{escape(name)}"
    
@app.route('/users', methods=["POST"])
def create_user():
    data = request.get_json()
    data["status"] = "user created"
    return jsonify(data), 201

""" @app.route('/penes')
def penecito():
    return '<h1>TU PENE ESTÁ BIEN</h1>'
"""   

@app.route('/index')
def showindex():
    return render_template('../resources/views/welcome.blade.php')

if __name__ == '__main__':
    app.run(debug=True)

# flask --app <name> run 
# if wanted, use "--debug" after run 
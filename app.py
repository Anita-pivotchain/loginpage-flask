from flask import Flask,request,jsonify

         
app = Flask(__name__)
# @app.route('/')
# def hello():
#     print("hello")

data = {'Anita':'abc','aaa':'eeefe','sdscsd':'scas'}  
@app.route('/test',methods=['GET','POST'])
def test(): 
    
    if request.method=="GET":
        return jsonify({"Response":"Get Request called"})
    elif request.method=="POST":
        req_json=request.json
        name = req_json['name']
        psw = req_json['psw']
        if name not in data:
            return jsonify({"Response":"Invalid user"})
        else :
             if data[name]!=psw :
                return jsonify({"Response":"Invalide User"})  
             else:
                return jsonify({"Response":"Valid user"})   

if __name__=="__main__":
    app.run(debug=True)    



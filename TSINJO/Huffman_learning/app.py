from flask import Flask, request,render_template,url_for,jsonify,json,session,redirect
from service import predire, apprendre

app = Flask(__name__)
app.secret_key = '06112003'

reponse = {True:'code',False:'Not a code'}


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sardinas-patterson',methods=['POST'])
def sardinas():
    data = request.get_json()
    code = data.get('code')
    val,sard = predire(code)
    return {'sardinas':reponse[sard], 'learning':reponse[val]}

@app.route('/learn',methods=['GET'])
def apprend():
    apprendre()
    return {'message':'reussi'}, 200



















if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
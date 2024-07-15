from projet import app
from flask import render_template, redirect, url_for, session, request, make_response, jsonify
from projet.annotation.authentication import auth
from flask_weasyprint import HTML
import csv
from io import StringIO, BytesIO
from openpyxl import Workbook


@app.route('/', methods = ['GET'])
def index():
    return redirect(url_for('login_client'))

@app.route('/page', methods = ['GET'])
def page():
    return render_template('page/page.html')

@app.route('/datatable', methods = ['GET'])
def datatable():
    return render_template('page/datable.html')


@app.route('/testupload', methods = ['GET'])
def testupload():
    return render_template('page/form-upload.html')

@app.route('/upload', methods = ['POST'])
def upload():
    if 'fichier' not in request.files:
        return 'Aucun fichier envoyé'
    fichier = request.files['fichier']

    if fichier.filename == '':
        return 'Nom de fichier vide'
    if fichier:
        fichier.save('projet/static/image/upload/' + fichier.filename)
        return 'Fichier uploadé avec succès'

@app.route('/getdata', methods = ['POST'])
def getdata():
    form = request.form
    print(form)
    size = int(form.get('size'))
    page = int(form.get('page'))
    tri_col = form.get('tri')
    print(tri_col)
    data = [
    {'nom':'Jeremia','prenom':'Rafa','id':5,'age':16.5,'annee':2023,'asa':'Mpivarotra'},
    {'nom':'John','prenom':'Doe','id':8,'age':18,'annee':2024,'asa':'Tsara'},
    {'nom':'Alice','prenom':'Smith','id':12,'age':19,'annee':2021,'asa':'Mahay'},
    {'nom':'Bob','prenom':'Johnson','id':15,'age':17.5,'annee':2022,'asa':'Manga'},
    {'nom':'Emma','prenom':'Brown','id':20,'age':20,'annee':2025,'asa':'Miafy'},
    {'nom':'Mark','prenom':'Wilson','id':22,'age':21,'annee':2026,'asa':'Mitafy'},
    {'nom':'Ella','prenom':'Davis','id':27,'age':22,'annee':2027,'asa':'Mibaila'},
    {'nom':'Chris','prenom':'Martinez','id':31,'age':23,'annee':2028,'asa':'Mipandry'},
    {'nom':'Sophia','prenom':'Hernandez','id':35,'age':24,'annee':2029,'asa':'Mandry'},
    {'nom':'William','prenom':'Lopez','id':38,'age':25,'annee':2030,'asa':'Mividy'},
    {'nom':'Olivia','prenom':'Gonzalez','id':40,'age':26,'annee':2031,'asa':'Mividy'},
    {'nom':'Michael','prenom':'Rodriguez','id':41,'age':27,'annee':2032,'asa':'Mianatra'},
    {'nom':'Alexis','prenom':'Wilson','id':43,'age':28,'annee':2033,'asa':'Mifandray'},
    {'nom':'Matthew','prenom':'King','id':45,'age':29,'annee':2034,'asa':'Mikatona'},
    {'nom':'Isabella','prenom':'Taylor','id':46,'age':30,'annee':2035,'asa':'Mikatona'},
    {'nom':'Andrew','prenom':'Anderson','id':47,'age':31,'annee':2036,'asa':'Mikatona'},
    {'nom':'Emily','prenom':'Thomas','id':49,'age':32,'annee':2037,'asa':'Mikatona'},
    {'nom':'Benjamin','prenom':'Moore','id':50,'age':33,'annee':2038,'asa':'Mikatona'},
    {'nom':'Madison','prenom':'Jackson','id':52,'age':34,'annee':2039,'asa':'Mikatona'},
    {'nom':'Avery','prenom':'White','id':55,'age':35,'annee':2040,'asa':'Mikatona'},
    {'nom':'Daniel','prenom':'Harris','id':57,'age':36,'annee':2041,'asa':'Mikatona'},
    {'nom':'Mia','prenom':'Brown','id':58,'age':37,'annee':2042,'asa':'Mikatona'},
    {'nom':'Jacob','prenom':'Evans','id':59,'age':38,'annee':2043,'asa':'Mikatona'},
    {'nom':'Chloe','prenom':'Allen','id':61,'age':39,'annee':2044,'asa':'Mikatona'},
    {'nom':'Gabriel','prenom':'Miller','id':63,'age':40,'annee':2045,'asa':'Mikatona'},
    {'nom':'Evelyn','prenom':'Thompson','id':65,'age':41,'annee':2046,'asa':'Mikatona'},
    {'nom':'Nicholas','prenom':'Garcia','id':67,'age':42,'annee':2047,'asa':'Mikatona'},
    {'nom':'Ava','prenom':'Lee','id':69,'age':43,'annee':2048,'asa':'Mikatona'},
    {'nom':'Hannah','prenom':'Phillips','id':71,'age':44,'annee':2049,'asa':'Mikatona'},
    {'nom':'Samuel','prenom':'Scott','id':73,'age':45,'annee':2050,'asa':'Mikatona'},
    {'nom':'Elizabeth','prenom':'Perez','id':75,'age':46,'annee':2051,'asa':'Mikatona'},
    {'nom':'Liam','prenom':'Walker','id':77,'age':47,'annee':2052,'asa':'Mikatona'},
    {'nom':'Aiden','prenom':'Hill','id':79,'age':48,'annee':2053,'asa':'Mikatona'},
    {'nom':'Natalie','prenom':'Roberts','id':81,'age':49,'annee':2054,'asa':'Mikatona'},
    {'nom':'Lily','prenom':'Morris','id':83,'age':50,'annee':2055,'asa':'Mikatona'}
]
    if tri_col != 'null' and tri_col!='undefined':
        data = sorted(data, key=lambda x: x[tri_col])

    ind1 = (page-1)*size
    ind2 = ind1 + size
    return {'data':data[ind1:ind2]}, 200


# @app.route('/login', methods = ['GET'])
# def login():
#     session['user'] = {'username': "Jeremia", 'roles': ['USER']}
#     return {'message':'connected'}, 200

@app.route('/pdf', methods = ['GET'])
def getpdf():
    # Récupérer le contenu HTML à partir d'un template
    html_content = render_template('page/monpdf.html', data={'name': 'John Doe', 'age': 30})
    # Convertir le contenu HTML en PDF avec WeasyPrint
    pdf = HTML(string=html_content).write_pdf()
    # Créer une réponse Flask pour le fichier PDF généré
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachement; filename=example.pdf'
    return response

def generate_csv_data():
    data = [
        ['Nom', 'Âge', 'Ville'],
        ['John Doe', 30, 'New York'],
        ['Jane Smith', 25, 'Los Angeles']
    ]
    return data

@app.route('/csv', methods = ['GET'])
def getcsv():
    data = generate_csv_data()

    csv_data = StringIO()
    csv_writer = csv.writer(csv_data)
    csv_writer.writerows(data)

    response = make_response(csv_data.getvalue())
    response.headers['Content-Type'] = 'text/csv'
    response.headers['Content-Disposition'] = 'attachment; filename=data.csv'

    return response

# @app.route('/first', methods = ['GET'])
# def first():
#     data = generate_csv_data()

#     csv_data = StringIO()
#     csv_writer = csv.writer(csv_data)
#     csv_writer.writerows(data)
#     return redirect(url_for('download'))

@app.route('/excel', methods = ['GET'])
def getexcel():
    data = generate_csv_data()

    wb = Workbook()
    ws = wb.active

    for row in data:
        ws.append(row)

    excel_data = BytesIO()
    wb.save(excel_data)

    # Créer une réponse Flask pour le fichier Excel généré
    response = make_response(excel_data.getvalue())
    response.headers['Content-Type'] = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    response.headers['Content-Disposition'] = 'attachment; filename=data.xlsx'


    return response

# content  = {
#     'pdf':'application/pdf',
#     'csv':'text/csv',
#     'xlsx':'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
# }

# @app.route('/download-file', methods = ['GET'])
# def download():
#     print(request.get_json())
#     data = ''
#     extension = ''
#     filename = ''

#     response = make_response(data)
#     response.headers['Content-Type'] = content[extension]
#     response.headers['Content-Disposition'] = f'attachment; filename={filename}.{extension}'


#     return {'message':'test'}, 200



# class MoiController:
#     @classmethod
#     def salut(cls):
#         return render_template('page-login.html')

# class ToiController:
#     a = 5

#     @classmethod
#     def salut(cls):
#         c = ToiController.a
#         ToiController.a = c + 5
#         print(c)
#         return render_template('page-login.html')

#     @classmethod
#     @app.route('/court', methods=['GET'])
#     def court():
#         return redirect(url_for('test_quoi'))


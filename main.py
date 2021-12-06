import os
import io
from flask import Flask, flash, request, send_file, Response
from flask_restful import Api
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename, safe_join
import ocrmypdf
import warnings

warnings.filterwarnings("ignore")

dirbase = os.path.dirname(os.path.realpath(__file__))

if not os.path.exists(dirbase + '/uploads'):
    os.mkdir(dirbase + '/uploads')

if not os.path.exists(dirbase + '/save'):
    os.mkdir(dirbase + '/save')

UPLOAD_FOLDER = dirbase + '/uploads/'
SAVE_FOLDER = dirbase + '/save/'
ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__)
api = Api(app)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SAVE_FOLDER'] = SAVE_FOLDER
app.config['CORS_HEADERS'] = 'Content-Type'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/decode/', methods=['POST'])
@cross_origin(origin='*', headers=['Content- Type'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return Response('Não foi enviado arquivo para ser convertido', status = 401)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            return Response('Arquivo enviado não tem nome', status = 401)
        if not file.filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS:
            return Response('Arquivo enviado diferente de PDF', status = 401)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            try:
                ocrmypdf.ocr(UPLOAD_FOLDER + filename, 
                        SAVE_FOLDER + filename, 
                        deskew=False, 
                        progress_bar=True,
                        force_ocr=True
                        )
                
                if os.path.exists(UPLOAD_FOLDER + filename):
                    os.remove(UPLOAD_FOLDER + filename)
                    
                safe_path = safe_join(app.config["SAVE_FOLDER"], filename)
                
                contentDownload = io.BytesIO(open(safe_path, 'rb').read())
                
                return send_file(contentDownload, as_attachment=True, mimetype='Application/pdf', download_name=filename)
                    
            except:
                return Response('Erro na converção do arquivo enviado', status = 500) 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, threaded = True, debug=True)
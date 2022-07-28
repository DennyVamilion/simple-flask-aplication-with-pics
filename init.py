from flask import Flask, app, url_for ,request, send_file
from flask.templating import render_template
import os

app = Flask(__name__)

PicturesFolder = os.path.join('static', 'Pictures')
app.config['UPLOAD_FOLDER'] = PicturesFolder

@app.route('/')
def Home():
    Pic1 = os.path.join(app.config['UPLOAD_FOLDER'], 'ult.jpg')
    Pic2 = os.path.join(app.config['UPLOAD_FOLDER'], 'emag.jpg')
    Pic3 = os.path.join(app.config['UPLOAD_FOLDER'], 'VTD.png')
    return render_template('Home.html', user_image1=Pic1, user_image2=Pic2, user_image3=Pic3)

@app.route('/Kontakte')
def Kontakte():
    discord = os.path.join(app.config['UPLOAD_FOLDER'], 'discord.png')
    instagram = os.path.join(app.config['UPLOAD_FOLDER'], 'instagram.png')
    twitch = os.path.join(app.config['UPLOAD_FOLDER'], 'twitch.png')
    yt = os.path.join(app.config['UPLOAD_FOLDER'], 'youtube.png')
    return render_template('Kontakte.html', user_imge1=discord, user_imge2=instagram, user_imge3=twitch, user_imge4=yt)
    
if __name__ == "__main__":
    app.run(port=5000, debug=True)
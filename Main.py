#realizzare un sito web in flask che permetta all'utente di avere una mappa di un quartiere con le fontalle. 
#L'utente seleziona da un menù a tendina il nome del quartiere, clicca sul bottone e ottiene la mappa del
#quartiere prescelto con le fontanelle presenti
from flask import Flask,render_template,request
import geopandas as gpd
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    
  
    return render_template("index.html")
    

@app.route('/map', methods=['GET'])
def map():
    
    fileContent = gpd.read_file("./fontanelle")
    return render_template("map.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
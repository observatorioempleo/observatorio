import pandas as pd
import feedparser
from flask import Flask, render_template, request
from datetime import datetime
from urllib.parse import quote
# Usar quote en lugar de url_quote
quoted_url = quote(url)

# Reemplaza url_quote con quote
quoted_url = quote(url)

import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)  # Asegúrate de que esté escuchando en el puerto 5000

#port = int(os.environ.get("PORT", 5000))  # Por defecto en 8080
#app.run(host="0.0.0.0", port=8000)


# Leer el archivo CSV con pandas
df = pd.read_csv('02_FUENTES_COMPLETAS.csv', delimiter=';')

app = Flask(__name__)

# Función para obtener noticias desde las RSS
def obtener_noticias():
    noticias = []
    seen_urls = set()  # Conjunto para rastrear URLs ya procesadas
    last_check_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Fecha de la última consulta

    # Iterar sobre las filas del DataFrame
    for index, row in df.iterrows():
        rss_url = row['RSS']
        rss_especifica = row['RSS_ESPECIFICA']
        
        # Usar feedparser para obtener noticias de las URLs RSS
        for url in [rss_url, rss_especifica]:
            if pd.notna(url):
                feed = feedparser.parse(url)
                for entry in feed.entries:
                    if 'link' in entry:
                        url_entry = entry.link
                        # Solo agregar la noticia si no se ha visto antes
                        if url_entry not in seen_urls:
                            seen_urls.add(url_entry)
                            noticia = {
                                'titulo': entry.title if 'title' in entry else '',
                                'fuente': row['FUENTE'] if pd.notna(row['FUENTE']) else '',
                                'ambito': row['AMBITO GEOGRAFICO'] if pd.notna(row['AMBITO GEOGRAFICO']) else '',
                                'agente': row['TIPO AGENTE'] if pd.notna(row['TIPO AGENTE']) else '',
                                'materia': row['MATERIA'] if pd.notna(row['MATERIA']) else '',
                                'url': url_entry,
                                'fecha_publicacion': entry.published if 'published' in entry else last_check_date
                            }
                            noticias.append(noticia)
    return noticias

# Ruta principal de la web
@app.route('/', methods=['GET', 'POST'])
def index():
    # Obtener todas las noticias
    noticias = obtener_noticias()
    
    # Obtener las opciones para los menús desplegables
    fuentes = df['FUENTE'].dropna().unique().tolist()
    ambitos = df['AMBITO GEOGRAFICO'].dropna().unique().tolist()
    agentes = df['TIPO AGENTE'].dropna().unique().tolist()
    materias = df['MATERIA'].dropna().unique().tolist()

    # Filtrar las noticias según los criterios de búsqueda si se ha enviado el formulario
    if request.method == 'POST':
        filtro_fuente = request.form.get('filtro-fuente')
        filtro_ambito = request.form.get('filtro-ambito')
        filtro_agente = request.form.get('filtro-agente')
        filtro_materia = request.form.get('filtro-materia')

        # Filtrar las noticias según los criterios de búsqueda
        if filtro_fuente:
            noticias = [n for n in noticias if filtro_fuente in n['fuente']]
        if filtro_ambito:
            noticias = [n for n in noticias if filtro_ambito in n['ambito']]
        if filtro_agente:
            noticias = [n for n in noticias if filtro_agente in n['agente']]
        if filtro_materia:
            noticias = [n for n in noticias if filtro_materia in n['materia']]

    return render_template('index.html', noticias=noticias, fuentes=fuentes, ambitos=ambitos, agentes=agentes, materias=materias)

# El puerto 5000 debe coincidir
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

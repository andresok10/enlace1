from flask import Flask, render_template, request, redirect
app = Flask(__name__)
links = [

("YouTube", "https://www.youtube.com/"),
("Futbol-Libre", "https://librefutbol.su/eventos/?r=aHR0cHM6Ly9jYW5kbGVyLmJlYXV0eS92b2QuaHRtbD9nZXQ9aHR0cHM6Ly92b29kYy5jb20vZW1iZWQvODU4YTkzOTBhMTg0OGE5Mzg3OTk4MzhiOTU4Yjk4ODU4Yjk2Lmh0bWw="),
("ecuabet", "https://ecuabet.com/deportes/partido/10613354?utm_source=Directa&utm_medium=Invasivo&utm_campaign=Evento_Tactico_ECU_Oct2024&utm_term=Evento&utm_content=Evento_Tactico_ECU_Oct2024"),
("peliculas1", "https://www.bilibili.tv/en/video/2042945247"),
("boostrap", "https://getbootstrap.com/docs/5.0/getting-started/introduction/"),
("tia.com", "https://reclutamiento.tia.com.ec/buscar"),
("apis_public", "https://www.apispublicas.com/"),
("numverify", "https://numverify.com/login?u=https%3A%2F%2Fnumverify.com%2Fdashboard"),
("API1", "https://serpstack.com/"),
("HACKIN1", "https://www.youtube.com/watch?v=1e8R7K_sIl8"),
("XAMP", "https://www.youtube.com/watch?v=84IOtc05TuA"),
("ILOVE-PDF", "https://www.ilovepdf.com/es"),
("MIES", "https://tramitesenlinea.inclusion.gob.ec/tramiteonl/views/public/registro_inicio.jsf"),
("program_python", "https://www.youtube.com/"),
("audio", "https://www.youtube.com/watch?v=iSFA1XiULBY"),
("vscode", "https://stackoverflow.com/questions/45218663/use-workbench-colorcustomizations-in-extension"),
("solucion_mysql", "https://www.youtube.com/watch?v=5cCT1ThLqqU"),
("reflex", "https://reflex.dev/docs/getting-started/introduction/"),
("calcular_edad", "https://calculadoradeedad.com/?day=10&month=11&year=1991"),

]
@app.route('/')
def index():
    return render_template('app_lista.html', links=links)

@app.route('/load', methods=['POST'])
def load():
    url = request.form.get('url')
    if url:
        return redirect(url)
    #return redirect('/')

if __name__ == '__main__':
    #app.run(host='127.0.0.1', port=8000, debug=True)
    app.run(host='0.0.0.0', port=8000, debug=True) # python app.py
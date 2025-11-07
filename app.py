from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    pokemon = None
    error = None

    if request.method == 'POST':
        name = (request.form.get('name') or '').strip().lower()
        if not name:
            error = 'Ingrese el nombre de un Pokémon.'
        else:
            url = f'https://pokeapi.co/api/v2/pokemon/{name}'
            try:
                resp = requests.get(url)
                if resp.status_code == 200:
                    data = resp.json()
                    pokemon = {
                        'name': data.get('name'),
                        'moves': [m['move']['name'] for m in data.get('moves', [])],
                        'types': [t['type']['name'] for t in data.get('types', [])],
                        'sprites': {
                            'front_default': data.get('sprites', {}).get('front_default'),
                            'front_shiny': data.get('sprites', {}).get('front_shiny'),
                            'back_default': data.get('sprites', {}).get('back_default'),
                            'back_shiny': data.get('sprites', {}).get('back_shiny'),
                        }
                    }
                elif resp.status_code == 404:
                    error = f"No se encontró el Pokémon '{name}'."
                else:
                    error = f"Error al consultar la API (status {resp.status_code})."
            except requests.RequestException:
                error = 'Error de conexión al consultar la API.'

    return render_template('index.html', pokemon=pokemon, error=error)

if __name__ == '__main__':
    app.run(debug=True)


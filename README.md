# Pokémon Flask App

Pequeña aplicación Flask que consulta la PokeAPI y muestra nombre, movimientos, tipos y 4 imágenes (frente/espalda default y shiny).

Requisitos
- Python 3.8+

Instalación (PowerShell)

```powershell
# crear entorno virtual (opcional pero recomendado)
python -m venv venv
# activar
.\venv\Scripts\Activate.ps1
# instalar dependencias
pip install -r requirements.txt
```

Ejecutar localmente

```powershell
# opción simple
python app.py
# o usando flask (si prefieres usar el comando flask):
$env:FLASK_APP = "app.py"; flask run
```

Desplegar a Heroku (opcional)

1) Instalar y loguearte con la CLI de Heroku.
2) Inicializar git, crear app y push:

```powershell
git init
heroku create
git add .
git commit -m "deploy"
# si tu branch principal es 'main'
git push heroku main
```

Nota: Heroku usará el `Procfile` y `requirements.txt`. Si usas otra plataforma (Render, Railway, etc.) los pasos son similares: subir el repo y configurar el comando de arranque `gunicorn app:app`.

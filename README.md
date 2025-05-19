🚀 **Instrucciones de Instalación y Despliegue**

## 🖥️ 1. Ejecución Local
_Requisitos: Python 3.9+, pip, MySQL (o SQLite para pruebas)_

```bash
# 1. Clona el repositorio
git clone https://github.com/sofia-donoso21/optica-maipu.git
cd optica-almonacid

# 2. Crea un entorno virtual
python -m venv venv
source venv/bin/activate   # En Windows: venv\Scripts\activate

# 3. Instala las dependencias
pip install -r requirements.txt

# 4. Configura las variables de entorno (ejemplo en .env)
# FLASK_APP=app.py
# DB_HOST=localhost
# DB_USER=root
# DB_PASS=tu_clave
# DB_NAME=optica

# 5. Inicializa la base de datos (si usas SQLAlchemy)
python setup_db.py  # o script equivalente de migración

# 6. Ejecuta la app
flask run


## ☁️ 2. Despliegue en Azure App Service

Requisitos: Cuenta de Azure, Azure CLI, App Service Plan (Linux), Python 3.9+

```bash
# 1. Inicia sesión en Azure
az login

# 2. Crea un grupo de recursos
az group create --name OpticaGroup --location eastus

# 3. Crea un plan de App Service (Linux)
az appservice plan create --name OpticaPlan --resource-group OpticaGroup --sku B1 --is-linux

# 4. Crea la aplicación web Flask
az webapp create --resource-group OpticaGroup \
  --plan OpticaPlan \
  --name optica-almonacid-app \
  --runtime "PYTHON|3.9" \
  --deployment-local-git

# 5. Obtén la URL del repositorio remoto para despliegue
az webapp deployment source config-local-git \
  --name optica-almonacid-app \
  --resource-group OpticaGroup

# 6. Agrega el repositorio remoto a tu proyecto local
git remote add azure <URL-GIT-proporcionada>
git push azure main

# 7. Configura las variables de entorno
az webapp config appsettings set \
  --name optica-almonacid-app \
  --resource-group OpticaGroup \
  --settings FLASK_APP=app.py DB_HOST=<host> DB_USER=<usuario> DB_PASS=<clave> DB_NAME=optica

# 8. Accede a tu aplicación
# Visita: https://optica-almonacid-app.azurewebsites.net

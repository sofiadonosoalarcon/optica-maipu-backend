# Óptica Almonacid

One Paragraph of project description goes here

## Instrucciones de Instalación y Despliegue

Estas instrucciones le permitirán obtener una copia del proyecto en funcionamiento en su equipo local para fines de desarrollo y pruebas. Consulte la sección de implementación para obtener instrucciones sobre cómo implementar el proyecto en un sistema en vivo.

### Ejecución Local 🖥️
> Requisitos: Python 3.9+, pip, MySQL (o SQLite para pruebas)


```
# 1. Clona el repositorio
git clone https://github.com/tu-usuario/optica-almonacid.git
cd optica-almonacid

# 2. Crea un entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

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
```

### Despliegue en Azure App Service
> Requisitos: Cuenta de Azure, CLI de Azure, App Service plan

```
# 1. Inicia sesión en Azure
az login

# 2. Crea un grupo de recursos (si no existe)
az group create --name OpticaGroup --location eastus

# 3. Crea el plan de App Service
az appservice plan create --name OpticaPlan --resource-group OpticaGroup --sku B1 --is-linux

# 4. Crea la Web App
az webapp create --resource-group OpticaGroup --plan OpticaPlan \
  --name optica-almonacid-app --runtime "PYTHON|3.9" \
  --deployment-local-git

# 5. Obtén la URL del repositorio Git para hacer push
az webapp deployment source config-local-git \
  --name optica-almonacid-app --resource-group OpticaGroup

# 6. Agrega y empuja al remoto
git remote add azure <url-git-proporcionada>
git push azure main

# 7. Configura variables de entorno
az webapp config appsettings set \
  --name optica-almonacid-app \
  --resource-group OpticaGroup \
  --settings FLASK_ENV=production
```

### Despliegue en Azure App Service
> Requisitos: Cuenta de Azure, CLI de Azure, App Service plan

```
# 1. Inicia sesión en Azure
az login

# 2. Crea un grupo de recursos (si no existe)
az group create --name OpticaGroup --location eastus

# 3. Crea el plan de App Service
az appservice plan create --name OpticaPlan --resource-group OpticaGroup --sku B1 --is-linux

# 4. Crea la Web App
az webapp create --resource-group OpticaGroup --plan OpticaPlan \
  --name optica-almonacid-app --runtime "PYTHON|3.9" \
  --deployment-local-git

# 5. Obtén la URL del repositorio Git para hacer push
az webapp deployment source config-local-git \
  --name optica-almonacid-app --resource-group OpticaGroup

# 6. Agrega y empuja al remoto
git remote add azure <url-git-proporcionada>
git push azure main

# 7. Configura variables de entorno
az webapp config appsettings set \
  --name optica-almonacid-app \
  --resource-group OpticaGroup \
  --settings FLASK_ENV=production

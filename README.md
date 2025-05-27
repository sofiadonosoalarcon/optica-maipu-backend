# Óptica Almonacid

One Paragraph of project description goes here

## Instrucciones de Instalación y Despliegue

Estas instrucciones le permitirán obtener una copia del proyecto en funcionamiento en su equipo local para fines de desarrollo y pruebas. Consulte la sección de implementación para obtener instrucciones sobre cómo implementar el proyecto en un sistema en vivo.

### 🖥️  Ejecución Local 
> Requisitos: Python 3.9+, pip, MySQL (o SQLite para pruebas)


```
# 1. Clona el repositorio
git clone --branch fix/implementation-products --single-branch https://github.com/sofiadonosoalarcon/optica-maipu.git 
cd optica-maipu

# 2. Crea un entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# 3. Instala las dependencias
pip install -r requirements.txt

# 6. Ejecuta la app
flask run // python boot.py
```

### ☁️  Despliegue en Azure App Service
> Requisitos: Cuenta de Azure, CLI de Azure, App Service plan

```
# 1. Inicia sesión en Azure
az login

# 2. Crea un grupo de recursos (si no existe)
az group create --name optica-maipu-resource-group --location eastus

# 3. Crea el plan de App Service
az appservice plan create --name optica-maipu-plan --resource-group optica-maipu-resource-group --sku B1 --is-linux

# 4. Crea la Web App
az webapp create --resource-group optica-maipu-resource-group --plan optica-maipu-plan \
  --name optica-maipu-backend --runtime "PYTHON|3.13" 

# 5. Crear el workflow oara el despliegue





```

### 🧪  Ejecución de Tests
> Requisitos: pytest, pytest-cov


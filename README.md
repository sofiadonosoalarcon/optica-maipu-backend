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

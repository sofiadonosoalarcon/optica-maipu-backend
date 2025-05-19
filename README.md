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

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

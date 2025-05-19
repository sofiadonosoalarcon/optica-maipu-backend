# Óptica Almonacid

La transformación digital ha generado profundas transformaciones en los modelos operativos de las empresas, especialmente en aquellas que buscan mejorar su eficiencia y adaptarse a un entorno competitivo cada vez más exigente. En este contexto, la automatización de procesos como la gestión de inventarios y ventas ha demostrado ser un factor clave para incrementar la productividad, reducir errores y tomar decisiones más informadas (Porter & Heppelmann, 2017).
Óptica Almonacid, una pequeña empresa familiar ubicada en la comuna de Maipú, ha logrado consolidarse como un proveedor confiable de productos ópticos. Sin embargo, su crecimiento ha evidenciado limitaciones en su modelo de operación, el cual se basa en procedimientos manuales para la administración de inventarios y la emisión de boletas. Esta situación ha provocado inconsistencias en el control de stock, errores en la atención al cliente y dificultades en la planificación de compras.
La falta de integración entre los procesos de ventas, inventario y finanzas limita la capacidad de respuesta de la óptica ante la demanda del mercado y restringe su proyección a largo plazo. De acuerdo con Kotler y Keller (2016), la adopción de soluciones tecnológicas adecuadas permite a las empresas mejorar su propuesta de valor, reducir costos operacionales y fortalecer la relación con los clientes.
Este estudio tiene como objetivo analizar las falencias operativas actuales de Óptica Almonacid y proponer una solución tecnológica que permita automatizar sus procesos clave. Se evaluarán distintas alternativas de implementación, considerando su viabilidad técnica, operativa y económica. Asimismo, se abordarán conceptos relacionados con la transformación digital, la gestión de inventarios y el desarrollo de software, con el propósito de entregar una propuesta integral y sostenible en el tiempo.


## 🖥️ 1. Ejecución Local

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

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

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
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

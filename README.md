## 🚀 Instrucciones de Instalación y Despliegue

### 🖥️ 1. Ejecución Local

> Requisitos: Python 3.9+, pip, MySQL (o SQLite para pruebas)

```bash
# 1. Clona el repositorio
git clone https://github.com/sofia-donoso21/optica-maipu.git
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

## 🚀 Despliegue Azure
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


# 🧾 Sistema Automatizado para Óptica Almonacid

## 📌 Resumen del Proyecto
Este proyecto busca implementar un **sistema automatizado de control de inventarios, ventas y pagos** en **Óptica Almonacid**, con el fin de optimizar procesos operativos, mejorar la atención al cliente y facilitar la administración de recursos mediante herramientas digitales modernas como **Mercado Pago**.

---

## 🎯 Objetivos
- Automatizar la gestión de productos, ventas y cobros.
- Reducir errores humanos y tiempos operativos.
- Integrar métodos de pago digitales y seguros.
- Aumentar la satisfacción del cliente con procesos más rápidos y transparentes.
- Mejorar el control interno y la trazabilidad de movimientos.

---

## 🛠️ Tecnologías y Herramientas
- **Lenguaje de programación:** Python (Flask), JavaScript
- **Base de datos:** MySQL
- **Frontend:** HTML, CSS, Bootstrap
- **Pasarela de pagos:** Mercado Pago
- **Modelado UML:** Enfoque OMT++ (Modelo funcional, dinámico y de objetos)

---

## 👥 Actores Principales
- **Administrador:** Gestiona inventario, ventas, pagos y usuarios.
- **Cliente:** Realiza compras y pagos.
- **Empleado:** Atiende ventas y actualiza productos.
- **Proveedor:** Abastece productos y actualiza stock.
- **Mercado Pago:** Procesa los pagos en línea.

---

## 🧩 Modelado OMT++
Se aplicó el enfoque OMT++ para diseñar el sistema con un enfoque estructurado y técnico:

### 🔄 Modelo Dinámico
- Diagrama de estados que representa el comportamiento del sistema ante eventos como compras, pagos y reabastecimientos.

### 🧱 Modelo de Objetos
- Clases como `Producto`, `Usuario`, `Venta`, `Pago`, `Proveedor`, `Cliente`
- Relaciones: herencia, agregación y asociaciones múltiples.

### ⚙️ Modelo Funcional
- Diagramas de flujo de datos (DFD) para procesos clave:
  - Registro de ventas
  - Control de inventario
  - Procesamiento de pagos
  - Reportes administrativos

---

## ✅ Beneficios Esperados
- Control en tiempo real del inventario y las ventas.
- Pagos seguros e instantáneos.
- Reducción de errores humanos.
- Mejora en la experiencia del cliente.
- Diferenciación frente a la competencia.

---

## ⚠️ Riesgos y Consideraciones
- Resistencia al cambio por parte del personal.
- Incompatibilidad con sistemas preexistentes.
- Riesgos de seguridad en el manejo de datos.

---

## 🧠 Recomendaciones
- Capacitación progresiva del personal.
- Implementar soporte técnico y acompañamiento en el uso.
- Realizar pruebas piloto y ajustes continuos.
- Establecer protocolos de mantenimiento y seguridad de datos.

---

## 📚 Bibliografía
- Laudon, K. C. – *Management Information Systems*
- Heizer, J. – *Operations Management*
- Mercado Pago – *Soluciones de pago para negocios*
- Cabrera, E. – *Transformación Digital*
- Gartner – *Retail Digital Guide*

---

## 📎 Conclusión
La implementación de un sistema automatizado de control de inventarios, ventas y pagos en **Óptica Almonacid** permitirá optimizar significativamente los procesos operativos, reducir tiempos y esfuerzos en la gestión diaria y mejorar la calidad del servicio al cliente.

Con una planificación adecuada, capacitación y estrategias de mitigación, esta transformación digital no solo mejorará la eficiencia interna, sino que fortalecerá el posicionamiento competitivo de la óptica a largo plazo.

---



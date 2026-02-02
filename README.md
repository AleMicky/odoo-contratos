# 📑 Sistema de Contratos – Odoo + Docker

Módulo profesional de **gestión de contratos** desarrollado en **Odoo**, pensado para entornos reales de **RRHH / Legal / Administración**, con soporte para **Docker** y buenas prácticas de desarrollo.

---

## 🚀 Características principales

- 📄 Registro de contratos
- 🏷️ Tipos de contrato configurables
- 🔄 Flujo de estados (Borrador → Vigente → Vencido / Rescindido)
- 📎 Adjuntos (PDF / documentos firmados)
- ⏰ Alerta visual de contratos por vencer
- 🔐 Seguridad por usuarios internos
- 💬 Seguimiento y auditoría (mail.thread)
- 🐳 Entorno de desarrollo con Docker

---

## 🧱 Tecnologías utilizadas

- **Odoo** (v18+)
- **Python**
- **PostgreSQL**
- **Docker / Docker Compose**
- **XML (Vistas Odoo)**
- **Git**

---

## 📁 Estructura del proyecto
odoo-contratos/
├── docker-compose.yml
├── .env.example
├── config/
│   └── odoo.conf
├── addons/
│   └── contratos/
│       ├── manifest.py
│       ├── init.py
│       ├── models/
│       │   ├── contrato.py
│       │   ├── contrato_tipo.py
│       │   └── init.py
│       ├── views/
│       │   ├── contrato_views.xml
│       │   ├── contrato_tipo_views.xml
│       │   └── menu.xml
│       └── security/
│           └── ir.model.access.csv
└── README.md

---

## ⚙️ Requisitos previos

- Docker y Docker Compose
- Git
- Navegador web moderno

---

## ▶️ Instalación y ejecución

### 1️⃣ Clonar el repositorio
```bash
git clone git@github.com:AleMicky/odoo-contratos.git
cd odoo-contratos

2️⃣ Configurar variables de entorno

Copia el archivo de ejemplo:

cp .env.example .env

3️⃣ Levantar el entorno con Docker

docker compose up -d

4️⃣ Inicializar la base de datos (primera vez)

docker exec -it odoo-app odoo \
  --config=/etc/odoo/odoo.conf \
  -d odoo_dev \
  -i base \
  --without-demo=all \
  --stop-after-init

Reinicia el servicio Odoo:

docker compose restart odoo

5️⃣ Instalar el módulo Contratos
	1.	Accede a:
👉 http://localhost:8069
	2.	Activa el modo desarrollador:
👉 http://localhost:8069/?debug=1
	3.	Ve a Apps
	4.	Pulsa Update Apps List
	5.	Busca Sistema de Contratos
	6.	Instala el módulo

🔄 Desarrollo y actualización del módulo

docker exec -it odoo-app odoo \
  --config=/etc/odoo/odoo.conf \
  -d odoo_dev \
  -u contratos \
  --stop-after-init

docker compose restart odoo

🔐 Seguridad

El módulo incluye permisos básicos definidos en:
	•	security/ir.model.access.csv

Por defecto:
	•	Usuarios internos pueden crear y leer contratos
	•	La seguridad puede ampliarse con roles específicos (RRHH / Legal)

🛠️ Posibles mejoras futuras
	•	📄 Generación de contratos en PDF (QWeb)
	•	🔔 Alertas automáticas por correo
	•	👥 Integración con empleados (hr.employee)
	•	📊 Dashboard con gráficos y KPIs
	•	🧾 Historial legal de modificaciones
	•	⏱️ Cron automático para vencimientos

👨‍💻 Autor

Miky
Desarrollador de software
Especializado en Backend, Odoo y sistemas administrativos

⸻

📜 Licencia

Este proyecto se distribuye bajo la licencia LGPL-3, compatible con el ecosistema Odoo.

⸻

⭐ Notas finales

Este módulo fue desarrollado siguiendo buenas prácticas de Odoo y puede adaptarse fácilmente a instituciones públicas o privadas.

Eres libre de usarlo, modificarlo y ampliarlo según tus necesidades.

---

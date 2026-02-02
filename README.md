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



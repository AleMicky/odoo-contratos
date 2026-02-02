{
    "name": "Sistema de Contratos",
    "version": "1.0.0",
    "category": "Human Resources",
    "summary": "Registro y control de contratos",
    "author": "Miky",
    "depends": ["base", "mail", "hr"], 
    "data": [
        "security/ir.model.access.csv",
        "views/contrato_tipo_views.xml",
        "views/contrato_views.xml",
        "views/menu.xml",
    ],
    "application": True,
    "installable": True,
    "license": "LGPL-3",
}
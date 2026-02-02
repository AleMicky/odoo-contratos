from odoo import models, fields

class ContratoTipo(models.Model):
    _name = 'contratos.tipo'
    _description = 'Tipo de Contrato'

    name = fields.Char(string="Nombre", required=True)
    codigo = fields.Char(string="Código", required=True)
    descripcion = fields.Text(string="Descripción")
    activo = fields.Boolean(default=True)
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Contrato(models.Model):
    _name = "contratos.contrato"
    _description = "Contrato"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "fecha_inicio desc"

    name = fields.Char(
        string="Código",
        default="Nuevo",
        readonly=True,
        copy=False
    )

    titulo = fields.Char(required=True, tracking=True)
    tipo_id = fields.Many2one("contratos.tipo", required=True)
    partner_id = fields.Many2one(
        "res.partner",
        string="Cliente / Proveedor",
        required=True
    )

    fecha_inicio = fields.Date(required=True, default=fields.Date.today)
    fecha_fin = fields.Date()
    monto = fields.Monetary()
    currency_id = fields.Many2one(
        "res.currency",
        default=lambda self: self.env.company.currency_id
    )

    estado = fields.Selection([
        ("borrador", "Borrador"),
        ("vigente", "Vigente"),
        ("vencido", "Vencido"),
        ("rescindido", "Rescindido"),
    ], default="borrador", tracking=True)

    notas = fields.Text()
    documento_ids = fields.Many2many(
        "ir.attachment",
        string="Documentos"
    )

    vence_pronto = fields.Boolean(compute="_compute_vence_pronto")

    @api.depends("fecha_fin")
    def _compute_vence_pronto(self):
        hoy = fields.Date.today()
        for rec in self:
            rec.vence_pronto = bool(
                rec.fecha_fin and (rec.fecha_fin - hoy).days <= 30
            )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get("name") == "Nuevo":
                vals["name"] = self.env["ir.sequence"].next_by_code(
                    "contratos.contrato"
                ) or "CT-00001"
        return super().create(vals_list)

    def action_vigente(self):
        self.write({"estado": "vigente"})

    def action_vencido(self):
        self.write({"estado": "vencido"})

    def action_rescindir(self):
        self.write({"estado": "rescindido"})
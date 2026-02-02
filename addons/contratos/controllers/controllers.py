# from odoo import http


# class Contratos(http.Controller):
#     @http.route('/contratos/contratos', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/contratos/contratos/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('contratos.listing', {
#             'root': '/contratos/contratos',
#             'objects': http.request.env['contratos.contratos'].search([]),
#         })

#     @http.route('/contratos/contratos/objects/<model("contratos.contratos"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('contratos.object', {
#             'object': obj
#         })


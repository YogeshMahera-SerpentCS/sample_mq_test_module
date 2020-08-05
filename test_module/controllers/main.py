from odoo import http
from odoo.http import request

from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSale(WebsiteSale):
    @http.route(["/notes"], type="json", auth="public", website=True)
    def order_notes(self, note="", **post):
        order = request.website.sale_get_order()
        order.sudo().write({"note": note})
        return True

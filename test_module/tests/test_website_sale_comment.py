from odoo.tests import common, tagged
from odoo.addons.website.tools import MockRequest
from odoo.addons.test_module.controllers.main import WebsiteSale


@tagged("post_install", "-at_install")
class TestWebsiteSaleComment(common.TransactionCase):
    def setUp(self):
        super(TestWebsiteSaleComment, self).setUp()
        self.website = self.env["website"].browse(1)
        self.WebsiteSaleController = WebsiteSale()

    # TEST WEBSITE SALE COMMENT
    def test_create_website_sale_comment(self):
        partner = self.env.user.partner_id
        so = self._create_so(partner.id)
        with MockRequest(self.env, website=self.website, sale_order_id=so.id):
            note = "<p>test-comment</p>"
            self.WebsiteSaleController.order_notes(note=note, **{})
            self.assertEqual(so.note, note, "Test-Comment Added to SaleOrder")

    def _create_so(self, partner_id=None):
        return self.env["sale.order"].create(
            {
                "partner_id": partner_id,
                "website_id": self.website.id,
                "order_line": [
                    (
                        0,
                        0,
                        {
                            "product_id": self.env["product.product"]
                            .create({"name": "Product A", "list_price": 100})
                            .id,
                            "name": "Product A",
                        },
                    )
                ],
            }
        )

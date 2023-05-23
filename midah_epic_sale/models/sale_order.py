from odoo import models, fields


class SaleOrder_FS(models.Model):
    _inherit = "sale.order"
    quot_notes_fs = fields.Text(string='Notes')
    quot_optional_item1_fs = fields.Char(string="Optional Item1")
    quot_optional_item2_fs = fields.Char(string="Optional Item2")
    quot_optional_item3_fs = fields.Char(string="Optional Item3")
    quot_optional_item4_fs = fields.Char(string="Optional Item4")
    quot_validity_epic = fields.Char(string="Validity")
    #quot_terms_epic = fields.Char(string="Terms")
    quot_payterms_epic = fields.Char(string="Terms")
    quot_delivery_time_epic = fields.Char(string="Delivery time")
    quot_delivery_epic = fields.Char(string="Delivery")
    quot_reference_link_epic = fields.Many2one('ir.attachment', string='Reference Link')


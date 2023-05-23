from odoo import models, fields,api


class SaleOrder_FS(models.Model):
    _inherit = "sale.order"
    quot_notes_timber = fields.Text(string='Notes')
    quot_optional_item1_timber = fields.Char(string="Optional Item1")
    quot_optional_item2_timber = fields.Char(string="Optional Item2")
    quot_optional_item3_timber = fields.Char(string="Optional Item3")
    quot_optional_item4_timber = fields.Char(string="Optional Item4")
    quot_validity_timber = fields.Char(string="Validity")
    quot_terms_timber = fields.Char(string="Terms")
    quot_price_validity_fs = fields.Char(string="Price Validity")
    quot_reference_link_timber = fields.Many2one('ir.attachment', string='Reference Link')

    optional_item1_timber = fields.Many2one('optional.items',string="Optional Item 1")

    optional_item2_timber = fields.Many2one('optional.items',string="Optional Item 2")

    optional_item3_timber = fields.Many2one('optional.items',string="Optional Item 3")

    optional_item4_timber = fields.Many2one('optional.items',string="Optional Item 4")

    optional_item5_timber = fields.Many2one('optional.items',string="Optional Item 5")

    optional_item6_timber = fields.Many2one('optional.items',string="Optional Item 6")

    optional_item7_timber = fields.Many2one('optional.items',string="Optional Item 7")

    optional_item8_timber = fields.Many2one('optional.items',string="Optional Item 8")

    optional_item9_timber = fields.Many2one('optional.items',string="Optional Item 9")

    optional_item10_timber = fields.Many2one('optional.items',string="Optional Item 10")

    optional_item11_timber = fields.Many2one('optional.items',string="Optional Item 11")

    optional_item12_timber = fields.Many2one('optional.items',string="Optional Item 12")

    # ~~~ Code by Hari ~~~
    timber_tnc = fields.Html(string="")
    # ~~~~~~~~~~~~~~~~~~~~

class SaleOrderLine_FS(models.Model):
    _inherit = "sale.order.line"

    @api.depends('tax_id')
    def _calculate_tax_per_qty_timber(self):
        for line in self:
            if line.tax_id:
                value = (line.price_tax / line.product_uom_qty)
                line.update({
                    'sstTax_fs_v4': value
                })
            if not line.tax_id:
                # value = (line.price_tax / line.product_uom_qty)
                line.update({
                    'sstTax_fs_v4': 0.00
                })

    @api.depends('tax_id')
    def _calculate_sum_tax_per_qty_timber(self):
        for line in self:
            if line.tax_id:
                value = (line.price_unit + line.sstTax_fs_v2)
                line.update({
                    'sstTax_fs_v5': value
                })
            if not line.tax_id:
                # value = (line.price_tax / line.product_uom_qty)
                line.update({
                    'sstTax_fs_v5': 0.00
                })

    sstTax_fs_v4 = fields.Float(compute='_calculate_tax_per_qty_timber', string='SST Value', digits=(12,2))
    sstTax_fs_v5 = fields.Float(compute='_calculate_sum_tax_per_qty_timber', string='Tax Incl. Rate', digits=(12,2))

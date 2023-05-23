from odoo import models, fields,api


class SaleOrder_FS(models.Model):
    _inherit = "sale.order"
    quot_notes_fs = fields.Text(string='Notes')

    #quot_optional_item3_fs = fields.Char(string="Optional Item3")
    #quot_optional_item4_fs = fields.Char(string="Optional Item4")
    quot_validity_fs = fields.Char(string="Validity")
    quot_terms_fs = fields.Char(string="Terms")
    quot_reference_link_kempurna = fields.Many2one('ir.attachment', string='Reference Link')

    sales_reviewer_v1 = fields.Many2one('res.users')
    sales_reviewer_v2 = fields.Many2one('res.partner', string="Sales Reviewer")

    optional_item1_KMPR = fields.Many2one('kmoptional.items', string="Optional Item 1")

    optional_item2_KMPR = fields.Many2one('kmoptional.items', string="Optional Item 2")

    optional_item3_KMPR = fields.Many2one('kmoptional.items', string="Optional Item 3")

    optional_item4_KMPR = fields.Many2one('kmoptional.items', string="Optional Item 4")

    optional_item5_KMPR = fields.Many2one('kmoptional.items', string="Optional Item 5")

    optional_item6_KMPR = fields.Many2one('kmoptional.items', string="Optional Item 6")

    quot_optional_item1_fs = fields.Text(string="Optional Item7")
    quot_optional_item2_fs = fields.Text(string="Optional Item8")


class SaleOrderLine_FS(models.Model):
    _inherit = "sale.order.line"

    @api.depends('tax_id')
    def _calculate_tax_per_qty(self):
        for line in self:
            if line.tax_id:
                value = (line.price_tax/line.product_uom_qty)
                line.update({
                    'sstTax_fs_v2': value
                    })
            if not line.tax_id:
                # value = (line.price_tax / line.product_uom_qty)
                line.update({
                    'sstTax_fs_v2': 0.00
                })

    @api.depends('tax_id')
    def _calculate_sum_tax_per_qty(self):
        for line in self:
            if line.tax_id:
                value = (line.price_unit + line.sstTax_fs_v2)
                line.update({
                    'sstTax_fs_v3': value
                })
            if not line.tax_id:
                # value = (line.price_tax / line.product_uom_qty)
                line.update({
                    'sstTax_fs_v3': 0.00
                })

    sstTax_fs_v2 = fields.Float(compute='_calculate_tax_per_qty', string='SST Value', digits=(12,2))
    sstTax_fs_v3 = fields.Float(compute='_calculate_sum_tax_per_qty', string='Tax Incl. Rate', digits=(12,2))

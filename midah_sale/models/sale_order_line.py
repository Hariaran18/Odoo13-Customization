from odoo import models, fields,api
#import odoo.addons.decimal_precision as dp

class SalesOrderLineTax(models.Model):
    _inherit = "sale.order.line"

    @api.depends('product_uom_qty','tax_id')
    def _comput_sstTax_fs(self):
        for line in self:
            if line.tax_id:
                value = (line.price_tax / line.product_uom_qty)
                line.update({
                    'sstTax_fs': value
                })

    sstTax_fs = fields.Float(compute="_comput_sstTax_fs",string="SST Value")




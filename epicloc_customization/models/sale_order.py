# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class SaleOrder_EpicLoc(models.Model):
    _inherit = "sale.order"

    quot_validity_epicloc = fields.Char(string='Validity of offer', default="7")
    quot_terms_epicloc = fields.Char(string='Delivery1', default="Ex-Klang Valley otherwise subject to transportation charges.")
    quot_terms_epicloc2 = fields.Char(string='Delivery2', default="Ex-Stock otherwise 90 days lead times upon receiving official confirmation order.")
    quot_terms_epicloc3 = fields.Char(string='Term', default="Subject to Credit Term Application Approval.")
    epicloc_tnc = fields.Html(string="")
    so_number = fields.Char(string="")
    so_attach = fields.Many2many('ir.attachment',
                                 'sale_order_so_attach_ir_attachments_rel',
                                 'so_id', 'attachment_id',
                                 string='SO Attachment')
        
class SaleOrderLine_EpicLoc(models.Model):
    _inherit = "sale.order.line"
    
    door_type = fields.Char('Door Type')

    @api.depends('tax_id')
    def _calculate_tax_per_qty_epicloc(self):
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
    def _calculate_sum_tax_per_qty_epicloc(self):
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

    sstTax_fs_v4 = fields.Float(compute='_calculate_tax_per_qty_epicloc', string='SST Value', digits=(12,2))
    sstTax_fs_v5 = fields.Float(compute='_calculate_sum_tax_per_qty_epicloc', string='Tax Incl. Rate', digits=(12,2))
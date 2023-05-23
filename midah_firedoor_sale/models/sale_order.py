from odoo import models, fields,api


class SaleOrder_FS(models.Model):
    _inherit = "sale.order"
    quot_remarks_firedoor = fields.Text(string='Remarks')
    paymode_firedoor_fds1 = fields.Char(string="Billing Mode1")
    paymode_firedoor_fds2 = fields.Char(string="Billing Mode2")
    paymode_firedoor_fds3 = fields.Char(string="Billing Mode3")
    quot_validity_firedoor = fields.Char(string="Validity")
    quot_price_validity_firedoor = fields.Char(string="Price Validity")
    defect_report_terms_firedoor = fields.Char(string="Defect Report Time")
    quot_reference_link_firedoor = fields.Many2one('ir.attachment', string='Reference Link')

    optional_item1_firedoor = fields.Text(string='Optional Item 1',
                                          default='One Hour Fire Rated Ironmongeries – Single Leaf.')
    optional_item2_firedoor = fields.Text(string='Optional Item 2',
                                          default='Epic Mortise Lever Handle Lockset (E) c/w Euro Profile Cylinder– 1 set.')
    optional_item3_firedoor = fields.Text(string='Optional Item 3',
                                          default='Epic Door Closer c/w Regular Arm – 1 no.')
    optional_item4_firedoor = fields.Text(string='Optional Item 4',
                                          default='One Hour Fire Rated Ironmongeries – Double Leaf')
    optional_item5_firedoor = fields.Text(string='Optional Item 5',
                                          default='Epic Mortise Lever Handle Lockset (E) c/w Euro Profile Cylinder– 1 set.')
    optional_item6_firedoor = fields.Text(string='Optional Item 6',
                                          default='Epic Door Closer c/w Regular Arm – 2 nos.')
    optional_item7_firedoor = fields.Text(string='Optional Item 7',
                                          default='Epic Door Selector – 1 pc.')
    optional_item8_firedoor = fields.Text(string='Optional Item 8',
                                          default='Epic Auto Bolt – 1 pair.')
    optional_item9_firedoor = fields.Text(string='Optional Item 9',
                                          default='**TRANSPORT CHARGES RM350.00 / TRIP**')
    optional_item10_firedoor = fields.Text(string='Optional Item 10',
                                           default='a) @RM 30.00/per opening for Single Leaf.')
    optional_item11_firedoor = fields.Text(string='Optional Item 11',
                                           default='b) @RM 50.00/per opening for Double Leaf.')
    optional_item12_firedoor = fields.Text(string='Optional Item 12',
                                           default='a) Extra Over @RM3.50/no of frame for 100mm normal primer at bottom of metal frame.')
    optional_item13_firedoor = fields.Text(string='Optional Item 13',
                                           default='b) Extra Over Auto Bolt Opening For Double Leaf @RM 30.00/pair.')
    optional_item14_firedoor = fields.Text(string='Optional Item 14')
    optional_item15_firedoor = fields.Text(string='Optional Item 15')
    optional_item16_firedoor = fields.Text(string='Optional Item 16')
    optional_item17_firedoor = fields.Text(string='Optional Item 17')

class SaleOrderLine_FS(models.Model):
    _inherit = "sale.order.line"

    @api.depends('tax_id')
    def _calculate_tax_per_qty_firedoor(self):
        for line in self:
            if line.tax_id:
                value = (line.price_tax / line.product_uom_qty)
                line.update({
                    'sstTax_fs_v6': value
                })
            if not line.tax_id:
                # value = (line.price_tax / line.product_uom_qty)
                line.update({
                    'sstTax_fs_v6': 0.00
                })

    @api.depends('tax_id')
    def _calculate_sum_tax_per_qty_firedoor(self):
        for line in self:
            if line.tax_id:
                value = (line.price_unit + line.sstTax_fs_v2)
                line.update({
                    'sstTax_fs_v7': value
                })
            if not line.tax_id:
                # value = (line.price_tax / line.product_uom_qty)
                line.update({
                    'sstTax_fs_v7': 0.00
                })

    sstTax_fs_v6 = fields.Float(compute='_calculate_tax_per_qty_firedoor', string='SST Value', digits=(12,2))
    sstTax_fs_v7 = fields.Float(compute='_calculate_sum_tax_per_qty_firedoor', string='Tax Incl. Rate', digits=(12,2))


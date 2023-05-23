from odoo import models, fields


class SaleOrder_FS(models.Model):
    _inherit = "sale.order"
    quot_product_fs = fields.Text(string='Product')
    quot_price_contractor_fs = fields.Text(string='Price Contractor')
    quot_price_distributor_fs = fields.Text(string='Price Distributor')
    quot_bending_charges_fs = fields.Char(string='Bending Charges')
    quot_quotation_validity_fs = fields.Text(string='Quotation Validity')
    quot_price_validity_of_fs = fields.Text(string='Price Validity')
    quot_term_of_payment_fs = fields.Text(string='Terms of Payment')
    quot_confirm_order_fs = fields.Char(string='Confirm Order')
    quot_delivery_lead_time_fs = fields.Char(string='Delivery Lead Time')
    quot_acceptance_of_purchase_order_fs = fields.Text(string='Acceptance of Purchase')
    #quot_reference_link_fs = fields.Binary(string='Reference Link', readonly=True,help="Expofile related to this batch",copy=False)
    quot_reference_link_fs = fields.Many2one('ir.attachment',string='Reference Link')
    quot_salesorder_num_fs = fields.Char(string='Sales Order No.')
    quot_spcl_remarks_fs  = fields.Text(string='Special Remarks')
    product_type_mtx = fields.Selection([('cut-to-size', 'Cut-to-size mesh'), ('standard_sheets', 'Standard Sheets'),
                                  ('hard_drawn_wires', 'Hard Drawn Wires')], tracking=True)

    def get_string_value_of_selection(self):
        if self.product_type_mtx=='cut-to-size':
            value='Cut-to-size mesh',
        if self.product_type_mtx=='standard_sheets':
            value='Standard Sheets',
        if self.product_type_mtx=='hard_drawn_wires':
            value='Hard Drawn WWires'
        #print
         #   dict(self._fields['type'].selection).get(self.type)
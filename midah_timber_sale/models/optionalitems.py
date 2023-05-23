from odoo import models, fields, api

class optional_Iems(models.Model):
    _name="optional.items"

    name = fields.Text(string="Optional Item")

   # optional_item2a_timber = fields.Text(string="Optional Item 2",default="RM15/DOOR FOR CYLINDRICAL LOCKSET OPENING ONLY")
   # optional_item3a_timber = fields.Text(string="Optional Item 3",default="6 pcs of ±40mm meranti hardwood horizontal stiles")
   # optional_item4a_timber = fields.Text(string="Optional Item 4", default="4 pcs of ±40mm meranti hardwood vertical stiles")
   # optional_item5a_timber = fields.Text(string="Optional Item 5", default="Meranti hw ±10 x ±38mm lipping edge all round")
   # optional_item6a_timber = fields.Text(string="Optional Item 6", default="4 pcs of ±40mm Group C hardwood horizontal stiles")
   #optional_item7a_timber = fields.Text(string="Optional Item 7", default="2 pcs of ±40mm Group C hardwood vertical stiles")
   # optional_item8a_timber = fields.Text(string="Optional Item 8", default="Honeycomb core infilled")
   # optional_item9a_timber = fields.Text(string="Optional Item 9", default="Meranti hw 12 x 38mm hw edging all round")
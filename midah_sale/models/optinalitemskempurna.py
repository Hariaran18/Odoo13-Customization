from odoo import models, fields, api

class optional_Iems_KMPR(models.Model):
    _name="kmoptional.items"

    name = fields.Text(string="Kempurna Optional Item")
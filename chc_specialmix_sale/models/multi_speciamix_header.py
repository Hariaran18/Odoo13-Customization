from odoo import models, fields, api

class multiple_specialmix_headers(models.Model):
    _name = "header.ids"
    name = fields.Char(string="Table Name")
    ud_grade_title_v1 = fields.Text(string="Grade Title")
    ud_header_column1_v1 = fields.Text(string="Header Title 1")
    ud_subtitle1_v1 = fields.Text(string="Sub Title1")
    ud_header_column2_v1 = fields.Text(string="Header Title 2")
    ud_subtitle2_v1 = fields.Text(string="Sub Title2")
    ud_header_column3_v1 = fields.Text(string="Header Title 3")
    ud_subtitle3_v1 = fields.Text(string="Sub Title3")
    ud_header_column4_v1 = fields.Text(string="Header Title 4")
    ud_subtitle4_v1 = fields.Text(string="Sub Title4")
    ud_header_column5_v1 = fields.Text(string="Header Title 5")
    ud_subtitle5_v1 = fields.Text(string="Sub Title5")
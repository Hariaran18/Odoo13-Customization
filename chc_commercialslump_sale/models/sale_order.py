from odoo import models, fields, api


class SaleOrder_FS(models.Model):
    _inherit = "sale.order"
    payment_days_chc_newslump = fields.Text(string="Payment Terms")
    project_reply_chc_newslump = fields.Text(string="Project Reply")
    reference_link_chc_newslump = fields.Many2one('ir.attachment', string='Reference Link')
    special_remarks_newslump = fields.Text(string="Special Remarks")
    price_variation_clause_newslump = fields.Text(string="Price Variation Clause", default="Our prices are subject to price fluctuation of raw materials (i.e.: bulk cement, fuel, sand, aggregates and etc.) for all orders in progress of deliveries. The difference between market revised price and our quotation calculation will be chargeable to you accordingly.")

    jkr_mix_chc_commercialslump = fields.Char(string="JKR Mix")
    waterproof_mix_commercialslump = fields.Char(string="Water Proofing Mix")
    chipping_mix_chc_commercialslump = fields.Char(string="Chipping Mix")

    default_price_newslump = fields.Integer(string="Grade Default  Price")
    g20_default_price_newslump = fields.Integer(string="G20 Default  Price")

    ud_grade_title_ns = fields.Text(string="Grade Title", default="Grade")
    ud_header_column1_ns = fields.Text(string="Header Title 1",default="Normal Mix")
    ud_sub_title1_ns = fields.Text(string="Header Sub Title 1",default="100+/-25mm")
    ud_header_column2_ns = fields.Text(string="Header Title 2",default="Pump Mix")
    ud_sub_title2_ns = fields.Text(string="Header Sub Title 2",default="125+/-25mm")
    ud_header_column3_ns = fields.Text(string="Header Title 3",default="Tremie 1")
    ud_sub_title3_ns = fields.Text(string="Header Sub Title 3",default="150+/-25mm")
    ud_header_column4_ns = fields.Text(string="Header Title 4",default="Tremie 2")
    ud_sub_title4_ns = fields.Text(string="Header Sub Title 4",default="175+/-25mm")
    ud_header_column5_ns = fields.Text(string="Header Title 5",default="Tremie 3")
    ud_sub_title5_ns = fields.Text(string="Header Sub Title 5",default="210+/-25mm")

    # set default values for calculation fields
    mortar13_normal_newslump = fields.Integer(string="Mortar 1:3 Mix Value", default=13)
    mortar14_normal_newslump = fields.Integer(string="Mortar 1:4 Mix Value", default=13)
    mortar15_normal_newslump = fields.Integer(string="Mortar 1:5 Mix Value", default=13)
    g15_normal_newslump = fields.Integer(string="G15 Mix Value", default=5)
    g20_normal_newslump = fields.Integer(string="G20 Mix Value", default=5)
    g25_normal_newslump = fields.Integer(string="G25 Mix Value", default=9)
    g30_normal_newslump = fields.Integer(string="G30 Mix Value", default=10)
    g35_normal_newslump = fields.Integer(string="G35 Mix Value", default=11)
    g40_normal_newslump = fields.Integer(string="G40 Mix Value", default=13)

    g25_pump_newslump = fields.Integer(string="G25 Pump Mix Value", default=6)
    g30_pump_newslump = fields.Integer(string="G30 Pump Mix Value", default=6)
    g35_pump_newslump = fields.Integer(string="G35 Pump Mix Value", default=6)
    g40_pump_newslump = fields.Integer(string="G40 Pump Mix Value", default=6)

    g30_tremie1_newslump = fields.Integer(string="G30 Tremie1 Value", default=6)
    g35_tremie1_newslump = fields.Integer(string="G35 Tremie1 Value", default=6)
    g40_tremie1_newslump = fields.Integer(string="G40 Tremie1 Value", default=6)
    g45_tremie1_newslump = fields.Integer(string="G45 Tremie1 Value", default=15)
    g50_tremie1_newslump = fields.Integer(string="G50 Tremie1 Value", default=17)

    g30_tremie2_newslump = fields.Integer(string="G30 Tremie2 Value", default=6)
    g35_tremie2_newslump = fields.Integer(string="G35 Tremie2 Value", default=6)
    g40_tremie2_newslump = fields.Integer(string="G40 Tremie2 Value", default=6)
    g45_tremie2_newslump = fields.Integer(string="G45 Tremie2 Value", default=6)
    g50_tremie2_newslump = fields.Integer(string="G50 Tremie2 Value", default=17)

    g30_tremie3_newslump = fields.Integer(string="G30 Tremie3 Value", default=6)
    g35_tremie3_newslump = fields.Integer(string="G35 Tremie3 Value", default=6)
    g40_tremie3_newslump = fields.Integer(string="G40 Tremie3 Value", default=6)
    g45_tremie3_newslump = fields.Integer(string="G45 Tremie3 Value", default=6)
    g50_tremie3_newslump = fields.Integer(string="G50 Tremie3 Value", default=17)
    g55_tremie3_newslump = fields.Integer(string="G55 Tremie3 Value", default=17)
    g60_tremie3_newslump = fields.Integer(string="G60 Tremie3 Value", default=17)

    # store the calculated info into variable to pass in report- Normal Mix
    mortar13_custom_ns = fields.Integer(compute="_mortar13_custom_newslump", string="Mortar 1:3 Value",inverse="_mortar13_custom_newslumpv2",readonly=False,store=True)
    mortar14_custom_ns = fields.Integer(compute="_mortar14_custom_newslump", string="Mortar 1:4 Value",inverse="_mortar14_custom_newslumpv2",readonly=False,store=True)
    mortar15_custom_ns = fields.Integer(compute="_mortar15_custom_newslump", string="Mortar 1:5 Value",inverse="_mortar15_custom_newslumpv2",readonly=False,store=True)#,inverse="_inverse_mortar15_custom_newslump")
    g15_custom_ns = fields.Integer(compute="_g15_custom_newslump", string="G15 Value",inverse="_g15_custom_newslumpv2",readonly=False,store=True)
    #g20_custom_ns = fields.Integer(compute="_g20_custom_newslump", string="G20 Value",inverse="_g20_custom_newslumpv2",readonly=False,store=True)
    g25_custom_ns = fields.Integer(compute="_g25_custom_newslump", string="G25 Value",inverse="_g25_custom_newslumpv2",readonly=False,store=True)
    g30_custom_ns = fields.Integer(compute="_g30_custom_newslump", string="G30 Value",inverse="_g30_custom_newslumpv2",readonly=False,store=True)
    g35_custom_ns = fields.Integer(compute="_g35_custom_newslump", string="G35 Value",inverse="_g35_custom_newslumpv2",readonly=False,store=True)
    g40_custom_ns = fields.Integer(compute="_g40_custom_newslump", string="G40 Value",inverse="_g40_custom_newslumpv2",readonly=False,store=True)
    # Pump Mix
    g25_custom_pump_ns = fields.Integer(compute="_g25_custom_pump_ns", string="G25 Pump Value",inverse="_g25_custom_pump_nsv2",readonly=False,store=True)
    g30_custom_pump_ns = fields.Integer(compute="_g30_custom_pump_ns", string="G30 Pump Value",inverse="_g30_custom_pump_nsv2",readonly=False,store=True)
    g35_custom_pump_ns = fields.Integer(compute="_g35_custom_pump_ns", string="G35 Pump Value",inverse="_g35_custom_pump_nsv2",readonly=False,store=True)
    g40_custom_pump_ns = fields.Integer(compute="_g40_custom_pump_ns", string="G40 Pump Value",inverse="_g40_custom_pump_nsv2",readonly=False,store=True)
    # Tremie1 Mix
    g30_custom_tremie1_ns = fields.Integer(compute="_g30_custom_tremie1_ns", string="G30 Tremie1 Value",inverse="_g30_custom_tremie1_nsv2",readonly=False,store=True)
    g35_custom_tremie1_ns = fields.Integer(compute="_g35_custom_tremie1_ns", string="G35 Tremie1 Value",inverse="_g35_custom_tremie1_nsv2",readonly=False,store=True)
    g40_custom_tremie1_ns = fields.Integer(compute="_g40_custom_tremie1_ns", string="G40 Tremie1 Value",inverse="_g40_custom_tremie1_nsv2",readonly=False,store=True)
    g45_custom_tremie1_ns = fields.Integer(compute="_g45_custom_tremie1_ns", string="G45 Tremie1 Value",inverse="_g45_custom_tremie1_nsv2",readonly=False,store=True)
    g50_custom_tremie1_ns = fields.Integer(compute="_g50_custom_tremie1_ns", string="G50 Tremie1 Value",inverse="_g50_custom_tremie1_nsv2",readonly=False,store=True)
    # Tremie2 Mix
    g30_custom_tremie2_ns = fields.Integer(compute="_g30_custom_tremie2_ns", string="G30 Tremie2 Value",inverse="_g30_custom_tremie2_nsv2",readonly=False,store=True)
    g35_custom_tremie2_ns = fields.Integer(compute="_g35_custom_tremie2_ns", string="G35 Tremie2 Value",inverse="_g35_custom_tremie2_nsv2",readonly=False,store=True)
    g40_custom_tremie2_ns = fields.Integer(compute="_g40_custom_tremie2_ns", string="G40 Tremie2 Value",inverse="_g40_custom_tremie2_nsv2",readonly=False,store=True)
    g45_custom_tremie2_ns = fields.Integer(compute="_g45_custom_tremie2_ns", string="G45 Tremie2 Value",inverse="_g45_custom_tremie2_nsv2",readonly=False,store=True)
    g50_custom_tremie2_ns = fields.Integer(compute="_g50_custom_tremie2_ns", string="G50 Tremie2 Value",inverse="_g50_custom_tremie2_nsv2",readonly=False,store=True)
    # Tremie 3 Mix
    g30_custom_tremie3_ns = fields.Integer(compute="_g30_custom_tremie3_ns", string="G30 Tremie3 Value",inverse="_g30_custom_tremie3_nsv2",readonly=False,store=True)
    g35_custom_tremie3_ns = fields.Integer(compute="_g35_custom_tremie3_ns", string="G35 Tremie3 Value",inverse="_g35_custom_tremie3_nsv2",readonly=False,store=True)
    g40_custom_tremie3_ns = fields.Integer(compute="_g40_custom_tremie3_ns", string="G40 Tremie3 Value",inverse="_g40_custom_tremie3_nsv2",readonly=False,store=True)
    g45_custom_tremie3_ns = fields.Integer(compute="_g45_custom_tremie3_ns", string="G45 Tremie3 Value",inverse="_g45_custom_tremie3_nsv2",readonly=False,store=True)
    g50_custom_tremie3_ns = fields.Integer(compute="_g50_custom_tremie3_ns", string="G50 Tremie3 Value",inverse="_g50_custom_tremie3_nsv2",readonly=False,store=True)
    g55_custom_tremie3_ns = fields.Integer(compute="_g55_custom_tremie3_ns", string="G55 Tremie3 Value",inverse="_g55_custom_tremie3_nsv2",readonly=False,store=True)
    g60_custom_tremie3_ns = fields.Integer(compute="_g60_custom_tremie3_ns", string="G60 Tremie3 Value",inverse="_g60_custom_tremie3_nsv2",readonly=False,store=True)

    # Normal Mix
    @api.depends('default_price_newslump')
    def _mortar15_custom_newslump(self):
        for rec in self:
            rec.mortar15_custom_ns = rec.default_price_newslump + rec.mortar15_normal_newslump
    def _mortar15_custom_newslumpv2(self):
        return self.mortar15_custom_ns

    @api.depends('mortar15_custom_ns')
    def _mortar14_custom_newslump(self):
        for rec in self:
            rec.mortar14_custom_ns = rec.mortar15_custom_ns + rec.mortar14_normal_newslump
    def _mortar14_custom_newslumpv2(self):
        return self.mortar14_custom_ns

    @api.depends('mortar14_custom_ns')
    def _mortar13_custom_newslump(self):
        for rec in self:
            rec.mortar13_custom_ns = rec.mortar14_custom_ns + rec.mortar13_normal_newslump
    def _mortar13_custom_newslumpv2(self):
        return self.mortar13_custom_ns
    #def _g20_custom_newslump(self):
     #   for rec in self:
       #     rec.g20_custom_ns = rec.default_price_newslump - rec.g20_normal_newslump
    @api.depends('g20_default_price_newslump')
    def _g15_custom_newslump(self):
        for rec in self:
            rec.g15_custom_ns = rec.g20_default_price_newslump - rec.g15_normal_newslump
    def _g15_custom_newslumpv2(self):
        return self.g15_custom_ns

    @api.depends('g20_default_price_newslump')
    def _g25_custom_newslump(self):
        for rec in self:
            rec.g25_custom_ns = rec.g20_default_price_newslump + rec.g25_normal_newslump
    def _g25_custom_newslumpv2(self):
        return self.g25_custom_ns

    @api.depends('g25_custom_ns')
    def _g30_custom_newslump(self):
        for rec in self:
            rec.g30_custom_ns = rec.g25_custom_ns + rec.g30_normal_newslump
    def _g30_custom_newslumpv2(self):
        return self.g30_custom_ns

    @api.depends('g30_custom_ns')
    def _g35_custom_newslump(self):
        for rec in self:
            rec.g35_custom_ns = rec.g30_custom_ns + rec.g35_normal_newslump
    def _g35_custom_newslumpv2(self):
        return self.g35_custom_ns

    @api.depends('g35_custom_ns')
    def _g40_custom_newslump(self):
        for rec in self:
            rec.g40_custom_ns = rec.g35_custom_ns + rec.g40_normal_newslump
    def _g40_custom_newslumpv2(self):
        return self.g40_custom_ns

    # Pump Mix
    @api.depends('g25_custom_ns')
    def _g25_custom_pump_ns(self):
        for rec in self:
            rec.g25_custom_pump_ns = rec.g25_custom_ns + rec.g25_pump_newslump
    def _g25_custom_pump_nsv2(self):
        return self.g25_custom_pump_ns

    @api.depends('g30_custom_ns')
    def _g30_custom_pump_ns(self):
        for rec in self:
            rec.g30_custom_pump_ns = rec.g30_custom_ns + rec.g30_pump_newslump
    def _g30_custom_pump_nsv2(self):
        return self.g30_custom_pump_ns

    @api.depends('g35_custom_ns')
    def _g35_custom_pump_ns(self):
        for rec in self:
            rec.g35_custom_pump_ns = rec.g35_custom_ns + rec.g35_pump_newslump
    def _g35_custom_pump_nsv2(self):
        return self.g35_custom_pump_ns

    @api.depends('g40_custom_ns')
    def _g40_custom_pump_ns(self):
        for rec in self:
            rec.g40_custom_pump_ns = rec.g40_custom_ns + rec.g40_pump_newslump
    def _g40_custom_pump_nsv2(self):
        return self.g40_custom_pump_ns

    # Tremie 1 Mix
    @api.depends('g30_custom_pump_ns')
    def _g30_custom_tremie1_ns(self):
        for rec in self:
            rec.g30_custom_tremie1_ns = rec.g30_custom_pump_ns + rec.g30_tremie1_newslump
    def _g30_custom_tremie1_nsv2(self):
        return self.g30_custom_tremie1_ns

    @api.depends('g35_custom_pump_ns')
    def _g35_custom_tremie1_ns(self):
        for rec in self:
            rec.g35_custom_tremie1_ns = rec.g35_custom_pump_ns + rec.g35_tremie1_newslump
    def _g35_custom_tremie1_nsv2(self):
        return self.g35_custom_tremie1_ns

    @api.depends('g40_custom_pump_ns')
    def _g40_custom_tremie1_ns(self):
        for rec in self:
            rec.g40_custom_tremie1_ns = rec.g40_custom_pump_ns + rec.g40_tremie1_newslump
    def _g40_custom_tremie1_nsv2(self):
        return self.g40_custom_tremie1_ns

    @api.depends('g40_custom_tremie1_ns')
    def _g45_custom_tremie1_ns(self):
        for rec in self:
            rec.g45_custom_tremie1_ns = rec.g40_custom_tremie1_ns + rec.g45_tremie1_newslump
    def _g45_custom_tremie1_nsv2(self):
        return self.g45_custom_tremie1_ns

    @api.depends('g45_custom_tremie1_ns')
    def _g50_custom_tremie1_ns(self):
        for rec in self:
            rec.g50_custom_tremie1_ns = rec.g45_custom_tremie1_ns + rec.g50_tremie1_newslump
    def _g50_custom_tremie1_nsv2(self):
        return self.g50_custom_tremie1_ns

    # Tremie 2 Mix

    @api.depends('g30_custom_tremie1_ns')
    def _g30_custom_tremie2_ns(self):
        for rec in self:
            rec.g30_custom_tremie2_ns = rec.g30_custom_tremie1_ns + rec.g30_tremie2_newslump
    def _g30_custom_tremie2_nsv2(self):
        return self.g30_custom_tremie2_ns

    @api.depends('g35_custom_tremie1_ns')
    def _g35_custom_tremie2_ns(self):
        for rec in self:
            rec.g35_custom_tremie2_ns = rec.g35_custom_tremie1_ns + rec.g35_tremie2_newslump
    def _g35_custom_tremie2_nsv2(self):
        return self.g35_custom_tremie2_ns

    @api.depends('g40_custom_tremie1_ns')
    def _g40_custom_tremie2_ns(self):
        for rec in self:
            rec.g40_custom_tremie2_ns = rec.g40_custom_tremie1_ns + rec.g40_tremie2_newslump
    def _g40_custom_tremie2_nsv2(self):
        return self.g40_custom_tremie2_ns

    @api.depends('g45_custom_tremie1_ns')
    def _g45_custom_tremie2_ns(self):
        for rec in self:
            rec.g45_custom_tremie2_ns = rec.g45_custom_tremie1_ns + rec.g45_tremie2_newslump
    def _g45_custom_tremie2_nsv2(self):
        return self.g45_custom_tremie2_ns

    @api.depends('g45_custom_tremie2_ns')
    def _g50_custom_tremie2_ns(self):
        for rec in self:
            rec.g50_custom_tremie2_ns = rec.g45_custom_tremie2_ns + rec.g50_tremie2_newslump
    def _g50_custom_tremie2_nsv2(self):
        return self.g50_custom_tremie2_ns

    # Tremie 3 Mix

    @api.depends('g30_custom_tremie2_ns')
    def _g30_custom_tremie3_ns(self):
        for rec in self:
            rec.g30_custom_tremie3_ns = rec.g30_custom_tremie2_ns + rec.g30_tremie3_newslump
    def _g30_custom_tremie3_nsv2(self):
        return self.g30_custom_tremie3_ns

    @api.depends('g35_custom_tremie2_ns')
    def _g35_custom_tremie3_ns(self):
        for rec in self:
            rec.g35_custom_tremie3_ns = rec.g35_custom_tremie2_ns + rec.g35_tremie3_newslump
    def _g35_custom_tremie3_nsv2(self):
        return self.g35_custom_tremie3_ns

    @api.depends('g40_custom_tremie2_ns')
    def _g40_custom_tremie3_ns(self):
        for rec in self:
            rec.g40_custom_tremie3_ns = rec.g40_custom_tremie2_ns + rec.g40_tremie3_newslump
    def _g40_custom_tremie3_nsv2(self):
        return self.g40_custom_tremie3_ns

    @api.depends('g45_custom_tremie2_ns')
    def _g45_custom_tremie3_ns(self):
        for rec in self:
            rec.g45_custom_tremie3_ns = rec.g45_custom_tremie2_ns + rec.g45_tremie3_newslump
    def _g45_custom_tremie3_nsv2(self):
        return self.g45_custom_tremie3_ns

    @api.depends('g45_custom_tremie3_ns')
    def _g50_custom_tremie3_ns(self):
        for rec in self:
            rec.g50_custom_tremie3_ns = rec.g45_custom_tremie3_ns + rec.g50_tremie3_newslump
    def _g50_custom_tremie3_nsv2(self):
        return self.g50_custom_tremie3_ns

    @api.depends('g50_custom_tremie3_ns')
    def _g55_custom_tremie3_ns(self):
        for rec in self:
            rec.g55_custom_tremie3_ns = rec.g50_custom_tremie3_ns + rec.g55_tremie3_newslump
    def _g55_custom_tremie3_nsv2(self):
        return self.g55_custom_tremie3_ns

    @api.depends('g55_custom_tremie3_ns')
    def _g60_custom_tremie3_ns(self):
        for rec in self:
            rec.g60_custom_tremie3_ns = rec.g55_custom_tremie3_ns + rec.g60_tremie3_newslump
    def _g60_custom_tremie3_nsv2(self):
        return self.g60_custom_tremie3_ns


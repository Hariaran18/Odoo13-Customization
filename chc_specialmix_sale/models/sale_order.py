from odoo import models, fields, api

class gradeClass_FS(models.Model):
    _name = "grade.ids"
    grade_line = fields.Many2one('sale.order', string='Grade Reference', ondelete='cascade', index=True, copy=False)
    name = fields.Char(string="Grade")
    table_header = fields.Many2one('header.ids', string="Table Number")
    price_normal = fields.Integer(string="Full OPC Normal(Price)",default="0")
    specialcode_normal = fields.Char(string="Full OPC Normal(special code)")
    price_pump = fields.Integer(string="Full OPC Pump(Price)",default="0")
    specialcode_pump = fields.Char(string="Full OPC Pump(special code)")
    price_t1 = fields.Integer(string="Full OPC T1(Price)",default="0")
    specialcode_t1 = fields.Char(string="Full OPC T1(special code)")
    price_t2 = fields.Integer(string="Full OPC T2(Price)",default="0")
    specialcode_t2 = fields.Char(string="Full OPC T2(special code)")
    price_t3 = fields.Integer(string="Full OPC T3(Price)",default="0")
    specialcode_t3 = fields.Char(string="Full OPC T3(special code)")

class SaleOrder_FS(models.Model):
    _inherit = "sale.order"
    payment_days_chc_spclmix = fields.Text(string="Payment Terms")
    rebate_chc_spclmix = fields.Char(string="Rebate")
    project_reply_chc_spclmix = fields.Text(string="Project Reply")
    reference_link_chc_spclmix = fields.Many2one('ir.attachment', string='Reference Link')
    special_remarks_spclmix = fields.Text(string="Special Remarks")
    price_variation_clause_spclmix = fields.Text(string="Price Variation Clause",
                                                  default="Our prices are subject to price fluctuation of raw materials (i.e.: bulk cement, fuel, sand, aggregates and etc.) for all orders in progress of deliveries. The difference between market revised price and our quotation calculation will be chargeable to you accordingly.")

    quotation_approver_spclmix = fields.Many2one('res.partner',string="Quotation Approver1")
    quotation_approver_spclmix_v1 = fields.Many2one('res.users', string="Quotation Approver",
                                                 domain=['|', ('id', '=', 88), ('id', '=', 98)])
    quotation_approver_signature = fields.Many2one('ir.attachment', string='Approver Signature')
    quotation_salesperson_signature = fields.Many2one('ir.attachment', string='Sales Person Signature')

    jkr_mix_chc_specialmix= fields.Char(string="JKR Mix")
    waterproof_mix_specialmix = fields.Char(string="Water Proofing Mix")
    chipping_mix_chc_specialmix = fields.Char(string="Chipping Mix")

    default_price_spclmix = fields.Integer(string="Grade Default  Price")
    g20_default_price_spclmix = fields.Integer(string="G20 Default Price")

    # First Grade Value
    ud_grade_ids = fields.One2many('grade.ids', 'grade_line', string="Grade Value")
    # set default values for calculation fields
    mortar13_normal_spclmix = fields.Integer(string="Mortar 1:3 Mix Value", default=13)
    mortar14_normal_spclmix = fields.Integer(string="Mortar 1:4 Mix Value", default=13)
    mortar15_normal_spclmix = fields.Integer(string="Mortar 1:5 Mix Value", default=13)
    g15_normal_spclmix = fields.Integer(string="G15 Mix Value", default=5)
    g20_normal_spclmix = fields.Integer(string="G20 Mix Value", default=5)
    g25_normal_spclmix = fields.Integer(string="G25 Mix Value", default=9)
    g30_normal_spclmix = fields.Integer(string="G30 Mix Value", default=10)
    g35_normal_spclmix = fields.Integer(string="G35 Mix Value", default=11)
    g40_normal_spclmix = fields.Integer(string="G40 Mix Value", default=13)

    g25_pump_spclmix = fields.Integer(string="G25 Pump Mix Value", default=6)
    g30_pump_spclmix = fields.Integer(string="G30 Pump Mix Value", default=6)
    g35_pump_spclmix = fields.Integer(string="G35 Pump Mix Value", default=6)
    g40_pump_spclmix = fields.Integer(string="G40 Pump Mix Value", default=6)

    g30_tremie1_spclmix = fields.Integer(string="G30 Tremie1 Value", default=6)
    g35_tremie1_spclmix = fields.Integer(string="G35 Tremie1 Value", default=6)
    g40_tremie1_spclmix = fields.Integer(string="G40 Tremie1 Value", default=6)
    g45_tremie1_spclmix = fields.Integer(string="G45 Tremie1 Value", default=15)
    g50_tremie1_spclmix = fields.Integer(string="G50 Tremie1 Value", default=17)

    g30_tremie2_spclmix = fields.Integer(string="G30 Tremie2 Value", default=6)
    g35_tremie2_spclmix = fields.Integer(string="G35 Tremie2 Value", default=6)
    g40_tremie2_spclmix = fields.Integer(string="G40 Tremie2 Value", default=6)
    g45_tremie2_spclmix = fields.Integer(string="G45 Tremie2 Value", default=6)
    g50_tremie2_spclmix = fields.Integer(string="G50 Tremie2 Value", default=17)

    g30_tremie3_spclmix = fields.Integer(string="G30 Tremie3 Value", default=6)
    g35_tremie3_spclmix = fields.Integer(string="G35 Tremie3 Value", default=6)
    g40_tremie3_spclmix = fields.Integer(string="G40 Tremie3 Value", default=6)
    g45_tremie3_spclmix = fields.Integer(string="G45 Tremie3 Value", default=6)
    g50_tremie3_spclmix = fields.Integer(string="G50 Tremie3 Value", default=17)
    g55_tremie3_spclmix = fields.Integer(string="G55 Tremie3 Value", default=17)
    g60_tremie3_spclmix = fields.Integer(string="G60 Tremie3 Value", default=17)

    # store the calculated info into variable to pass in report- Normal Mix
    mortar13_custom = fields.Integer(compute="_mortar13_custom_spclmix", string="Mortar 1:3 Value",inverse="_mortar13_custom_spclmixv2",readonly=False,store=True)
    mortar14_custom = fields.Integer(compute="_mortar14_custom_spclmix", string="Mortar 1:4 Value",inverse="_mortar14_custom_spclmixv2",readonly=False,store=True)
    mortar15_custom = fields.Integer(compute="_mortar15_custom_spclmix", string="Mortar 1:5 Value",inverse="_inverse_mortar15_custom_spclmixv2",readonly=False,store=True)
    g15_custom = fields.Integer(compute="_g15_custom_spclmix", string="G15 Value",inverse="_g15_custom_spclmixv2",readonly=False,store=True)
    #g20_custom = fields.Integer(compute="_g20_custom_spclmix", string="G20 Value",inverse="_g20_custom_spclmixv2",readonly=False,store=True)
    g25_custom = fields.Integer(compute="_g25_custom_spclmix", string="G25 Value",inverse="_g25_custom_spclmixv2",readonly=False,store=True)
    g30_custom = fields.Integer(compute="_g30_custom_spclmix", string="G30 Value",inverse="_g30_custom_spclmixv2",readonly=False,store=True)
    g35_custom = fields.Integer(compute="_g35_custom_spclmix", string="G35 Value",inverse="_g35_custom_spclmixv2",readonly=False,store=True)
    g40_custom = fields.Integer(compute="_g40_custom_spclmix", string="G40 Value",inverse="_g40_custom_spclmixv2",readonly=False,store=True)
    #Pump Mix
    g25_custom_pump = fields.Integer(compute="_g25_custom_pump", string="G25 Pump Value",inverse="_g25_custom_pumpv2",readonly=False,store=True)
    g30_custom_pump = fields.Integer(compute="_g30_custom_pump", string="G30 Pump Value",inverse="_g30_custom_pumpv2",readonly=False,store=True)
    g35_custom_pump = fields.Integer(compute="_g35_custom_pump", string="G35 Pump Value",inverse="_g35_custom_pumpv2",readonly=False,store=True)
    g40_custom_pump = fields.Integer(compute="_g40_custom_pump", string="G40 Pump Value",inverse="_g40_custom_pumpv2",readonly=False,store=True)
    # Tremie1 Mix
    g30_custom_tremie1 = fields.Integer(compute="_g30_custom_tremie1", string="G30 Tremie1 Value",inverse="_g30_custom_tremie1v2",readonly=False,store=True)
    g35_custom_tremie1 = fields.Integer(compute="_g35_custom_tremie1", string="G35 Tremie1 Value",inverse="_g35_custom_tremie1v2",readonly=False,store=True)
    g40_custom_tremie1 = fields.Integer(compute="_g40_custom_tremie1", string="G40 Tremie1 Value",inverse="_g40_custom_tremie1v2",readonly=False,store=True)
    g45_custom_tremie1 = fields.Integer(compute="_g45_custom_tremie1", string="G45 Tremie1 Value",inverse="_g45_custom_tremie1v2",readonly=False,store=True)
    g50_custom_tremie1 = fields.Integer(compute="_g50_custom_tremie1", string="G50 Tremie1 Value",inverse="_g50_custom_tremie1v2",readonly=False,store=True)
    # Tremie2 Mix
    g30_custom_tremie2 = fields.Integer(compute="_g30_custom_tremie2", string="G30 Tremie2 Value",inverse="_g30_custom_tremie2v2",readonly=False,store=True)
    g35_custom_tremie2 = fields.Integer(compute="_g35_custom_tremie2", string="G35 Tremie2 Value",inverse="_g35_custom_tremie2v2",readonly=False,store=True)
    g40_custom_tremie2 = fields.Integer(compute="_g40_custom_tremie2", string="G40 Tremie2 Value",inverse="_g40_custom_tremie2v2",readonly=False,store=True)
    g45_custom_tremie2 = fields.Integer(compute="_g45_custom_tremie2", string="G45 Tremie2 Value",inverse="_g45_custom_tremie2v2",readonly=False,store=True)
    g50_custom_tremie2 = fields.Integer(compute="_g50_custom_tremie2", string="G50 Tremie2 Value",inverse="_g50_custom_tremie2v2",readonly=False,store=True)
    # Tremie 3 Mix
    g30_custom_tremie3 = fields.Integer(compute="_g30_custom_tremie3", string="G30 Tremie3 Value",inverse="_g30_custom_tremie3v2",readonly=False,store=True)
    g35_custom_tremie3 = fields.Integer(compute="_g35_custom_tremie3", string="G35 Tremie3 Value",inverse="_g35_custom_tremie3v2",readonly=False,store=True)
    g40_custom_tremie3 = fields.Integer(compute="_g40_custom_tremie3", string="G40 Tremie3 Value",inverse="_g40_custom_tremie3v2",readonly=False,store=True)
    g45_custom_tremie3 = fields.Integer(compute="_g45_custom_tremie3", string="G45 Tremie3 Value",inverse="_g45_custom_tremie3v2",readonly=False,store=True)
    g50_custom_tremie3 = fields.Integer(compute="_g50_custom_tremie3", string="G50 Tremie3 Value",inverse="_g50_custom_tremie3v2",readonly=False,store=True)
    g55_custom_tremie3 = fields.Integer(compute="_g55_custom_tremie3", string="G55 Tremie3 Value",inverse="_g55_custom_tremie3v2",readonly=False,store=True)
    g60_custom_tremie3 = fields.Integer(compute="_g60_custom_tremie3", string="G60 Tremie3 Value",inverse="_g60_custom_tremie3v2",readonly=False,store=True)

    # Specail Mix Table with Codes
    ud_grade_title = fields.Text(string="Grade Title")
    ud_header_column1 = fields.Text(string="Header Title 1")
    ud_subtitle1 = fields.Text(string="Sub Title1")
    ud_header_column2 = fields.Text(string="Header Title 2")
    ud_subtitle2 = fields.Text(string="Sub Title2")
    ud_header_column3 = fields.Text(string="Header Title 3")
    ud_subtitle3 = fields.Text(string="Sub Title3")
    ud_header_column4 = fields.Text(string="Header Title 4")
    ud_subtitle4 = fields.Text(string="Sub Title4")
    ud_header_column5 = fields.Text(string="Header Title 5")
    ud_subtitle5 = fields.Text(string="Sub Title5")

    ud_grade_value1 = fields.Char(string="Grade Value 1")
    ud_opcnormal_value1 = fields.Char(string="OPC Normal Value 1")
    ud_opcnormal_spclcode1 = fields.Char(string="OPC Normal Special Code 1")

# Normal Mix
    @api.depends('default_price_spclmix')
    def _mortar15_custom_spclmix(self):
        for rec in self:
            rec.mortar15_custom = rec.default_price_spclmix + rec.mortar15_normal_spclmix
    def _inverse_mortar15_custom_spclmixv2(self):
        return self.mortar15_custom

    @api.depends('mortar15_custom')
    def _mortar14_custom_spclmix(self):
        for rec in self:
            rec.mortar14_custom = rec.mortar15_custom + rec.mortar14_normal_spclmix
    def _mortar14_custom_spclmixv2(self):
        return self.mortar14_custom

    @api.depends('mortar14_custom')
    def _mortar13_custom_spclmix(self):
        for rec in self:
            rec.mortar13_custom = rec.mortar14_custom + rec.mortar13_normal_spclmix
    def _mortar13_custom_spclmixv2(self):
        return self.mortar13_custom

    #def _g20_custom_spclmix(self):
     #   for rec in self:
      #      rec.g20_custom = rec.default_price_spclmix - rec.g20_normal_spclmix
    @api.depends('g20_default_price_spclmix')
    def _g15_custom_spclmix(self):
        for rec in self:
            rec.g15_custom = rec.g20_default_price_spclmix - rec.g15_normal_spclmix
    def _g15_custom_spclmixv2(self):
        return self.g15_custom

    @api.depends('g20_default_price_spclmix')
    def _g25_custom_spclmix(self):
        for rec in self:
            rec.g25_custom = rec.g20_default_price_spclmix + rec.g25_normal_spclmix
    def _g25_custom_spclmixv2(self):
        return self.g25_custom

    @api.depends('g25_custom')
    def _g30_custom_spclmix(self):
        for rec in self:
            rec.g30_custom = rec.g25_custom + rec.g30_normal_spclmix
    def _g30_custom_spclmixv2(self):
        return self.g30_custom

    @api.depends('g30_custom')
    def _g35_custom_spclmix(self):
        for rec in self:
            rec.g35_custom = rec.g30_custom + rec.g35_normal_spclmix
    def _g35_custom_spclmixv2(self):
        return self.g35_custom

    @api.depends('g35_custom')
    def _g40_custom_spclmix(self):
        for rec in self:
            rec.g40_custom = rec.g35_custom + rec.g40_normal_spclmix
    def _g40_custom_spclmixv2(self):
        return self.g40_custom

# Pump Mix
    @api.depends('g25_custom')
    def _g25_custom_pump(self):
        for rec in self:
            rec.g25_custom_pump = rec.g25_custom + rec.g25_pump_spclmix
    def _g25_custom_pumpv2(self):
        return self.g25_custom_pump

    @api.depends('g30_custom')
    def _g30_custom_pump(self):
        for rec in self:
            rec.g30_custom_pump = rec.g30_custom + rec.g30_pump_spclmix
    def _g30_custom_pumpv2(self):
        return self.g30_custom_pump

    @api.depends('g35_custom')
    def _g35_custom_pump(self):
        for rec in self:
            rec.g35_custom_pump = rec.g35_custom + rec.g35_pump_spclmix
    def _g35_custom_pumpv2(self):
        return self.g35_custom_pump

    @api.depends('g40_custom')
    def _g40_custom_pump(self):
        for rec in self:
            rec.g40_custom_pump = rec.g40_custom + rec.g40_pump_spclmix
    def _g40_custom_pumpv2(self):
        return self.g40_custom_pump

# Tremie 1 Mix
    @api.depends('g30_custom_pump')
    def _g30_custom_tremie1(self):
        for rec in self:
            rec.g30_custom_tremie1 = rec.g30_custom_pump + rec.g30_tremie1_spclmix
    def _g30_custom_tremie1v2(self):
        return self.g30_custom_tremie1

    @api.depends('g35_custom_pump')
    def _g35_custom_tremie1(self):
        for rec in self:
            rec.g35_custom_tremie1 = rec.g35_custom_pump + rec.g35_tremie1_spclmix
    def _g35_custom_tremie1v2(self):
        return self.g35_custom_tremie1

    @api.depends('g40_custom_pump')
    def _g40_custom_tremie1(self):
        for rec in self:
            rec.g40_custom_tremie1 = rec.g40_custom_pump + rec.g40_tremie1_spclmix
    def _g40_custom_tremie1v2(self):
        return self.g40_custom_tremie1

    @api.depends('g40_custom_tremie1')
    def _g45_custom_tremie1(self):
        for rec in self:
            rec.g45_custom_tremie1 = rec.g40_custom_tremie1 + rec.g45_tremie1_spclmix
    def _g45_custom_tremie1v2(self):
        return self.g45_custom_tremie1

    @api.depends('g45_custom_tremie1')
    def _g50_custom_tremie1(self):
        for rec in self:
            rec.g50_custom_tremie1 = rec.g45_custom_tremie1 + rec.g50_tremie1_spclmix
    def _g50_custom_tremie1v2(self):
        return self.g50_custom_tremie1

# Tremie 2 Mix

    @api.depends('g30_custom_tremie1')
    def _g30_custom_tremie2(self):
        for rec in self:
            rec.g30_custom_tremie2 = rec.g30_custom_tremie1 + rec.g30_tremie2_spclmix
    def _g30_custom_tremie2v2(self):
        return self.g30_custom_tremie2

    @api.depends('g35_custom_tremie1')
    def _g35_custom_tremie2(self):
        for rec in self:
            rec.g35_custom_tremie2 = rec.g35_custom_tremie1 + rec.g35_tremie2_spclmix
    def _g35_custom_tremie2v2(self):
        return self.g35_custom_tremie2

    @api.depends('g40_custom_tremie1')
    def _g40_custom_tremie2(self):
        for rec in self:
            rec.g40_custom_tremie2 = rec.g40_custom_tremie1 + rec.g40_tremie2_spclmix
    def _g40_custom_tremie2v2(self):
        return self.g40_custom_tremie2

    @api.depends('g45_custom_tremie1')
    def _g45_custom_tremie2(self):
        for rec in self:
            rec.g45_custom_tremie2 = rec.g45_custom_tremie1 + rec.g45_tremie2_spclmix
    def _g45_custom_tremie2v2(self):
        return self.g45_custom_tremie2

    @api.depends('g45_custom_tremie2')
    def _g50_custom_tremie2(self):
        for rec in self:
            rec.g50_custom_tremie2 = rec.g45_custom_tremie2 + rec.g50_tremie2_spclmix
    def _g50_custom_tremie2v2(self):
        return self.g50_custom_tremie2

# Tremie 3 Mix
    @api.depends('g30_custom_tremie2')
    def _g30_custom_tremie3(self):
        for rec in self:
            rec.g30_custom_tremie3 = rec.g30_custom_tremie2 + rec.g30_tremie3_spclmix
    def _g30_custom_tremie3v2(self):
        return self.g30_custom_tremie3

    @api.depends('g35_custom_tremie2')
    def _g35_custom_tremie3(self):
        for rec in self:
            rec.g35_custom_tremie3 = rec.g35_custom_tremie2 + rec.g35_tremie3_spclmix
    def _g35_custom_tremie3v2(self):
        return self.g35_custom_tremie3

    @api.depends('g40_custom_tremie2')
    def _g40_custom_tremie3(self):
        for rec in self:
            rec.g40_custom_tremie3 = rec.g40_custom_tremie2 + rec.g40_tremie3_spclmix
    def _g40_custom_tremie3v2(self):
        return self.g40_custom_tremie3

    @api.depends('g45_custom_tremie2')
    def _g45_custom_tremie3(self):
        for rec in self:
            rec.g45_custom_tremie3 = rec.g45_custom_tremie2 + rec.g45_tremie3_spclmix
    def _g45_custom_tremie3v2(self):
        return self.g45_custom_tremie3

    @api.depends('g45_custom_tremie3')
    def _g50_custom_tremie3(self):
        for rec in self:
            rec.g50_custom_tremie3 = rec.g45_custom_tremie3 + rec.g50_tremie3_spclmix
    def _g50_custom_tremie3v2(self):
        return self.g50_custom_tremie3

    @api.depends('g50_custom_tremie3')
    def _g55_custom_tremie3(self):
        for rec in self:
            rec.g55_custom_tremie3 = rec.g50_custom_tremie3 + rec.g55_tremie3_spclmix
    def _g55_custom_tremie3v2(self):
        return self.g55_custom_tremie3

    @api.depends('g55_custom_tremie3')
    def _g60_custom_tremie3(self):
        for rec in self:
            rec.g60_custom_tremie3 = rec.g55_custom_tremie3 + rec.g60_tremie3_spclmix
    def _g60_custom_tremie3v2(self):
        return self.g60_custom_tremie3


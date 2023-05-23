from odoo import models, fields, api

class SaleOrder_FS(models.Model):
    _inherit = "sale.order"
    jkr_mix_chc_proposal = fields.Char(string="JKR Mix")
    waterproof_mix_chc_proposal = fields.Char(string="Water Proofing Mix")
    chipping_mix_chc_proposal = fields.Char(string="Chipping Mix")
    project_reply_chc_proposal = fields.Text(string="Project Reply")
    reference_link_chc_proposal = fields.Many2one('ir.attachment', string='Reference Link')

    termsandconditions_proposal= fields.Many2one("terms.conditions", string="Terms and Conditions")

    default_price_proposal = fields.Integer(string="Grade Default  Price")
    g20_default_price_proposal = fields.Integer(string="G20 Default  Price")

    # set default values for calculation fields
    mortar13_normal_proposal = fields.Integer(string="Mortar 1:3 Mix Value", default=13)
    mortar14_normal_proposal = fields.Integer(string="Mortar 1:4 Mix Value", default=13)
    mortar15_normal_proposal = fields.Integer(string="Mortar 1:5 Mix Value", default=13)
    g15_normal_proposal = fields.Integer(string="G15 Mix Value", default=5)
    g20_normal_proposal = fields.Integer(string="G20 Mix Value", default=5)
    g25_normal_proposal = fields.Integer(string="G25 Mix Value", default=9)
    g30_normal_proposal = fields.Integer(string="G30 Mix Value", default=10)
    g35_normal_proposal = fields.Integer(string="G35 Mix Value", default=11)
    g40_normal_proposal = fields.Integer(string="G40 Mix Value", default=13)

    g25_pump_proposal = fields.Integer(string="G25 Pump Mix Value", default=6)
    g30_pump_proposal = fields.Integer(string="G30 Pump Mix Value", default=6)
    g35_pump_proposal = fields.Integer(string="G35 Pump Mix Value", default=6)
    g40_pump_proposal = fields.Integer(string="G40 Pump Mix Value", default=6)

    g30_tremie1_proposal = fields.Integer(string="G30 Tremie1 Value", default=6)
    g35_tremie1_proposal = fields.Integer(string="G35 Tremie1 Value", default=6)
    g40_tremie1_proposal = fields.Integer(string="G40 Tremie1 Value", default=6)
    g45_tremie1_proposal = fields.Integer(string="G45 Tremie1 Value", default=15)
    g50_tremie1_proposal = fields.Integer(string="G50 Tremie1 Value", default=17)

    g30_tremie2_proposal = fields.Integer(string="G30 Tremie2 Value", default=6)
    g35_tremie2_proposal = fields.Integer(string="G35 Tremie2 Value", default=6)
    g40_tremie2_proposal = fields.Integer(string="G40 Tremie2 Value", default=6)
    g45_tremie2_proposal = fields.Integer(string="G45 Tremie2 Value", default=6)
    g50_tremie2_proposal = fields.Integer(string="G50 Tremie2 Value", default=17)

    g30_tremie3_proposal = fields.Integer(string="G30 Tremie3 Value", default=6)
    g35_tremie3_proposal = fields.Integer(string="G35 Tremie3 Value", default=6)
    g40_tremie3_proposal = fields.Integer(string="G40 Tremie3 Value", default=6)
    g45_tremie3_proposal = fields.Integer(string="G45 Tremie3 Value", default=6)
    g50_tremie3_proposal = fields.Integer(string="G50 Tremie3 Value", default=17)
    g55_tremie3_proposal = fields.Integer(string="G55 Tremie3 Value", default=17)
    g60_tremie3_proposal = fields.Integer(string="G60 Tremie3 Value", default=17)

    # store the calculated info into variable to pass in report- Normal Mix
    mortar13_custom_prop = fields.Integer(compute="_mortar13_custom_proposal", string="Mortar 1:3 Value",inverse="_mortar13_custom_proposalv2",readonly=False,store=True)
    mortar14_custom_prop = fields.Integer(compute="_mortar14_custom_proposal", string="Mortar 1:4 Value",inverse="_mortar14_custom_proposalv2",readonly=False,store=True)
    mortar15_custom_prop = fields.Integer(compute="_mortar15_custom_proposal", string="Mortar 1:5 Value",inverse="_mortar15_custom_proposalv2",readonly=False,store=True)
    g15_custom_prop = fields.Integer(compute="_g15_custom_proposal", string="G15 Value",inverse="_g15_custom_proposalv2",readonly=False,store=True)
    #g20_custom_prop = fields.Integer(compute="_g20_custom_proposal", string="G20 Value",inverse="_g15_custom_proposalv2",readonly=False,store=True)
    g25_custom_prop = fields.Integer(compute="_g25_custom_proposal", string="G25 Value",inverse="_g25_custom_proposalv2",readonly=False,store=True)
    g30_custom_prop = fields.Integer(compute="_g30_custom_proposal", string="G30 Value",inverse="_g30_custom_proposalv2",readonly=False,store=True)
    g35_custom_prop = fields.Integer(compute="_g35_custom_proposal", string="G35 Value",inverse="_g35_custom_proposalv2",readonly=False,store=True)
    g40_custom_prop = fields.Integer(compute="_g40_custom_proposal", string="G40 Value",inverse="_g40_custom_proposalv2",readonly=False,store=True)
    # Pump Mix
    g25_custom_pump_prop = fields.Integer(compute="_g25_custom_pump_prop", string="G25 Pump Value",inverse="_g25_custom_pump_propv2",readonly=False,store=True)
    g30_custom_pump_prop = fields.Integer(compute="_g30_custom_pump_prop", string="G30 Pump Value",inverse="_g30_custom_pump_propv2",readonly=False,store=True)
    g35_custom_pump_prop = fields.Integer(compute="_g35_custom_pump_prop", string="G35 Pump Value",inverse="_g35_custom_pump_propv2",readonly=False,store=True)
    g40_custom_pump_prop = fields.Integer(compute="_g40_custom_pump_prop", string="G40 Pump Value",inverse="_g40_custom_pump_propv2",readonly=False,store=True)
    # Tremie1 Mix
    g30_custom_tremie1_prop = fields.Integer(compute="_g30_custom_tremie1_prop", string="G30 Tremie1 Value",inverse="_g30_custom_tremie1_propv2",readonly=False,store=True)
    g35_custom_tremie1_prop = fields.Integer(compute="_g35_custom_tremie1_prop", string="G35 Tremie1 Value",inverse="_g35_custom_tremie1_propv2",readonly=False,store=True)
    g40_custom_tremie1_prop = fields.Integer(compute="_g40_custom_tremie1_prop", string="G40 Tremie1 Value",inverse="_g40_custom_tremie1_propv2",readonly=False,store=True)
    g45_custom_tremie1_prop = fields.Integer(compute="_g45_custom_tremie1_prop", string="G45 Tremie1 Value",inverse="_g45_custom_tremie1_propv2",readonly=False,store=True)
    g50_custom_tremie1_prop = fields.Integer(compute="_g50_custom_tremie1_prop", string="G50 Tremie1 Value",inverse="_g50_custom_tremie1_propv2",readonly=False,store=True)
    # Tremie2 Mix
    g30_custom_tremie2_prop = fields.Integer(compute="_g30_custom_tremie2_prop", string="G30 Tremie2 Value",inverse="_g30_custom_tremie2_propv2",readonly=False,store=True)
    g35_custom_tremie2_prop = fields.Integer(compute="_g35_custom_tremie2_prop", string="G35 Tremie2 Value",inverse="_g35_custom_tremie2_propv2",readonly=False,store=True)
    g40_custom_tremie2_prop = fields.Integer(compute="_g40_custom_tremie2_prop", string="G40 Tremie2 Value",inverse="_g40_custom_tremie2_propv2",readonly=False,store=True)
    g45_custom_tremie2_prop = fields.Integer(compute="_g45_custom_tremie2_prop", string="G45 Tremie2 Value",inverse="_g45_custom_tremie2_propv2",readonly=False,store=True)
    g50_custom_tremie2_prop = fields.Integer(compute="_g50_custom_tremie2_prop", string="G50 Tremie2 Value",inverse="_g50_custom_tremie2_propv2",readonly=False,store=True)
    # Tremie 3 Mix
    g30_custom_tremie3_prop = fields.Integer(compute="_g30_custom_tremie3_prop", string="G30 Tremie3 Value",inverse="_g30_custom_tremie3_propv2",readonly=False,store=True)
    g35_custom_tremie3_prop = fields.Integer(compute="_g35_custom_tremie3_prop", string="G35 Tremie3 Value",inverse="_g35_custom_tremie3_propv2",readonly=False,store=True)
    g40_custom_tremie3_prop = fields.Integer(compute="_g40_custom_tremie3_prop", string="G40 Tremie3 Value",inverse="_g40_custom_tremie3_propv2",readonly=False,store=True)
    g45_custom_tremie3_prop = fields.Integer(compute="_g45_custom_tremie3_prop", string="G45 Tremie3 Value",inverse="_g45_custom_tremie3_propv2",readonly=False,store=True)
    g50_custom_tremie3_prop = fields.Integer(compute="_g50_custom_tremie3_prop", string="G50 Tremie3 Value",inverse="_g50_custom_tremie3_propv2",readonly=False,store=True)
    g55_custom_tremie3_prop = fields.Integer(compute="_g55_custom_tremie3_prop", string="G55 Tremie3 Value",inverse="_g55_custom_tremie3_propv2",readonly=False,store=True)
    g60_custom_tremie3_prop = fields.Integer(compute="_g60_custom_tremie3_prop", string="G60 Tremie3 Value",inverse="_g60_custom_tremie3_propv2",readonly=False,store=True)

    # Normal Mix
    @api.depends('default_price_proposal')
    def _mortar15_custom_proposal(self):
        for rec in self:
            rec.mortar15_custom_prop = rec.default_price_proposal + rec.mortar15_normal_proposal
    def _mortar15_custom_proposalv2(self):
        return self.mortar15_custom_prop

    @api.depends('mortar15_custom_prop')
    def _mortar14_custom_proposal(self):
        for rec in self:
            rec.mortar14_custom_prop = rec.mortar15_custom_prop + rec.mortar14_normal_proposal
    def _mortar14_custom_proposalv2(self):
        return self.mortar14_custom_prop

    @api.depends('mortar14_custom_prop')
    def _mortar13_custom_proposal(self):
        for rec in self:
            rec.mortar13_custom_prop = rec.mortar14_custom_prop + rec.mortar13_normal_proposal
    def _mortar13_custom_proposalv2(self):
        return self.mortar13_custom_prop

    #def _g20_custom_newslump(self):
     #   for rec in self:
       #     rec.g20_custom_ns = rec.default_price_newslump - rec.g20_normal_newslump
    @api.depends('g20_default_price_proposal')
    def _g15_custom_proposal(self):
        for rec in self:
            rec.g15_custom_prop = rec.g20_default_price_proposal - rec.g15_normal_proposal
    def _g15_custom_proposalv2(self):
        return self.g15_custom_prop

    @api.depends('g20_default_price_proposal')
    def _g25_custom_proposal(self):
        for rec in self:
            rec.g25_custom_prop = rec.g20_default_price_proposal + rec.g25_normal_proposal
    def _g25_custom_proposalv2(self):
        return self.g25_custom_prop

    @api.depends('g25_custom_prop')
    def _g30_custom_proposal(self):
        for rec in self:
            rec.g30_custom_prop = rec.g25_custom_prop + rec.g30_normal_proposal
    def _g30_custom_proposalv2(self):
        return self.g30_custom_prop

    @api.depends('g30_custom_prop')
    def _g35_custom_proposal(self):
        for rec in self:
            rec.g35_custom_prop = rec.g30_custom_prop + rec.g35_normal_proposal
    def _g35_custom_proposalv2(self):
        return self.g35_custom_prop

    @api.depends('g35_custom_prop')
    def _g40_custom_proposal(self):
        for rec in self:
            rec.g40_custom_prop = rec.g35_custom_prop + rec.g40_normal_proposal
    def _g40_custom_proposalv2(self):
        return self.g40_custom_prop

    # Pump Mix
    @api.depends('g25_custom_prop')
    def _g25_custom_pump_prop(self):
        for rec in self:
            rec.g25_custom_pump_prop = rec.g25_custom_prop + rec.g25_pump_proposal
    def _g25_custom_pump_propv2(self):
        return self.g25_custom_pump_prop

    @api.depends('g30_custom_prop')
    def _g30_custom_pump_prop(self):
        for rec in self:
            rec.g30_custom_pump_prop = rec.g30_custom_prop + rec.g30_pump_proposal
    def _g30_custom_pump_propv2(self):
        return self.g30_custom_pump_prop

    @api.depends('g35_custom_prop')
    def _g35_custom_pump_prop(self):
        for rec in self:
            rec.g35_custom_pump_prop = rec.g35_custom_prop + rec.g35_pump_proposal
    def _g35_custom_pump_propv2(self):
        return self.g35_custom_pump_prop

    @api.depends('g40_custom_prop')
    def _g40_custom_pump_prop(self):
        for rec in self:
            rec.g40_custom_pump_prop = rec.g40_custom_prop + rec.g40_pump_proposal
    def _g40_custom_pump_propv2(self):
        return self.g40_custom_pump_prop

    # Tremie 1 Mix
    @api.depends('g30_custom_pump_prop')
    def _g30_custom_tremie1_prop(self):
        for rec in self:
            rec.g30_custom_tremie1_prop = rec.g30_custom_pump_prop + rec.g30_tremie1_proposal
    def _g30_custom_tremie1_propv2(self):
        return self.g30_custom_tremie1_prop

    @api.depends('g35_custom_pump_prop')
    def _g35_custom_tremie1_prop(self):
        for rec in self:
            rec.g35_custom_tremie1_prop = rec.g35_custom_pump_prop + rec.g35_tremie1_proposal
    def _g35_custom_tremie1_propv2(self):
        return self.g35_custom_tremie1_prop

    @api.depends('g40_custom_pump_prop')
    def _g40_custom_tremie1_prop(self):
        for rec in self:
            rec.g40_custom_tremie1_prop = rec.g40_custom_pump_prop + rec.g40_tremie1_proposal
    def _g40_custom_tremie1_propv2(self):
        return self.g45_custom_tremie1_prop

    @api.depends('g40_custom_tremie1_prop')
    def _g45_custom_tremie1_prop(self):
        for rec in self:
            rec.g45_custom_tremie1_prop = rec.g40_custom_tremie1_prop + rec.g45_tremie1_proposal
    def _g45_custom_tremie1_propv2(self):
        return self.g45_custom_tremie1_prop

    @api.depends('g45_custom_tremie1_prop')
    def _g50_custom_tremie1_prop(self):
        for rec in self:
            rec.g50_custom_tremie1_prop = rec.g45_custom_tremie1_prop + rec.g50_tremie1_proposal
    def _g50_custom_tremie1_propv2(self):
        return self.g50_custom_tremie1_prop

    # Tremie 2 Mix
    @api.depends('g30_custom_tremie1_prop')
    def _g30_custom_tremie2_prop(self):
        for rec in self:
            rec.g30_custom_tremie2_prop = rec.g30_custom_tremie1_prop + rec.g30_tremie2_proposal
    def _g30_custom_tremie2_propv2(self):
        return self.g30_custom_tremie2_prop

    @api.depends('g35_custom_tremie1_prop')
    def _g35_custom_tremie2_prop(self):
        for rec in self:
            rec.g35_custom_tremie2_prop = rec.g35_custom_tremie1_prop + rec.g35_tremie2_proposal
    def _g35_custom_tremie2_propv2(self):
        return self.g35_custom_tremie2_prop

    @api.depends('g40_custom_tremie1_prop')
    def _g40_custom_tremie2_prop(self):
        for rec in self:
            rec.g40_custom_tremie2_prop = rec.g40_custom_tremie1_prop + rec.g40_tremie2_proposal
    def _g40_custom_tremie2_propv2(self):
        return self.g40_custom_tremie2_prop

    @api.depends('g45_custom_tremie1_prop')
    def _g45_custom_tremie2_prop(self):
        for rec in self:
            rec.g45_custom_tremie2_prop = rec.g45_custom_tremie1_prop + rec.g45_tremie2_proposal
    def _g45_custom_tremie2_propv2(self):
        return self.g45_custom_tremie2_prop

    @api.depends('g45_custom_tremie2_prop')
    def _g50_custom_tremie2_prop(self):
        for rec in self:
            rec.g50_custom_tremie2_prop = rec.g45_custom_tremie2_prop + rec.g50_tremie2_proposal
    def _g50_custom_tremie2_propv2(self):
        return self.g50_custom_tremie2_prop

    # Tremie 3 Mix

    @api.depends('g30_custom_tremie2_prop')
    def _g30_custom_tremie3_prop(self):
        for rec in self:
            rec.g30_custom_tremie3_prop = rec.g30_custom_tremie2_prop + rec.g30_tremie3_proposal
    def _g30_custom_tremie3_propv2(self):
        return self.g30_custom_tremie3_prop

    @api.depends('g35_custom_tremie2_prop')
    def _g35_custom_tremie3_prop(self):
        for rec in self:
            rec.g35_custom_tremie3_prop = rec.g35_custom_tremie2_prop + rec.g35_tremie3_proposal
    def _g35_custom_tremie3_propv2(self):
        return self.g35_custom_tremie3_prop

    @api.depends('g40_custom_tremie2_prop')
    def _g40_custom_tremie3_prop(self):
        for rec in self:
            rec.g40_custom_tremie3_prop = rec.g40_custom_tremie2_prop + rec.g40_tremie3_proposal
    def _g40_custom_tremie3_propv2(self):
        return self.g40_custom_tremie3_prop

    @api.depends('g45_custom_tremie2_prop')
    def _g45_custom_tremie3_prop(self):
        for rec in self:
            rec.g45_custom_tremie3_prop = rec.g45_custom_tremie2_prop + rec.g45_tremie3_proposal
    def _g45_custom_tremie3_propv2(self):
        return self.g45_custom_tremie3_prop

    @api.depends('g45_custom_tremie3_prop')
    def _g50_custom_tremie3_prop(self):
        for rec in self:
            rec.g50_custom_tremie3_prop = rec.g45_custom_tremie3_prop + rec.g50_tremie3_proposal
    def _g50_custom_tremie3_propv2(self):
        return self.g50_custom_tremie3_prop

    @api.depends('g50_custom_tremie3_prop')
    def _g55_custom_tremie3_prop(self):
        for rec in self:
            rec.g55_custom_tremie3_prop = rec.g50_custom_tremie3_prop + rec.g55_tremie3_proposal
    def _g55_custom_tremie3_propv2(self):
        return self.g55_custom_tremie3_prop

    @api.depends('g55_custom_tremie3_prop')
    def _g60_custom_tremie3_prop(self):
        for rec in self:
            rec.g60_custom_tremie3_prop = rec.g55_custom_tremie3_prop + rec.g60_tremie3_proposal
    def _g60_custom_tremie3_propv2(self):
        return self.g60_custom_tremie3_prop


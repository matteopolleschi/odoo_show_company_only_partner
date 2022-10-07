# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    my_company_id = fields.Integer(string='My Company ID', compute='_compute_my_company_id')

    def _compute_my_company_id(self):
        for record in self:
            if record.parent_id:
                record.my_company_id = record.parent_id.id
            else:
                record.my_company_id = -1

# -*- coding: utf-8 -*-
# Copyright 2017-2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from datetime import datetime

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    team_ids = fields.Many2many(
        'crm.team',
        'product_tmpl_team_rel',
        'product_tmpl_id',
        'team_id',
        'Sales Channels',
    )
    manufacturer = fields.Char()
    manufactured_year = fields.Selection(
        [(num, str(num)) for num in reversed(
            range(1900, datetime.now().year+1))],
        'Manufactured Year',
    )
    model = fields.Char()
    product_state_id = fields.Many2one('product.state', 'Product State')
    purchase_category_id = fields.Many2one(
        'purchase.category',
        'Purchase Category',
    )
    evaluated_by_id = fields.Many2one('hr.employee', "Evaluated By")
    purchased_by_id = fields.Many2one('hr.employee', "Purchased By")
    shop_id = fields.Many2one('stock.warehouse', string='Shop Purchased')

    @api.multi
    def open_record(self):
        form_id = self.env.ref('product.product_template_only_form_view')
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'product.template',
            'res_id': self.id,
            'view_type': 'form',
            'view_mode': 'form',
            'view_id': form_id.id,
            'context': {},
            'target': 'current',
        }

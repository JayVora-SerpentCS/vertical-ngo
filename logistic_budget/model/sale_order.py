# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright 2013-2014 Camptocamp SA
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    budget_holder_id = fields.Many2one(
        'res.users',
        string='Budget Holder')
    date_budget_holder = fields.Datetime(
        'Budget Holder Validation Date')
    budget_holder_remark = fields.Text(
        'Budget Holder Remark')
    finance_officer_id = fields.Many2one(
        'res.users',
        string='Finance Officer')
    date_finance_officer = fields.Datetime(
        'Finance Officer Validation Date')
    finance_officer_remark = fields.Text(
        'Finance Officer Remark')

    @api.onchange('budget_holder_id')
    def onchange_set_date_budget_holder(self):
        self.date_budget_holder = fields.Datetime.now()

    @api.onchange('finance_officer_id')
    def onchange_set_date_finance_officer(self):
        self.date_finance_officer = fields.Datetime.now()
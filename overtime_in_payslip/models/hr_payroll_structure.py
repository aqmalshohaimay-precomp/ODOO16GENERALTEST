# -*- coding:utf-8 -*-

from odoo import api, fields, models, _


class HrPayrollStructure(models.Model):
    _inherit = 'hr.payroll.structure'

    @api.model
    def _get_default_rule_ids(self):
        res = super(HrPayrollStructure, self)._get_default_rule_ids()
        res.append((0, 0, {
                'name': 'Overtime',
                'sequence': 2,
                'code': 'OVERTIME',
                'category_id': self.env.ref('overtime_in_payslip.overtime_salary_rule_categ').id,
                'condition_select': 'none',
                'amount_select': 'code',
                'is_overtime_rule': True,
                'amount_python_compute': 'result = result = employee_overtime_amount(payslip)',
            }), )
        return res

    rule_ids = fields.One2many(
        'hr.salary.rule', 'struct_id',
        string='Salary Rules', default=_get_default_rule_ids)

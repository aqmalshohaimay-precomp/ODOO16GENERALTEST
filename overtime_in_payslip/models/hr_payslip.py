# -*- coding:utf-8 -*-

from odoo import api, fields, models, _


class HrPayslip(models.Model):
    _inherit = 'hr.payslip'

    def _get_base_local_dict(self):
        res = super()._get_base_local_dict()
        res.update({
            'employee_overtime_amount': employee_overtime_amount,
        })
        return res

    def _get_payslip_lines(self):
            result = super(HrPayslip, self)._get_payslip_lines()
            for line in result:
                description = ''
                used_type_ids = []
                salary_rule = self.env['hr.salary.rule'].browse(line['salary_rule_id'])
                if salary_rule.is_overtime_rule:
                    for bonus_line in self.env['employee.overtime'].search([
                        '|', '|', '&',
                        ('type', '=', 'employee'),
                        ('employee_id', '=', self.employee_id.id),
                        '&',
                        ('type', '=', 'department'),
                        ('department_id', '=', self.employee_id.department_id.id),
                        ('type', '=', 'all'),
                        ('state', '=', 'approve'),
                        ('date', '<=', self.date_to),
                        ('date', '>=', self.date_from)
                    ]):
                        if bonus_line.type_id.id not in used_type_ids:
                            description += description == '' and bonus_line.type_id.name or (
                                        ', ' + bonus_line.type_id.name)
                            used_type_ids.append(bonus_line.type_id.id)
                    line['description'] = description
            return result

    def _get_employee_overtime_amount(self):
        self.ensure_one()
        employee_bonus = self.env['employee.overtime'].search([
            '|', '|', '&',
            ('type', '=', 'employee'),
            ('employee_id', '=', self.employee_id.id),
            '&',
            ('type', '=', 'department'),
            ('department_id', '=', self.employee_id.department_id.id),
            ('type', '=', 'all'),
            ('state', '=', 'approve'),
            ('date', '<=', self.date_to),
            ('date', '>=', self.date_from),

        ])
        return sum(b.bonus_amount for b in employee_bonus)


class HrPayslipLine(models.Model):
    _inherit = 'hr.payslip.line'

    description = fields.Char()


class HrSalaryRule(models.Model):
    _inherit = 'hr.salary.rule'

    is_overtime_rule = fields.Boolean(default=False, readonly=True, copy=False)


def employee_overtime_amount(payslip):
    return payslip.dict._get_employee_overtime_amount()
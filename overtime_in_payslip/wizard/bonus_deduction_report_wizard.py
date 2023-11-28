# -*- coding: utf-8 -*-
from odoo import models, fields,_,api


class OvertimeReportWizard(models.TransientModel):
    _name = 'overtime.report.wizard'

    from_date = fields.Date(required=True)
    to_date = fields.Date(required=True)
    department_id = fields.Many2one("hr.department")
    employee_id = fields.Many2one("hr.employee")

    @api.onchange('employee_id')
    def onchange_department_id(self):
        for rec in self:
            if rec.employee_id:
                rec.department_id = rec.employee_id.department_id

    def print_report(self):
        """
        Print Report with data of filters
        :return:
        """

        datas = {'ids': self.env.context.get('active_ids', [])}
        res = self.read(['from_date', 'to_date', 'department_id', 'employee_id'])
        res = res and res[0] or {}
        datas['form'] = res
        return self.env.ref('overtime_in_payslip.report_employee_overtime').report_action([], data=datas)

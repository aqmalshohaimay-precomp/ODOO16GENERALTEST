# -*- coding: utf-8 -*-

from odoo import api, models


class EmployeeOvertimeReport(models.AbstractModel):
    _name = 'report.overtime_in_payslip.employee_overtime_report_doc'

    @api.model
    def _get_report_values(self, docids, data=None):
        data = data if data is not None else {}
        data_form = data['form']
        domain = [
            ('date', '<=', data_form['to_date']),
            ('date', '>=', data_form['from_date']),
            ('state', '=', 'approve')
        ]
        employee_id = data_form['employee_id']
        department_id = data_form['department_id']
        if employee_id:
            domain.append(('employee_id', '=', employee_id[0]))
        elif department_id:
            domain.append(('department_id', '=', department_id[0]))
        obj_model = self.env['employee.overtime']
        lines = obj_model.search(domain)
        data = dict(
                data,
                lines=lines,
                from_date=data_form['from_date'],
                to_date=data_form['to_date'],
                employee_id=employee_id,
                department_id=department_id
            )
        return {
            'doc_ids': data.get('ids', data.get('active_ids')),
            'doc_model': obj_model,
            'docs': self.env.user,
            'data': dict(
                data,
                lines=lines,
                from_date=data_form['from_date'],
                to_date=data_form['to_date'],
                employee_id=employee_id,
                department_id=department_id
            ),
        }

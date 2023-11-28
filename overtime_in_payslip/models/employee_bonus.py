from odoo import fields, models, api


class EmployeeBonus(models.Model):
    _name = 'employee.overtime'
    _inherit = ['mail.thread', "mail.activity.mixin"]

    name = fields.Char(compute="get_employee_name")
    type = fields.Selection([
        ('employee', 'Employee'),
        ('department', 'Department'),
        ('all', 'All Employees')
    ], default='employee', required=True)
    employee_id = fields.Many2one(comodel_name="hr.employee")
    no_of_days = fields.Float(default=0)
    department_id = fields.Many2one(comodel_name="hr.department")
    type_id = fields.Many2one(comodel_name="overtime.type", string="Bonus Type", required=True)
    date = fields.Date(required=True)
    bonus_amount = fields.Float(default=1)
    company_id = fields.Many2one(comodel_name="res.company", string='Company', default=lambda self: self.env.company)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('approve', 'Approved'),
        ('reject', 'Rejected'),
        ('cancel', 'Canceled')
    ], default="draft", string="Status", track_visibility="onchange")
    overtime_per = fields.Selection([('day', 'Days'), ('hour', 'Hours')], default="day", string="Per", track_visibility="onchange")
    description = fields.Text()
    @api.onchange('no_of_days', 'employee_id')
    def onchange_no_of_days(self):
        for rec in self:
            if rec.type == 'employee' and rec.employee_id and rec.employee_id.contract_id:
                if rec.overtime_per == 'day' and rec.no_of_days > 0:
                    rec.bonus_amount = (rec.employee_id.contract_id.wage / 30) * rec.no_of_days
                elif rec.overtime_per == 'hour' and rec.no_of_days > 0:
                    rec.bonus_amount = ((rec.employee_id.contract_id.wage / 30)/8) * rec.no_of_days


    @api.onchange('employee_id', 'date')
    def get_employee_name(self):
        for rec in self:
            name = ''
            if rec.type == 'employee' and rec.employee_id:
                rec.department_id = rec.employee_id.department_id.id
                name = rec.employee_id.name + ' '
            elif rec.type == 'department' and rec.department_id:
                name = rec.department_id.name + ' '
            elif rec.type == 'all':
                name = "Employees "
            name += rec.date and str(rec.date) or ''
            rec.name = name

    def action_approve(self):
        for rec in self:
            rec.state = "approve"

    def action_reject(self):
        for rec in self:
            rec.state = "reject"

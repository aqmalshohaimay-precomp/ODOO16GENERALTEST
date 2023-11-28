from odoo import fields, models, api


class OvertimeType(models.Model):
    _name = 'overtime.type'

    name = fields.Char(required=True)

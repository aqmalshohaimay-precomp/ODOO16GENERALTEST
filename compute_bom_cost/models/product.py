from odoo import  models


class ProductCustom(models.Model):
    _inherit = 'product.template'


    #cron for auto compute the cost
    def _cron_auto_compute_cost(self):
        print('_cron_validate_do')
        product_obj=self.env['product.template'].search([('active','=',True)])
        for product in product_obj:
            product.button_bom_cost()
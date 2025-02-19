from odoo import api, fields, models

class AccountMove(models.Model):
    _inherit = 'account.move'

    company_currency_id = fields.Many2one(
        related="company_id.currency_id",
        string="devise de l'entreprise associée"
    )



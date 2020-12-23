# -*- coding: utf-8 -*-

from flectra import models, fields, api, _

# class openacademy(models.Model):
#     _name = 'openacademy.openacademy'

#     name = fields.Char()

class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'
    patient_name = fields.Char(String='Patient Name', required=True)
# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class ScheduledReminders(model.Model):
    _name = "Scheduled Reminders"
    _description = "Scheduled Reminders Model"

    Descreption = fields.Char('Mô tả', required=True)
    name = fields.Char('Tên')
    address = fields.Char('địa chỉ')
    phone = fields.Integer('số điện thoại')
    owner_id = fields.Many2one('res.partner', string='Owner')
    age = fields.Integer('Age', default=1)

    # @api.model
    # def send_email_maintain_reminder(self):
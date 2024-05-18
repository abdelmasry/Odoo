# models/digizilla.py
from odoo import models, fields

class Digizilla(models.Model):
    _name = 'digizilla'
    _description = 'Digizilla'

    name = fields.Char(string='Name', required=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string='Gender')
    country_id = fields.Many2one('res.country', string='Country')
    joining_date = fields.Date(string='Joining Date')
    tag_ids = fields.Many2many('digizilla.tag', string='Tags')
    customer_ids = fields.Many2many('res.partner', string='Customers')
    company_id = fields.Many2one('res.company', string='Company', required=True)
    notes = fields.Text(string='Notes', compute='_compute_notes', store=True)
    comments = fields.Char(string='Comments')
    message_ids = fields.One2many('digizilla.message', 'digizilla_id', string='Messages')

    def _compute_notes(self):
        for record in self:
            record.notes = f"This is a note for {record.name}"

class DizigillaTag(models.Model):
    _name = 'digizilla.tag'
    _description = 'Digizilla Tag'

    name = fields.Char(string='Name')

class DizigillaMessage(models.Model):
    _name = 'digizilla.message'
    _description = 'Digizilla Message'

    digizilla_id = fields.Many2one('digizilla', string='Digizilla')
    message = fields.Text(string='Message')
    user_id = fields.Many2one('res.users', string='User')
    create_date = fields.Datetime(string='Create Date')
# -*- coding: utf-8 -*-
##############################################################################
#
#    Competitiveness Management
#    Copyright (C) 2013 No author.
#    No email
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


import re
from openerp import netsvc
from openerp.osv import osv, fields

class price_type(osv.osv):
    """Al cargar precios se debe poder restringuir por gurpo de usuario o usuario que tipos de precios tiene permitido cargar"""
    
    _name = 'competitiveness_management.price_type'
    _description = 'Al cargar precios se debe poder restringuir por gurpo de usuario'

    _columns = {
        'name': fields.char(string='Name', required=True, size=32),
        'code': fields.char(string='Code', required=True, size=2),
        'require_invoice_info': fields.boolean(string='Requiere Invoice Info'),
        'price_record_id': fields.one2many('competitiveness_management.price_record', 'price_type_id', string='&lt;no label&gt;'), 
        'record_responsibility_ids': fields.one2many('competitiveness_management.record_responsibility', 'price_type_id', string='record_responsibility_ids'), 
    }

    _defaults = {
    }


    _constraints = [
    ]




price_type()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

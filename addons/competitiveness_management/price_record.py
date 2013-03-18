# -*- coding: utf-8 -*-
##############################################################################
#
#    Agrihold Costs and Competitiveness Management
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
import netsvc
from osv import osv, fields

class price_record(osv.osv):
    """"""
    _name = 'competitiveness_management.price_record'
    _description = 'price_record'

    _states_ = [
    ]

    _columns = {
        'product_id': fields.many2one('product.product', string='Product', required=True, context={'default_function_type':'formulated'}, domain=[('function_type','=','formulated')]),
        'commercial_name': fields.char(string='Commercial Name', readonly=True),
        'information_date': fields.date(string='Price Date', help=u"""Pre completar con la fecha actual""", required=True),
        'usd_price': fields.float(string='Price (USD)', required=True),
        'operative_id': fields.many2one('res.company', string='Operative', help=u"""Pre completar con la compania de contexto. Se debe filtrar solo por partners que tengan companias o definir criterio""", required=True),
        'supplier': fields.many2one('res.partner', string='Supplier'),
        'invoice_number': fields.char(string='Invoice Number'),
        'user': fields.many2one('res.users', string='User', help=u"""Completar con el usuario actual""", readonly=True),
        'record_date': fields.datetime(string='Recorded', help=u"""Completar con el usuario actual""", readonly=True),
        'price_type_id': fields.many2one('competitiveness_management.price_type', string='Price Type', required=True, ondelete='cascade'), 
        'price_term_id': fields.many2one('competitiveness_management.payment_term', string='Term'), 
    }

    _defaults = {
        'operative_id': lambda s,cr,uid,c: s.pool.get('res.company')._company_default_get(cr, uid, 'sgr.package_file', context=c),
    }


price_record()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

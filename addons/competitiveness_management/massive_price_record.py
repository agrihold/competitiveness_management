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


import netsvc
from osv import osv, fields

class massive_price_record(osv.osv):
    """
    Si cualquiera de los datos de esta vista se completa, entonces se pasa dicho valor por contexto a la tabla "price_record"    """
    _name = 'competitiveness_management.massive_price_record'
    _description = 'Massive Price Record'

    _columns = {
        'information_date': fields.date('Information Date'), 
        'operative': fields.many2one('res.partner', 'Operative'), 
        'user': fields.many2one('res.users', 'user', readonly=True), 
        'record_date': fields.datetime('record_date', readonly=True), 
        'product': fields.many2one('product.product', 'Product'), 
        'price_record_ids': fields.one2many('competitiveness_management.price_record', 'massive_price_record_id', 'Records'), 
        'price_type_id': fields.many2one('competitiveness_management.price_type', 'Price Type'), 
    }

    _defaults = {
    }




massive_price_record()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

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

class price_record(osv.osv):
    """
        """
    _name = 'competitiveness_management.price_record'
    _description = 'Price Records'

    _columns = {
        'information_date': fields.date('information_date', required=True), 
        'usd_price': fields.float('usd_price', required=True), 
        'operative': fields.many2one('res.partner', 'operative', required=True), 
        'user': fields.many2one('res.users', 'user', readonly=True), 
        'record_date': fields.datetime('record_date', readonly=True), 
        'price_type_id': fields.many2one('competitiveness_management.price_type', 'Price Type', required=True), 
    }

    _defaults = {
    }




price_record()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

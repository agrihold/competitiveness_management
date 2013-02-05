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

class price_type(osv.osv):
    """
        """
    _name = 'competitiveness_management.price_type'
    _description = 'Price Types'

    _columns = {
        'name': fields.char('Name', size=32, required=True), 
        'code': fields.char('Code', size=2, required=True), 
        'price_record_id': fields.one2many('competitiveness_management.price_record', 'price_type_id', '<no label>'), 
    }

    _defaults = {
    }




price_type()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

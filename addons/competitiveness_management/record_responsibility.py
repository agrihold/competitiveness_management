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

class record_responsibility(osv.osv):
    """"""
    _name = 'competitiveness_management.record_responsibility'
    _description = 'record_responsibility'

    _states_ = [
    ]

    _columns = {
        'interval_number': fields.integer(string='Interval Number', required=True),
        'interval_type': fields.selection([(u'days', u'Days'), (u'weeks', u'Weeks'), (u'months', u'Months')], string='Interval Unit', required=True),
        'nextcall': fields.datetime(string='Next Execution Date', required=True),
        'note': fields.text(string='Note'),
        'user_id': fields.many2one('res.users', string='User', required=True), 
        'price_type_id': fields.many2one('competitiveness_management.price_type', string='Price Type', required=True, ondelete='cascade'), 
    }

    _defaults = {
    }


record_responsibility()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

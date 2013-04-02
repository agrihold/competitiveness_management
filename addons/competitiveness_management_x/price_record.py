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

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import time
from openerp import pooler
from openerp.osv import fields, osv
from openerp.tools.translate import _
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT, DATETIME_FORMATS_MAP, float_compare
import openerp.addons.decimal_precision as dp
from openerp import netsvc

class price_record(osv.osv):
    """"""
    _name = 'competitiveness_management.price_record'
    _inherit = [ _name ]
    _order = 'information_date desc'
    
    def _compute_commercial_name(self, cr, uid, ids, name, arg, context=None):
        result = {}
        if context is None:
            context = {}
        
        for price_record in self.browse(cr, uid, ids, context=context):
            commercial = None
            for it_commercial in price_record.product_id.commercial_name_ids:
                if it_commercial.operative_id.id == price_record.operative_id.id:
                    commercial = it_commercial
                    break
            result[price_record.id] = commercial.name
        return result
        
    _columns = {
        'commercial_name': fields.function(_compute_commercial_name, method=True, string='Commercial Name', type='char'),
    }
    
    _defaults = {
        'information_date': fields.date.context_today,
    }


price_record()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

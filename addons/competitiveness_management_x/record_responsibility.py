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

class record_responsibility(osv.osv):
    """"""
    _name = 'competitiveness_management.record_responsibility'
    _inherit = [ _name ]
    
    _columns = {
        'ir_cron_id': fields.many2one('ir.cron', string='Cron', ondelete='cascade'),
    }
    
    def create_cron(self, cr, uid, ids, context=None):
        cron_obj = self.pool.get('ir.cron')
        vals = {}
        cron_obj.create(cr, uid, vals, context=context)
    
    def create(self, cr, uid, vals, context=None):
        super(record_responsibility, self).create(cr, uid, vals, context=context)
    


record_responsibility()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
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
from openerp import SUPERUSER_ID

class record_responsibility(osv.osv):
    """"""
    _name = 'competitiveness_management.record_responsibility'
    _inherit = [ _name, 'mail.thread']
    
    def _get_name(self, cr, uid, ids, fn, args, context=None):
        result = dict.fromkeys(ids, False)
        for resp in self.browse(cr, uid, ids, context=context):
            result[resp.id] = 'Alert to record ' + resp.price_type_id.name
        return result
    
    _columns = {
        'name': fields.function(_get_name, string='Name', type='char', size=128),
        'ir_cron_id': fields.many2one('ir.cron', string='Cron', ondelete='cascade'),
    }
    
    def update_cron(self, cr, uid, ids, context=None):
        cron_obj = self.pool.get('ir.cron')
        mail_group_obj = self.pool.get('mail.group')
        for resp in self.browse(cr, uid, ids, context=context):
            vals = {}
            vals['name'] = 'Record Responsibility ' + resp.user_id.name
            vals['user_id'] = 1
            vals['model'] = 'competitiveness_management.record_responsibility'
            vals['function'] = 'create_message_to_user'
            vals['args'] = '(' + str(resp.id) + ',)'
            vals['interval_type'] = resp.interval_type
            vals['nextcall'] = resp.nextcall
            vals['interval_number'] = resp.interval_number
            vals['active'] = True
            vals['doall'] = False
            vals['numbercall'] = -1
            
            if resp.ir_cron_id:
                cron_id = cron_obj.write(cr, uid, [resp.ir_cron_id.id], vals, context=context)
            else:
                cron_id = cron_obj.create(cr, uid, vals, context=context)
                self.write(cr, uid, [resp.id], {'ir_cron_id': cron_id}, context=context)
    
    def update_suscription(self, cr, uid, ids, context=None):
        if not context:
            context = {}
        context['update_suscription'] = True
        user_obj = self.pool.get('res.users');
        all_users_ids = user_obj.search(cr, uid, [], context=context)
        self.message_unsubscribe_users(cr, uid, ids, user_ids=all_users_ids, context=context)
        for resp in self.browse(cr, uid, ids, context=context):
            self.message_subscribe_users(cr, uid, ids, user_ids=[resp.user_id.id], context=context)
        
        ret = self.message_get_subscription_data(cr, uid, ids, context=context)
        
    def create(self, cr, uid, vals, context=None):
        if not context:
            context = {}
            
        new_id = super(record_responsibility, self).create(cr, uid, vals, context=context)
        self.update_cron(cr, uid, [new_id], context=context)
        self.update_suscription(cr, uid, [new_id], context=context)
        if not context.get('update_suscription', False):
            self.update_suscription(cr, uid, [new_id], context=context)
        return new_id
        
    def write(self, cr, uid, ids, vals, context=None):
        if not context:
            context = {}
        
        ret = super(record_responsibility, self).write(cr, uid, ids, vals, context=context)
        if not isinstance(ids, list):
            ids = [ids]
        self.update_cron(cr, uid, ids, context=context)
        if not context.get('update_suscription', False):
            self.update_suscription(cr, uid, ids, context=context)
        return ret
    
    def unlink(self, cr, uid, ids, context=None):
        if not isinstance(ids, list):
            ids = [ids]
        cron_obj = self.pool.get('ir.cron')
        for rec_res in self.browse(cr, uid, ids, context=context):
            cron_obj.unlink(cr, uid, [rec_res.ir_cron_id.id], context=context)
    
    def create_message_to_user(self, cr, uid, ids=None, context=None):
        if not isinstance(ids, list):
            ids = [ids]
        message_obj = self.pool.get('mail.message')
        for rec_res in self.browse(cr, SUPERUSER_ID, ids, context=context):
            user = rec_res.user_id
            subject = 'Alert to record ' + rec_res.price_type_id.name
            body = rec_res.note
            self.message_post(cr, SUPERUSER_ID, [rec_res.id], subject=subject, body=body, type='notification', subtype='mail.mt_comment', context=context)

record_responsibility()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

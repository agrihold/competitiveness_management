# -*- coding: utf-8 -*-
##############################################################################
#
#    
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


{   'active': False,
    'author': 'No author.',
    'category': 'base.module_category_hidden',
    'depends': ['competitiveness_management_x','report_aeroo'],
    'description': 'Competitiveness Management Reports',
    'init_xml': [],
    'installable': True,
    'license': 'AGPL-3',
    'name': 'Competitiveness Management Reports',
    'test': [],
    'demo': [   #'data/price_record_demo.xml',
                #'data/price.type.date2.csv',
],
    'data': [   'security/ejemplo_group.xml',
                'security/ir.model.access.csv',
                'report/price_analysis.xml',
],
    'version': 'No version',
   # 'auto_install': False,
   # 'application': True,
    'website': ''}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

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


{   'active': False,
    'author': 'No author.',
    'category': u'base.module_category_knowledge_management',
    'demo_xml': [],
    'depends': [u'product', u'sgr'],
    'description': u'Agrihold Costs and Competitiveness Management',
    'init_xml': [],
    'installable': True,
    'license': 'AGPL-3',
    'name': u'Agrihold Costs and Competitiveness Management',
    'test': [],
    'update_xml': [   u'security/competitiveness_management_group.xml',
                      u'view/product_view.xml',
                      u'view/commercial_name_view.xml',
                      u'view/payment_term_view.xml',
                      u'view/price_type_view.xml',
                      u'view/record_responsibility_view.xml',
                      u'view/price_record_view.xml',
                      u'view/competitiveness_management_menuitem.xml',
                      u'data/product_properties.xml',
                      u'data/commercial_name_properties.xml',
                      u'data/payment_term_properties.xml',
                      u'data/price_type_properties.xml',
                      u'data/record_responsibility_properties.xml',
                      u'data/price_record_properties.xml',
                      'security/ir.model.access.csv'],
    'version': 'No version',
    'website': ''}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

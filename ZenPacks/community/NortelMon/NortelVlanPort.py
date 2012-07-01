# ==============================================================================
# NortelVlanPort object class
#
# Zenoss community Zenpack for Avaya (Nortel) Devices
# version: 1.0
#
# (C) Copyright Jonathan Colon. All Rights Reserved.
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License along
#  with this program; if not, write to the Free Software Foundation, Inc.,
#  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
# ==============================================================================

__doc__="""NortelVlanPort object class"""
__author__ = "Jonathan Colon"
__copyright__ = "(C) Copyright Jonathan Colon. 2011. All Rights Reserved."
__license__ = "GPL"
__version__ = "1.0.0"

from Globals import DTMLFile
from Globals import InitializeClass
from Products.ZenRelations.RelSchema import *
from Products.ZenModel.ZenossSecurity import ZEN_VIEW, ZEN_CHANGE_SETTINGS
from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from ZenPacks.community.NortelMon import utils


class NortelVlanPort(DeviceComponent, ManagedEntity):

    portal_type = meta_type = 'NortelVlanPort'
    
    description = ''
    intname = ''
    vlanportindex = ''
    vlanportids = ''
    vlanporttype = ''
    vlanpvid = 0
    vlantag = ''

    monitor = True

    _properties = (
        {'id':'description', 'type':'string', 'mode':''},
        {'id':'intname', 'type':'string', 'mode':''},
        {'id':'vlanportindex', 'type':'string', 'mode':''},
        {'id':'vlanportids', 'type':'string', 'mode':''},
        {'id':'vlanporttype', 'type':'string', 'mode':''},
        {'id':'vlanpvid', 'type':'int', 'mode':''},
        {'id':'vlantag', 'type':'string', 'mode':''},
        )
    
    _relations = (
        ("NortelDevVlanPort", ToOne(ToManyCont,
            "ZenPacks.community.NortelMon.NortelDevice", "NortelVlanPort")),
        )


    factory_type_information = ( 
        { 
            'id'             : 'NortelVlanPort',
            'meta_type'      : 'NortelVlanPort',
            'description'    : """NortelVlanPort info""",
            'product'        : 'NortelMon',
            'immediate_view' : 'viewNortelVlanPort',
            'actions'        :
            ( 
                { 'id'            : 'viewHistory'
                , 'name'          : 'Modifications'
                , 'action'        : 'viewHistory'
                , 'permissions'   : (ZEN_VIEW, )
                },
            )
        },
                                )

    def viewName(self):
        """Pretty version human readable version of this object"""
        return self.id
    
    titleOrId = name = viewName
    
    def localinterface(self):
        try:
            return utils.findinterface(self, self.device(), self.intname)
        except:
            return self.intname


    def device(self):
        return self.NortelDevVlanPort()

    def manage_deleteComponent(self, REQUEST=None):
        """Delete NortelVlanPort component takes from Jane Curry"""
        url = None
        if REQUEST is not None:
            url = self.device().NortelVlanPort.absolute_url()
        self.getPrimaryParent()._delObject(self.id)

        if REQUEST is not None:
            REQUEST['RESPONSE'].redirect(url)
    
InitializeClass(NortelVlanPort)
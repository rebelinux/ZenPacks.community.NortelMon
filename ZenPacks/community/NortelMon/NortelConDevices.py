# ==============================================================================
# NortelFan object class
#
# Zenoss community Zenpack for Avaya (Nortel) Nortel Devices
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

__doc__="""NortelConDevices object class"""
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

class NortelConDevices(DeviceComponent, ManagedEntity):

    portal_type = meta_type = 'NortelConDevices'
    
    RemoteDevice = 0
    RemoteInterface = ''
    Connected = ''


    _properties = (
        {'id':'RemoteDevice', 'type':'string', 'mode':''},
        {'id':'RemoteInterface', 'type':'string', 'mode':''},
        {'id':'Connected', 'type':'string', 'mode':''},
        )
    
    _relations = (
        ("NortelDevConDevices", ToOne(ToManyCont,
            "ZenPacks.community.NortelMon.NortelDevice", "NortelConDevices")),
        )


    factory_type_information = ( 
        { 
            'id'             : 'NortelConDevices',
            'meta_type'      : 'NortelConDevices',
            'description'    : """NortelConDevices info""",
            'product'        : 'NortelMon',
            'immediate_view' : 'viewNortelConDevices',
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


    def device(self):
        return self.NortelDevConDevices()
    
    def manage_deleteComponent(self, REQUEST=None):
        """Delete NortelConDevices component takes from Jane Curry"""
        url = None
        if REQUEST is not None:
            url = self.device().NortelConDevices.absolute_url()
        self.getPrimaryParent()._delObject(self.id)

        if REQUEST is not None:
            REQUEST['RESPONSE'].redirect(url)

    def getRRDTemplates(self):
        """
        Return the RRD Templates list
        """
        templates = []
        for tname in [self.__class__.__name__]:
            templ = self.getRRDTemplateByName(tname)
            if templ: templates.append(templ)
        return templates
    
InitializeClass(NortelConDevices)

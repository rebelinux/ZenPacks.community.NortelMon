# ==============================================================================
# NortelTopology object class
#
# Zenoss community Zenpack for Avaya (Nortel) Passport Devices
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

__doc__="""NortelConDevice object class"""
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
from ZenPacks.community.NortelMon.utils import localinterface, getremotedevice, getremotedeviceIP
import re

class NortelConDevice(DeviceComponent, ManagedEntity):

    portal_type = meta_type = 'NortelConDevice'
    
    localint = ''
    baseport = 0
    baseportindex = 0
    ipaddr = '' 
    macaddr = ''
    sysname  = ''
    fdbport = ''

    _properties = (
        {'id':'localint', 'type':'string', 'mode':''},
        {'id':'baseportindex', 'type':'int', 'mode':''},
        {'id':'baseport', 'type':'int', 'mode':''},
        {'id':'fdbport', 'type':'int', 'mode':''},
        {'id':'ipaddr', 'type':'string', 'mode':''},
        {'id':'macaddr', 'type':'string', 'mode':''},
        {'id':'sysname', 'type':'string', 'mode':''},
        )
    
    _relations = (
        ("NortelDevConDevice", ToOne(ToManyCont,
            "ZenPacks.community.NortelMon.NortelDevice", "NortelConDevice")),
        )


    factory_type_information = ( 
        { 
            'id'             : 'NortelConDevice',
            'meta_type'      : 'NortelConDevice',
            'description'    : """NortelConDevice info""",
            'product'        : 'NortelMon',
            'immediate_view' : 'viewNortelConDevice',
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
        self.sysname = getremotedevice(self, self.macaddr)
        self.localint = localinterface(self, self.device(), self.localint)
        self.id = getremotedeviceIP(self, self.macaddr)
        return self.id
        return self.sysname
        return self.localint

    titleOrId = name = viewName

    def device(self):
        return self.NortelDevConDevice()

    def getRRDTemplates(self):
        """
        Return the RRD Templates list
        """
        templates = []
        for tname in [self.__class__.__name__]:
            templ = self.getRRDTemplateByName(tname)
            if templ: templates.append(templ)
        return templates
    
InitializeClass(NortelConDevice)

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

__doc__="""NortelTopology object class"""
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

class NortelTopology(DeviceComponent, ManagedEntity):

    portal_type = meta_type = 'NortelTopology'
    

    unit = 0
    port = 0
    ipaddr = '' 
    macaddr = ''
    chassistype = ''
    localseg = ''
    curstate = ''
    sysname  = ''
    monitor = True

    _properties = (
        {'id':'unit', 'type':'int', 'mode':''},
        {'id':'port', 'type':'int', 'mode':''},
        {'id':'ipaddr', 'type':'string', 'mode':''},
        {'id':'macaddr', 'type':'string', 'mode':''},
        {'id':'chassistype', 'type':'string', 'mode':''},
        {'id':'localseg', 'type':'string', 'mode':''},
        {'id':'curstate', 'type':'string', 'mode':''},
        {'id':'sysname', 'type':'string', 'mode':''},
        )
    
    _relations = (
        ("NortelDevTopology", ToOne(ToManyCont,
            "ZenPacks.community.NortelMon.NortelDevice", "NortelTopology")),
        )


    factory_type_information = ( 
        { 
            'id'             : 'NortelTopology',
            'meta_type'      : 'NortelTopology',
            'description'    : """NortelTopology info""",
            'product'        : 'NortelMon',
            'immediate_view' : 'viewNortelTopology',
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
        self.sysname = self.remoteswitch()
        return self.id
        return self.sysname

    titleOrId = name = viewName

    def device(self):
        return self.NortelDevTopology()

    def getRRDTemplates(self):
        """
        Return the RRD Templates list
        """
        templates = []
        for tname in [self.__class__.__name__]:
            templ = self.getRRDTemplateByName(tname)
            if templ: templates.append(templ)
        return templates

    def remoteswitch(self):
        """try to get the remote device, using the management IP"""
        device = self.dmd.Devices.findDeviceByIdOrIp(self.ipaddr)
        if device:
            if device.urlLink() is None:
                return self.ipaddr
            else:
                return device.urlLink()
        else:
            return self.ipaddr
    
InitializeClass(NortelTopology)

# ==============================================================================
# NortelStatus object class
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

__doc__="""NortelStatus object class"""
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

class NortelStatus(DeviceComponent, ManagedEntity):

    portal_type = meta_type = 'NortelStatus'
    
    index = 0
    tmpvalue = 0
    cpuusage = ''
    totalmem = ''
    availablemem = ''
    usedmem = ''


    _properties = (
        {'id':'index', 'type':'int', 'mode':''},
        {'id':'tmpvalue', 'type':'int', 'mode':''},
        {'id':'cpuusage', 'type':'string', 'mode':''},
        {'id':'totalmem', 'type':'string', 'mode':''},
        {'id':'availablemem', 'type':'string', 'mode':''},
        {'id':'usedmem', 'type':'string', 'mode':''},
        )
    
    _relations = (
        ("NortelDevStatus", ToOne(ToManyCont,
            "ZenPacks.community.NortelMon.NortelDevice", "NortelStatus")),
        )


    factory_type_information = ( 
        { 
            'id'             : 'NortelStatus',
            'meta_type'      : 'NortelStatus',
            'description'    : """NortelStatus info""",
            'product'        : 'NortelMon',
            'immediate_view' : 'viewNortelStatus',
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
        self.tmpvalue = self.temperature()
        return self.id
        return self.tmpvalue

    titleOrId = name = viewName


    def device(self):
        return self.NortelDevStatus()
    
    def temperature(self):
        if self.tmpvalue != 0:
            self.tmpvalue = self.tmpvalue / 2
            return self.tmpvalue
        else:
            return self.tmpvalue

    def getRRDTemplates(self):
        """
        Return the RRD Templates list
        """
        templates = []
        for tname in [self.__class__.__name__]:
            templ = self.getRRDTemplateByName(tname)
            if templ: templates.append(templ)
        return templates
    
InitializeClass(NortelStatus)

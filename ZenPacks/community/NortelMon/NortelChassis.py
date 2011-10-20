# ==============================================================================
# NortelChassis object class
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

__doc__="""NortelChassis object class"""
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

class NortelChassis(DeviceComponent, ManagedEntity):

    portal_type = meta_type = 'NortelChassis'
    
    unitindex = 0
    unitnumber = ''
    totalport = 0
    chasstype = '' 
    desc = ''
    sernum = ''
    admstatus = ''
    operstatus  = ''

    _properties = (
        {'id':'unitindex', 'type':'int', 'mode':''},
        {'id':'unitnumber', 'type':'string', 'mode':''},
        {'id':'totalport', 'type':'int', 'mode':''},
        {'id':'chasstype', 'type':'string', 'mode':''},
        {'id':'desc', 'type':'string', 'mode':''},
        {'id':'sernum', 'type':'string', 'mode':''},
        {'id':'admstatus', 'type':'string', 'mode':''},
        {'id':'operstatus', 'type':'string', 'mode':''},
        )
    
    _relations = (
        ("NortelDevChassis", ToOne(ToManyCont,
            "ZenPacks.community.NortelMon.NortelDevice", "NortelChassis")),
        )


    factory_type_information = ( 
        { 
            'id'             : 'NortelChassis',
            'meta_type'      : 'NortelChassis',
            'description'    : """NortelChassis info""",
            'product'        : 'NortelMon',
            'immediate_view' : 'viewNortelChassis',
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
        return self.NortelDevChassis()

    def getRRDTemplates(self):
        """
        Return the RRD Templates list
        """
        templates = []
        for tname in [self.__class__.__name__]:
            templ = self.getRRDTemplateByName(tname)
            if templ: templates.append(templ)
        return templates
        
InitializeClass(NortelChassis)

# ==============================================================================
# PassportCardTable object class
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

__doc__="""PassportCardTable object class"""
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

class PassportCardTable(DeviceComponent, ManagedEntity):

    portal_type = meta_type = 'PassportCardTable'
    
    cardindex = 0
    cardtype = ''
    description = ''
    serialnumber = ''
    hwversion = ''
    partnumber = '' 
    opstatus = ''
    admstatus = ''
    

    _properties = (
        {'id':'cardindex', 'type':'int', 'mode':''},
        {'id':'cardtype', 'type':'string', 'mode':''},
        {'id':'description', 'type':'string', 'mode':''},
        {'id':'serialnumber', 'type':'string', 'mode':''},
        {'id':'hwversion', 'type':'string', 'mode':''},
        {'id':'partnumber', 'type':'string', 'mode':''},
        {'id':'opstatus', 'type':'string', 'mode':''},
        {'id':'admstatus', 'type':'string', 'mode':''},
        )
    
    _relations = (
        ("PassportDevCardTable", ToOne(ToManyCont,
            "ZenPacks.community.NortelMon.PassportDevice", "PassportCardTable")),
        )


    factory_type_information = ( 
        { 
            'id'             : 'PassportCardTable',
            'meta_type'      : 'PassportCardTable',
            'description'    : """PassportCardTable info""",
            'product'        : 'NortelMon',
            'immediate_view' : 'viewPassportCardTable',
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
        return self.PassportDevCardTable()

    def getRRDTemplates(self):
        """
        Return the RRD Templates list
        """
        templates = []
        for tname in [self.__class__.__name__]:
            templ = self.getRRDTemplateByName(tname)
            if templ: templates.append(templ)
        return templates
    
InitializeClass(PassportCardTable)

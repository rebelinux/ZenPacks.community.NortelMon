# ==============================================================================
# PassportConPort object class
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

__doc__="""PassportConPort object class"""
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

class PassportConPort(DeviceComponent, ManagedEntity):

    portal_type = meta_type = 'PassportConPort'
    

    cpuethernetportindex = 0
    cpuethernetportdescr = ''
    ethernetportaddr = ''
    cpuethernetportmask = ''
    cpuethernetportnetwork = ''
    cpuethernetportgateway = ''
    portmgmtmacaddr = ''

    monitor = True

    _properties = (
        {'id':'cpuethernetportindex', 'type':'int', 'mode':''},
        {'id':'cpuethernetportdescr', 'type':'string', 'mode':''},
        {'id':'ethernetportaddr', 'type':'string', 'mode':''},
        {'id':'cpuethernetportmask', 'type':'string', 'mode':''},
        {'id':'cpuethernetportnetwork', 'type':'string', 'mode':''},
        {'id':'cpuethernetportgateway', 'type':'string', 'mode':''},
        {'id':'portmgmtmacaddr', 'type':'string', 'mode':''},
        )
    
    _relations = (
        ("PassportDevConPort", ToOne(ToManyCont,
            "ZenPacks.community.NortelMon.PassportDevice", "PassportConPort")),
        )


    factory_type_information = ( 
        { 
            'id'             : 'PassportConPort',
            'meta_type'      : 'PassportConPort',
            'description'    : """PassportConPort info""",
            'product'        : 'NortelMon',
            'immediate_view' : 'viewPassportConPort',
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
        return self.PassportDevConPort()
    
    def manage_deleteComponent(self, REQUEST=None):
        """Delete PassportConPort component takes from Jane Curry"""
        url = None
        if REQUEST is not None:
            url = self.device().PassportConPort.absolute_url()
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
    
InitializeClass(PassportConPort)

# ==============================================================================
# PassportTopology object class
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

__doc__="""PassportTopology object class"""
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

class PassportTopology(DeviceComponent, ManagedEntity):

    portal_type = meta_type = 'PassportTopology'
    

    localint = ''
    slot = 0
    port = 0
    ipaddr = '' 
    macaddr = ''
    chassistype = ''
    connection = ''
    pingstatus = ''
    sysname  = ''
    monitor = True

    _properties = (
        {'id':'localint', 'type':'string', 'mode':''},
        {'id':'slot', 'type':'int', 'mode':''},
        {'id':'port', 'type':'int', 'mode':''},
        {'id':'ipaddr', 'type':'string', 'mode':''},
        {'id':'macaddr', 'type':'string', 'mode':''},
        {'id':'chassistype', 'type':'string', 'mode':''},
        {'id':'pingstatus', 'type':'string', 'mode':''},
        {'id':'connection', 'type':'string', 'mode':''},
        {'id':'sysname', 'type':'string', 'mode':''},
        )
    
    _relations = (
        ("PassportDevTopology", ToOne(ToManyCont,
            "ZenPacks.community.NortelMon.PassportDevice", "PassportTopology")),
        )


    factory_type_information = ( 
        { 
            'id'             : 'PassportTopology',
            'meta_type'      : 'PassportTopology',
            'description'    : """PassportTopology info""",
            'product'        : 'NortelMon',
            'immediate_view' : 'viewPassportTopology',
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
    
    def remoteswitch(self):
        """try to get the remote device, using the device ip"""
        try:
            remotedev = self.dmd.Devices.findDeviceByIdOrIp(self.ipaddr)
            if remotedev.urlLink():
                self.sysname = remotedev.urlLink()
                return self.sysname
            else:
                self.sysname = self.ipaddr
                return self.sysname
        except:
            return 'Device Not In Zenoss'

    def localinterface(self):
        try:
            return utils.findinterface(self, self.device(), self.localint)
        except AttributeError:
            return self.localint
    
    def status(self):
        try:
            dev = self.dmd.Devices.findDeviceByIdOrIp(self.ipaddr)
            if dev:
                if dev.getPingStatus() > 0:
                    self.pingstatus = 'Down'
                else:
                    self.pingstatus = 'Up'
                return self.pingstatus
        except AttributeError:
            self.pingstatus = 'Unknown'
            return self.pingstatus

    def device(self):
        return self.PassportDevTopology()
    
    def manage_deleteComponent(self, REQUEST=None):
        """Delete PassportTopology component takes from Jane Curry"""
        url = None
        if REQUEST is not None:
            url = self.device().PassportTopology.absolute_url()
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
    
InitializeClass(PassportTopology)

# =======================================================================
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
# =========================================================================

__doc__ = """NortelTopology object class"""
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
from ZenPacks.community.NortelMon.utils import fixip, devicename, findinterface

import logging
log = logging.getLogger('NortelTopology')

class NortelTopology(DeviceComponent, ManagedEntity):

    portal_type = meta_type = 'NortelTopology'

    localint = ''
    unit = 0
    port = 0
    ipaddr = ''
    macaddr = ''
    chassistype = ''
    connection = ''
    pingstatus = ''
    sysname = ''
    monitor = True

    _properties = (
        {'id':'localint', 'type':'string', 'mode':''},
        {'id':'unit', 'type':'int', 'mode':''},
        {'id':'port', 'type':'int', 'mode':''},
        {'id':'ipaddr', 'type':'string', 'mode':''},
        {'id':'macaddr', 'type':'string', 'mode':''},
        {'id':'chassistype', 'type':'string', 'mode':''},
        {'id':'connection', 'type':'string', 'mode':''},
        {'id':'pingstatus', 'type':'string', 'mode':''},
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
        return self.id

    titleOrId = name = viewName

    def remoteswitch(self):
        """try to get the remote device, using the device ip"""
        try:
            topologyid = fixip(self, self.ipaddr)
            localdev = self.device()
            remotedev = self.dmd.Devices.findDeviceByIdOrIp(topologyid)
            if remotedev.getDeviceClassPath() == '/Network/Switch/Nortel/Passport':
                topolink = remotedev.PassportTopology.findObjectsById(localdev.getManageIp())
            else:
                topolink = remotedev.NortelTopology.findObjectsById(localdev.getManageIp())
            for link in topolink:
                if link.urlLink():
                    oldtext = '>%s<' % link.id
                    newtext = '>%s<' % devicename(self, topologyid)
                    oldlink = link.urlLink()
                    newlink = oldlink.replace(oldtext, newtext)
                    self.sysname = newlink
                    return self.sysname
                else:
                    self.sysname = topologyid
                    return self.sysname
        except:
            return 'Device Not In Zenoss'

    def localinterface(self):
        try:
            return findinterface(self, self.device(), self.localint)
        except:
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
        except:
            return self.pingstatus
    def zlink(self):
        try:
            if self.ipaddr:
                telnet = '<a href=telnet://%s target="_">Telnet:</a>' % self.ipaddr
                web = '<a href=http://%s target="_">Web Manage:</a>' % self.ipaddr
                jdm = '<a href=jdm://%s target="_">Nortel Manager:</a>' % self.ipaddr
                self.connection = telnet + '  ' + web + '  ' + jdm
                return self.connection
        except:
            return self.connection

    def device(self):
        return self.NortelDevTopology()

    def manage_deleteComponent(self, REQUEST=None):
        """Delete NortelTopology component takes from Jane Curry"""
        url = None
        if REQUEST is not None:
            url = self.device().NortelTopology.absolute_url()
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
    
InitializeClass(NortelTopology)

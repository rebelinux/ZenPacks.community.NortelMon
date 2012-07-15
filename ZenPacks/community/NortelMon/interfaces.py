# ==============================================================================
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

__doc__="""Representation of an Avaya Nortel Monitoring Component"""
__author__ = "Jonathan Colon"
__copyright__ = "(C) Copyright Jonathan Colon. 2011. All Rights Reserved."
__license__ = "GPL"
__version__ = "1.0.0"

from Products.Zuul.interfaces import IComponentInfo
from Products.Zuul.form import schema
from Products.Zuul.utils import ZuulMessageFactory as _t


class IPassportPowerInfo(IComponentInfo):
    powersupplystatus = schema.Text(title=u"Passport Monitoring Status (value)", readonly=True, group='Details')
    powersupplystatusText = schema.Text(title=u"Passport Monitoring Status", readonly=True, group='Details')

class IPassportFanInfo(IComponentInfo):
    fanstatus = schema.Text(title=u"Fan Status (value)", readonly=True, group='Details')
    fanstatusText = schema.Text(title=u"Fan Status", readonly=True, group='Details')
    fantemp = schema.Text(title=u"Fan Temperature", readonly=True, group='Details')

class IPassportConPortInfo(IComponentInfo):
    cpuethernetportdescr = schema.Text(title=u"Port Description", readonly=True, group='Details')
    ethernetportaddr = schema.Text(title=u"IP Address", readonly=True, group='Details')
    cpuethernetportmask = schema.Text(title=u"NetMask", readonly=True, group='Details')    
    cpuethernetportnetwork = schema.Text(title=u"Network", readonly=True, group='Details')
    portmgmtmacaddr = schema.Text(title=u"Mgmt Mac Address", readonly=True, group='Details')
    cpuethernetportgateway = schema.Text(title=u"Gateway", readonly=True, group='Details')

class IPassportTopologyInfo(IComponentInfo):
    sysname = schema.Text(title=u"System Name", readonly=True, group='Details')
    ipaddr = schema.Text(title=u"Ip Address", readonly=True, group='Details')
    macaddr = schema.Text(title=u"Mac Address", readonly=True, group='Details')
    localint = schema.Text(title=u"Local Interface", readonly=True, group='Details')
    chassistype = schema.Text(title=u"Chassis Type", readonly=True, group='Details')
    connection = schema.Text(title=u"Connection", readonly=True, group='Details')
    pingstatus = schema.Text(title=u"Device Status", readonly=True, group='Details')

class INortelTopologyInfo(IComponentInfo):
    sysname = schema.Text(title=u"System Name", readonly=True, group='Details')
    ipaddr = schema.Text(title=u"Ip Address", readonly=True, group='Details')
    macaddr = schema.Text(title=u"Mac Address", readonly=True, group='Details')
    localint = schema.Text(title=u"Local Interface", readonly=True, group='Details')
    chassistype = schema.Text(title=u"Chassis Type", readonly=True, group='Details')
    connection = schema.Text(title=u"Connection", readonly=True, group='Details')
    pingstatus = schema.Text(title=u"Device Status", readonly=True, group='Details')
    
class INortelChassisInfo(IComponentInfo):
    unitnumber = schema.Text(title=u"Stack Members", readonly=True, group='Details')
    totalport = schema.Text(title=u"Total Ports", readonly=True, group='Details')
    chasstype = schema.Text(title=u"Chassis Type", readonly=True, group='Details')
    desc = schema.Text(title=u"Description", readonly=True, group='Details')
    sernum = schema.Text(title=u"Serial Number", readonly=True, group='Details')
    operstatus = schema.Text(title=u"Oper Status", readonly=True, group='Details')

class IPassportVlanTableInfo(IComponentInfo):
    vlanid = schema.Text(title=u"Vlan Id", readonly=True, group='Details')
    vlanname = schema.Text(title=u"Name", readonly=True, group='Details')
    vlanstgid = schema.Text(title=u"STG Id", readonly=True, group='Details')
    vlantype = schema.Text(title=u"Type", readonly=True, group='Details')
    vlanmac = schema.Text(title=u"Mac Address", readonly=True, group='Details')

class IPassportVlanPortInfo(IComponentInfo):
    intname = schema.Text(title=u"Port Id", readonly=True, group='Details')
    description = schema.Text(title=u"Description", readonly=True, group='Details')
    vlanportids = schema.Text(title=u"Vlan Members", readonly=True, group='Details')
    vlanporttype = schema.Text(title=u"Port Type", readonly=True, group='Details')
    vlanpvid = schema.Text(title=u"PvId", readonly=True, group='Details')
    vlantag = schema.Text(title=u"Vlan Tag", readonly=True, group='Details')
    
class IPassportCardTableInfo(IComponentInfo):
    cardtype = schema.Text(title=u"Type", readonly=True, group='Details')
    description = schema.Text(title=u"Description", readonly=True, group='Details')
    serialnumber = schema.Text(title=u"Serial Number", readonly=True, group='Details')
    hwversion = schema.Text(title=u"HW Version", readonly=True, group='Details')
    partnumber = schema.Text(title=u"Part Number", readonly=True, group='Details')
    opstatus = schema.Text(title=u"Oper Status", readonly=True, group='Details')
    admstatus = schema.Text(title=u"Admin Status", readonly=True, group='Details')
    
class INortelVlanTableInfo(IComponentInfo):
    vlanid = schema.Text(title=u"Vlan Id", readonly=True, group='Details')
    vlanname = schema.Text(title=u"Name", readonly=True, group='Details')
    vlanstgid = schema.Text(title=u"STG Id", readonly=True, group='Details')
    vlantype = schema.Text(title=u"Type", readonly=True, group='Details')
    vlanmac = schema.Text(title=u"Mac Address", readonly=True, group='Details')

class INortelVlanPortInfo(IComponentInfo):
    intname = schema.Text(title=u"Port Id", readonly=True, group='Details')
    description = schema.Text(title=u"Description", readonly=True, group='Details')
    vlanportids = schema.Text(title=u"Vlan Members", readonly=True, group='Details')
    vlanporttype = schema.Text(title=u"Port Type", readonly=True, group='Details')
    vlanpvid = schema.Text(title=u"PvId", readonly=True, group='Details')
    vlantag = schema.Text(title=u"Vlan Tag", readonly=True, group='Details')

class INortelFanInfo(IComponentInfo):
    fanstatus = schema.Text(title=u"Fan Status", readonly=True, group='Details')
    fanindex = schema.Text(title=u"Fan", readonly=True, group='Details')
    fandesc = schema.Text(title=u"Description", readonly=True, group='Details')
    
class INortelPowerInfo(IComponentInfo):
    powerstatus = schema.Text(title=u"Power Supply Status", readonly=True, group='Details')
    powerindex = schema.Text(title=u"Power Supply", readonly=True, group='Details')
    powerdesc = schema.Text(title=u"Description", readonly=True, group='Details')
    
class INortelStatusInfo(IComponentInfo):
    cpuusage = schema.Text(title=u"Cpu% Usage", readonly=True, group='Details')
    totalmem = schema.Text(title=u"Total Mem", readonly=True, group='Details')
    availablemem = schema.Text(title=u"Available Mem", readonly=True, group='Details')
    usedmem = schema.Text(title=u"Used Mem", readonly=True, group='Details')
    tmpvalue = schema.Text(title=u"Temperature", readonly=True, group='Details')

class INortelMltStatusInfo(IComponentInfo):
    nmltname = schema.Text(title=u"Name", readonly=True, group='Details')
    nmltvlans = schema.Text(title=u"Vlans", readonly=True, group='Details')
    nmltenable = schema.Text(title=u"Enabled?", readonly=True, group='Details')
    nmltstatus = schema.Text(title=u"Status", readonly=True, group='Details')

class IPassportMltStatusInfo(IComponentInfo):
    mltname = schema.Text(title=u"Name", readonly=True, group='Details')
    mlttype = schema.Text(title=u"Configured Type", readonly=True, group='Details')
    mltruntype = schema.Text(title=u"Running Type", readonly=True, group='Details')
    mltvlans = schema.Text(title=u"Vlans", readonly=True, group='Details')
    mltenable = schema.Text(title=u"Enabled?", readonly=True, group='Details')
    mltstatus = schema.Text(title=u"Status", readonly=True, group='Details')
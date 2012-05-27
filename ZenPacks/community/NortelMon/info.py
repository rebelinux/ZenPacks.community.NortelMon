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

from zope.interface import implements
from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.component import ComponentInfo
from Products.Zuul.decorators import info
from ZenPacks.community.NortelMon import interfaces
from Products.Zuul.interfaces import IInfo


class PassportPowerInfo(ComponentInfo):
    implements(interfaces.IPassportPowerInfo)

    powerindex = ProxyProperty("powerindex")
    powersupplystatus = ProxyProperty("powersupplystatus")
    powersupplystatusText = ProxyProperty("powersupplystatusText")

class PassportFanInfo(ComponentInfo):
    implements(interfaces.IPassportFanInfo)
    
    fanindex = ProxyProperty("fanindex")
    fanstatus = ProxyProperty("fanstatus")
    fanstatusText = ProxyProperty("fanstatusText")
    fantemp = ProxyProperty("fantemp")

class PassportConPortInfo(ComponentInfo):
    implements(interfaces.IPassportConPortInfo)

    cpuethernetportindex = ProxyProperty("cpuethernetportindex")
    cpuethernetportdescr = ProxyProperty("cpuethernetportdescr")
    ethernetportaddr = ProxyProperty("ethernetportaddr")
    cpuethernetportmask = ProxyProperty("cpuethernetportmask")
    cpuethernetportnetwork = ProxyProperty("cpuethernetportnetwork")
    cpuethernetportgateway = ProxyProperty("cpuethernetportgateway")
    portmgmtmacaddr = ProxyProperty("portmgmtmacaddr")

class PassportTopologyInfo(ComponentInfo):
    implements(interfaces.IPassportTopologyInfo)

    localint = ProxyProperty("localint")
    slot = ProxyProperty("slot")
    port = ProxyProperty("port")
    ipaddr = ProxyProperty("ipaddr")
    macaddr = ProxyProperty("macaddr")
    chassistype = ProxyProperty("chassistype")
    localseg = ProxyProperty("localseg")
    curstate = ProxyProperty("curstate")
    sysname = ProxyProperty("sysname")

class NortelTopologyInfo(ComponentInfo):
    implements(interfaces.INortelTopologyInfo)

    localint = ProxyProperty("localint")
    unit = ProxyProperty("unit")
    port = ProxyProperty("port")
    ipaddr = ProxyProperty("ipaddr")
    macaddr = ProxyProperty("macaddr")
    chassistype = ProxyProperty("chassistype")
    localseg = ProxyProperty("localseg")
    curstate = ProxyProperty("curstate")
    sysname = ProxyProperty("sysname")

class NortelChassisInfo(ComponentInfo):
    implements(interfaces.INortelChassisInfo)

    unitindex = ProxyProperty("unitindex")
    unitnumber = ProxyProperty("unitnumber")
    totalport = ProxyProperty("totalport")
    chasstype = ProxyProperty("chasstype")
    desc = ProxyProperty("desc")
    sernum = ProxyProperty("sernum")
    operstatus = ProxyProperty("operstatus")

class PassportVlanTableInfo(ComponentInfo):
    implements(interfaces.IPassportVlanTableInfo)

    vlanid = ProxyProperty("vlanid")
    vlanname = ProxyProperty("vlanname")
    vlanstgid = ProxyProperty("vlanstgid")
    vlantype = ProxyProperty("vlantype")
    vlanmac = ProxyProperty("vlanmac")

class PassportVlanPortInfo(ComponentInfo):
    implements(interfaces.IPassportVlanPortInfo)

    intname = ProxyProperty("intname")
    description = ProxyProperty("description")
    vlanportindex = ProxyProperty("vlanportindex")
    vlanportids = ProxyProperty("vlanportids")
    vlanporttype = ProxyProperty("vlanporttype")
    vlanpvid = ProxyProperty("vlanpvid")
    vlantag = ProxyProperty("vlantag")
    
class PassportCardTableInfo(ComponentInfo):
    implements(interfaces.IPassportCardTableInfo)
    
    cardindex = ProxyProperty("cardindex")
    cardtype = ProxyProperty("cardtype")
    description = ProxyProperty("description")
    serialnumber = ProxyProperty("serialnumber")
    hwversion = ProxyProperty("hwversion")
    partnumber = ProxyProperty("partnumber")
    opstatus = ProxyProperty("opstatus")
    admstatus = ProxyProperty("admstatus")
    
class NortelVlanTableInfo(ComponentInfo):
    implements(interfaces.INortelVlanTableInfo)

    vlanid = ProxyProperty("vlanid")
    vlanname = ProxyProperty("vlanname")
    vlanstgid = ProxyProperty("vlanstgid")
    vlantype = ProxyProperty("vlantype")
    vlanmac = ProxyProperty("vlanmac")

class NortelVlanPortInfo(ComponentInfo):
    implements(interfaces.INortelVlanPortInfo)

    intname = ProxyProperty("intname")
    description = ProxyProperty("description")
    vlanportids = ProxyProperty("vlanportids")
    vlanporttype = ProxyProperty("vlanporttype")
    vlanpvid = ProxyProperty("vlanpvid")
    vlantag = ProxyProperty("vlantag")
    
class NortelFanInfo(ComponentInfo):
    implements(interfaces.INortelFanInfo)
    
    fanindex = ProxyProperty("fanindex")
    fanstatus = ProxyProperty("fanstatus")
    fandesc = ProxyProperty("fandesc")
    
class NortelPowerInfo(ComponentInfo):
    implements(interfaces.INortelPowerInfo)
    
    powerindex = ProxyProperty("powerindex")
    powerstatus = ProxyProperty("powerstatus")
    powerdesc = ProxyProperty("powerdesc")
    
class NortelStatusInfo(ComponentInfo):
    implements(interfaces.INortelStatusInfo)
    
    index = ProxyProperty("index")
    tmpvalue = ProxyProperty("tmpvalue")
    cpuusage = ProxyProperty("cpuusage")
    totalmem = ProxyProperty("totalmem")
    availablemem = ProxyProperty("availablemem")
    usedmem = ProxyProperty("usedmem")
    
class NortelMltStatusInfo(ComponentInfo):
    implements(interfaces.INortelMltStatusInfo)
    
    nmltid = ProxyProperty("nmltid")
    nmltname = ProxyProperty("nmltname")
    nmltenable = ProxyProperty("nmltenable")
    nmltvlans = ProxyProperty("nmltvlans")
    nmltstatus = ProxyProperty("nmltstatus")
    
class PassportMltStatusInfo(ComponentInfo):
    implements(interfaces.IPassportMltStatusInfo)
    
    mltid = ProxyProperty("mltid")
    mltname = ProxyProperty("mltname")
    mltenable = ProxyProperty("mltenable")
    mltvlans = ProxyProperty("mltvlans")
    mltstatus = ProxyProperty("mltstatus")
    mlttype = ProxyProperty("mlttype")
    mltruntype = ProxyProperty("mltruntype")
    
class NortelConDeviceInfo(ComponentInfo):
    implements(interfaces.INortelConDeviceInfo)

    localint = ProxyProperty("localint")
    ipaddr = ProxyProperty("ipaddr")
    macaddr = ProxyProperty("macaddr")
    sysname = ProxyProperty("sysname")
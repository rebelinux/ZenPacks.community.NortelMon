# ==============================================================================
# PassportCardTableMap modeler plugin
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

__doc__="""PassportCardTableMap maps rc2kCardTable monitoring entries"""
__author__ = "Jonathan Colon"
__copyright__ = "(C) Copyright Jonathan Colon. 2011. All Rights Reserved."
__license__ = "GPL"
__version__ = "1.0.0"

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap, GetTableMap

class PassportCardTableMap(SnmpPlugin):
    """Map Nortel Passport Card table to model."""
    maptype = "PassportCardTableMap"
    modname = "ZenPacks.community.NortelMon.PassportCardTable"
    relname = "PassportCardTable"
    

    snmpGetTableMaps = (
        GetTableMap('card',
		'.1.3.6.1.4.1.2272.1.100.6.1',
                    {
                        '.1': 'cardindex',
                        '.2': 'cardtype',
                        '.3': 'description',
                        '.4': 'admstatus',
                        '.5': 'opstatus',
                        '.6': 'serialnumber',
                        '.7': 'hwversion',
                        '.8': 'partnumber',
                    }
                    ),
	)
    def process(self, device, results, log):
        """collect snmp information from this device"""
        log.info('processing %s for device %s', self.name(), device.id)
        getdata, tabledata = results
        cards = tabledata.get("card")
        
        # Debug: print data retrieved from device.
        log.debug( "Get data = %s", getdata )
        log.debug( "Table data = %s", tabledata )

        # If no data retrieved return nothing.        
        if not cards:
            log.warn( 'No data collected from %s for the %s plugin', device.id, self.name() )
            return
        rm = self.relMap()
        for oid, data in cards.iteritems():
            try:
                om = self.objectMap(data)
                om.id = self.prepId("Slot_%s" % om.cardindex)
                om.snmpindex = om.cardindex
                if om.admstatus not in self.status.keys():
                    om.admstatus = 4
                om.admstatus = self.status[om.admstatus]
                if om.opstatus not in self.status.keys():
                    om.opstatus = 4
                om.opstatus = self.status[om.opstatus]
                if om.cardtype not in self.type.keys():
                    om.cardtype = 1
                om.cardtype = self.type[om.cardtype]
            except AttributeError:
                continue
            rm.append(om)
        return rm

    status = { 1: 'UP',
                       2: 'Down',
                       3: 'Testing',
                       4: 'Unknown',
                       5: 'Dormant'
                     }
    type = { 1: 'other',
                       537788672: 'CPU',
                       539033904: '48x100BaseTX',
                       539033880: '24x100BaseT',
                       539033888: '32x100BaseTX',
                       539099400: '8x1000BaseT',
                       539099408: '16x1000BaseT',
                       540082456: '24x100BaseFX',
                       540147976: '8x1000BaseSXBB',
                       540147984: '16x1000BaseSXBB',
                       540156168: '8x1000BaseLXBB',
                       540164360: '8x1000BaseXDBB',
                       540168452: '4x1000BaseOPM',
                       40168456: '8x1000BaseOPM',
                       540168456: '8x1000BaseIC',
                       540168464: '16x1000BaseIC',
                       540180744: '8x1000BaseSXRBB',
                       540188936: '8x1000BaseLXRBB',
                       541327624: '8xOC3',
                       541393154: '2xOC12',
                       541401350: '6xPOS',
                       542441732: '4xATM',
                       542441736: '8xATM',
                       545128704: 'RMON',
                       573767937: '1x10GBaseLW',
                       573784321: '1x10GBaseLR',
                       572588320: '32x100BaseTXM',
                       572588336: '48x100BaseTXM',
                       572653832: '8x1000BaseTM',
                       573702408: '8x1000BaseSXBBM',
                       573722888: '8x1000BaseICM',
                       574955782: '6xPOSM',
                       575996168: '8xATMM',
                       607338764: 'PR12X10GBaseXLRS',
                       807469360: 'Mg48x100BaseTX',
                       807473440: 'Mg32x100BaseTX',
                       808522000: 'Mg16x100BaseFX',
                       808583432: 'Mg8x1000BaseTX',
                       808603912: 'Mg8x1000BaseIC',
                       817955120: 'Mg48x100BaseTC',
                       1073807408: 'Cobra48x100BaseT',
                       1073872920: 'Cobra24x1000BaseG',
                       1073872908: 'Cobra12x1000BaseG',
                       1926365441: '61AlteonSAM',
                       1926369537: '62AlteonSAM',
                       1342316808: 'PP8300-CPU8x1000BaseSFP',
                       1344405784: 'PP8300-24x1000BaseTX',
                       1344340272: 'PP8300-48x100BaseTX',
                       1344344368: 'PP8300-48x100BaseTXPOE',
                       607277342: 'PR30X1000BaseSXBB',
                       607338755: 'PR3X10GBaseGbic',
                       607346947: 'PR3X10GBaseXZW',
                       607277360: 'PR48x1000BaseGBRS',
                     }

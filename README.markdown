# ZenPacks.community.NortelMon

## About
This project is [Zenoss][] extension (ZenPack) that makes it possible to
model and monitor Nortel Passport, Baystack, BPS2000 and Ers Serie Switches
## Requirements

### Zenoss
You must first have, or install, Zenoss 3.0 or later. This ZenPack was
tested against Zenoss 3.0 and Zenoss 3.2.1. You can download
the free Core version of Zenoss from
<http://community.zenoss.org/community/download>.

## Installation

### Normal Installation (packaged egg)
Download the [NortelMon ZenPack][]. Copy this file to your Zenoss
server and run the following commands as the zenoss user.

    zenpack --install EGG File
    zenoss restart

### Developer Installation (link mode)
If you wish to further develop and possibly contribute back to the HPEVAMon
ZenPack you should clone the [git repository][], then install the ZenPack in
developer mode using the following commands.

    git clone git://github.com/rebelinux/ZenPacks.community.NortelMon.git
    zenpack --link --install ZenPacks.community.NortelMon
    zenoss restart

## Usage

### You should now have Nortel device class.

/Device/Network/Switch/Nortel = Root Device Class

/Device/Network/Switch/Nortel/Baystack = This Class is for legacy Nortel Switches (Tested it with BPS2000 & Baystack).

/Device/Network/Switch/Nortel/ERS = This Class is for new Avaya Switches (Tested it with ERS2000, ERS4000 & ERS5000).

/Device/Network/Switch/NortelPassport	= This Class is for Nortel Passport Switches (Tested it with ERS-1624 & ERS-8000).


The following elements are discovered:

 * Manufacturer Info set by Modeler (All Model).
 * PowerSupply Component (Status) (ERS & Passport Model).
 * Fan Component (Status) )ERS & Passport-8000 Model).
 * CardTable Component (Status) (Passport Model).
 * Console Port (Status) (Passport Model).
 * Vlans Table (Status) (All Model).
 * Per Port Vlan Table (Status) (All Model).
 * CPU, Memory & Temperature Performance Graph (ERS & Passport Model).
 * Stack Member Status (Status) (ERS Model).
 * Correct Network Interface Name (All Model).
 * Correct Network Interface Description (Passport Model).
 * Correct Network Interface Duplex Value (All Model).
 * Topology Table (SONMP) (All Model).

[Zenoss]: <http://www.zenoss.com/>
[NortelMon ZenPack]: <http://community.zenoss.org/docs/DOC-3522>
[git repository]: <https://github.com/rebelinux/ZenPacks.community.NortelMon>


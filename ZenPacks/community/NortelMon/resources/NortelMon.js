(function(){

var ZC = Ext.ns('Zenoss.component');

function render_link(ob) {
    if (ob && ob.uid) {
        return Zenoss.render.link(ob.uid);
    } else {
        return ob;
    }
}

ZC.PassportPowerPanel = Ext.extend(ZC.ComponentGridPanel, {
    subComponentGridPanel: false,
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'PassportPower',
            fields: [
                {name: 'uid'},
                {name: 'severity'},
                {name: 'name'},
                {name: 'status'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitored'},
                {name: 'monitor'},
                {name: 'powersupplystatus'},
                {name: 'powersupplystatusText'},
                {name: 'locking'},
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                width: 60,
            },{
                id: 'powersupplystatus',
                dataIndex: 'powersupplystatus',
                header: _t('PowerSupply Status'),
                sortable: true,
                renderer: Zenoss.render.severity,
                width: 120
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
            },{
                id: 'powersupplystatusText',
                dataIndex: 'powersupplystatusText',
                header: _t('Status'),
                sortable: true,
            },{ 
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                width: 72,
                renderer: Zenoss.render.locking_icons,
            }]
        });
        ZC.PassportPowerPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('PassportPowerPanel', ZC.PassportPowerPanel);
ZC.registerName('PassportPower', _t('Power Supply'), _t('Power Supplies'));

ZC.PassportFanPanel = Ext.extend(ZC.ComponentGridPanel, {
    subComponentGridPanel: false,
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'PassportFan',
            fields: [
                {name: 'uid'},
                {name: 'severity'},
				{name: 'name'},
                {name: 'status'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitored'},
                {name: 'monitor'},
                {name: 'fanstatus'},
                {name: 'fanstatusText'},
                {name: 'fantemp'},
                {name: 'locking'},
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                width: 60,
            },{
                id: 'fanstatus',
                dataIndex: 'fanstatus',
                header: _t('Fan Status'),
                sortable: true,
                renderer: Zenoss.render.severity,
                width: 120,
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name')
            },{
                id: 'fantemp',
                dataIndex: 'fantemp',
                header: _t('Temperature'),
                sortable: true,
                width: 120,
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored')
            },{
                id: 'fanstatusText',
                dataIndex: 'fanstatusText',
                header: _t('Status'),
                sortable: true,
            },{ 
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                width: 72,
                renderer: Zenoss.render.locking_icons,
            }]
        });
        ZC.PassportFanPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('PassportFanPanel', ZC.PassportFanPanel);
ZC.registerName('PassportFan', _t('Fan'), _t('Fans'));

ZC.PassportConPortPanel = Ext.extend(ZC.ComponentGridPanel, {
    subComponentGridPanel: false,
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'PassportConPort',
            fields: [
                {name: 'uid'},
                {name: 'severity'},
				{name: 'name'},
                {name: 'status'},
                {name: 'hasMonitor'},
                {name: 'monitor'},
                {name: 'cpuethernetportdescr'},
                {name: 'ethernetportaddr'},
                {name: 'cpuethernetportmask'},
                {name: 'cpuethernetportnetwork'},
                {name: 'cpuethernetportgateway'},
                {name: 'portmgmtmacaddr'},
                {name: 'locking'},
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                width: 60,
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
            },{

                id: 'cpuethernetportdescr',
                dataIndex: 'cpuethernetportdescr',
                header: _t('Description'),
                sortable: true,
                width: 120,
            },{
                id: 'ethernetportaddr',
                dataIndex: 'ethernetportaddr',
                header: _t('IP Address'),
                sortable: true,
                width: 120,
            },{
                id: 'cpuethernetportmask',
                dataIndex: 'cpuethernetportmask',
                header: _t('NetMask'),
                sortable: true,
            },{
                id: 'cpuethernetportgateway',
                dataIndex: 'cpuethernetportgateway',
                header: _t('Gateway'),
                sortable: true,
            },{
                id: 'cpuethernetportnetwork',
                dataIndex: 'cpuethernetportnetwork',
                header: _t('Network Filter'),
                sortable: true,
            },{
                id: 'portmgmtmacaddr',
                dataIndex: 'portmgmtmacaddr',
                header: _t('Mgmt Mac Address'),
                sortable: true,
                width: 120,
            }]
        });
        ZC.PassportConPortPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('PassportConPortPanel', ZC.PassportConPortPanel);
ZC.registerName('PassportConPort', _t('Console Port'), _t('Console Ports'));

ZC.PassportTopologyPanel = Ext.extend(ZC.ComponentGridPanel, {
    subComponentGridPanel: false,
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'PassportTopology',
            autoExpandColumn: 'sysname',
            fields: [
                {name: 'uid'},
                {name: 'severity'},
				{name: 'name'},
                {name: 'status'},
                {name: 'hasMonitor'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitored'},
                {name: 'monitor'},
                {name: 'localint'},
                {name: 'macaddr'},
                {name: 'chassistype'},
                {name: 'pingstatus'},
                {name: 'sysname'},
                {name: 'connection'},
                {name: 'locking'},
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                width: 60,
            },{
                id: 'sysname',
                dataIndex: 'sysname',
                header: _t('Remote Device'),
                renderer: render_link,
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('IP Address'),
            },{
                id: 'macaddr',
                dataIndex: 'macaddr',
                header: _t('Mac Address'),
                sortable: true,
                width: 120,
            },{
                id: 'localint',
                dataIndex: 'localint',
                header: _t('Local Interface'),
                renderer: render_link,
            },{
                id: 'chassistype',
                dataIndex: 'chassistype',
                header: _t('Chassis Type'),
                sortable: true,
                width: 160,
            },{
                id: 'pingstatus',
                dataIndex: 'pingstatus',
                header: _t('Switch Status'),
                sortable: true,
                width: 120,
                renderer: function(pS) {
        			if (pS=='Up') {
        			  return Zenoss.render.pingStatus('up');
        			} if (pS=='Down') {
          			  return Zenoss.render.pingStatus('down');
        			} else {
        			  return 'Unknown';
        			}
                },
            },{ 
                id: 'connection',
                dataIndex: 'connection',
                header: _t('Manage'),
                sortable: true,
                width: 220,
            }]
        });
        ZC.PassportTopologyPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('PassportTopologyPanel', ZC.PassportTopologyPanel);
ZC.registerName('PassportTopology', _t('Topology Table'), _t('Topology Tables'));

ZC.PassportVlanTablePanel = Ext.extend(ZC.ComponentGridPanel, {
    subComponentGridPanel: false,
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'PassportVlanTable',
            autoExpandColumn: 'name',
            sortInfo: {
                field: 'vlanid',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'severity'},
				{name: 'name'},
                {name: 'status'},
                {name: 'hasMonitor'},
                {name: 'monitor'},
                {name: 'vlanid'},
                {name: 'vlanmac'},
                {name: 'vlantype'},
                {name: 'vlanname'},
                {name: 'vlanstgid'},		
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                width: 60,
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                width: 160,
			},{
                id: 'vlanid',
                dataIndex: 'vlanid',
                header: _t('Vlan ID'),
                sortable: true,
            },{
                id: 'vlantype',
                dataIndex: 'vlantype',
                header: _t('Type'),
                sortable: true,
                width: 120,
            },{
                id: 'vlanmac',
                dataIndex: 'vlanmac',
                header: _t('Mac Address'),
                sortable: true,
                width: 160,
			},{
                id: 'vlanstgid',
                dataIndex: 'vlanstgid',
                header: _t('STG Id'),
                sortable: true,
                width: 120,
            }]
        });
        ZC.PassportVlanTablePanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('PassportVlanTablePanel', ZC.PassportVlanTablePanel);
ZC.registerName('PassportVlanTable', _t('Vlan Table'), _t('Vlan Tables'));

ZC.PassportVlanPortPanel = Ext.extend(ZC.ComponentGridPanel, {
    subComponentGridPanel: false,
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'PassportVlanPort',
            autoExpandColumn: 'vlanportids',
            fields: [
                {name: 'uid'},
                {name: 'severity'},
                {name: 'name'},
                {name: 'intname'},
                {name: 'description'},
                {name: 'status'},
                {name: 'hasMonitor'},
                {name: 'monitor'},
                {name: 'vlanportids'},
                {name: 'vlanporttype'},
                {name: 'vlanpvid'},
                {name: 'vlantag'},		
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                width: 60,
            },{
                id: 'name',
                dataIndex: 'intname',
                header: _t('Name'),
                width: 160,
                renderer: render_link,
            },{
                id: 'description',
                dataIndex: 'description',
                header: _t('Description'),
                width: 180,
			},{
                id: 'vlanportids',
                dataIndex: 'vlanportids',
                header: _t('Vlan Members'),
                sortable: true,
			},{
                id: 'vlanporttype',
                dataIndex: 'vlanporttype',
                header: _t('Port Type'),
                sortable: true,
                width: 120,
            },{
                id: 'vlanpvid',
                dataIndex: 'vlanpvid',
                header: _t('PvId'),
                sortable: true,
                width: 160,
			},{
                id: 'vlantag',
                dataIndex: 'vlantag',
                header: _t('Vlan Tag'),
                sortable: true,
            }]
        });
        ZC.PassportVlanPortPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('PassportVlanPortPanel', ZC.PassportVlanPortPanel);
ZC.registerName('PassportVlanPort', _t('Ports Table'), _t('Ports Tables'));

ZC.PassportCardTablePanel = Ext.extend(ZC.ComponentGridPanel, {
    subComponentGridPanel: false,
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'PassportCardTable',
            autoExpandColumn: 'description',
            fields: [
                {name: 'uid'},
                {name: 'severity'},
				{name: 'name'},
                {name: 'status'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitored'},
                {name: 'monitor'},
                {name: 'cardtype'},
                {name: 'description'},
                {name: 'serialnumber'},
                {name: 'hwversion'},	
                {name: 'opstatus'},
                {name: 'admstatus'},
                {name: 'locking'},
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                width: 60,
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                width: 120,
			},{
                id: 'cardtype',
                dataIndex: 'cardtype',
                header: _t('Model'),
                sortable: true,
                width: 160,
			},{
                id: 'description',
                dataIndex: 'description',
                header: _t('Description'),
                sortable: true,
                width: 160,
            },{
                id: 'serialnumber',
                dataIndex: 'serialnumber',
                header: _t('Serial Number'),
                sortable: true,
                width: 160,
            },{
                id: 'admstatus',
                dataIndex: 'admstatus',
                header: _t('Admin Status'),
                sortable: true,
            },{
                id: 'opstatus',
                dataIndex: 'opstatus',
                header: _t('Oper Status'),
                sortable: true,
			},{
                id: 'hwversion',
                dataIndex: 'hwversion',
                header: _t('HW Version'),
                sortable: true,
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
            },{ 
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                width: 72,
                renderer: Zenoss.render.locking_icons,
            }]
        });
        ZC.PassportCardTablePanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('PassportCardTablePanel', ZC.PassportCardTablePanel);
ZC.registerName('PassportCardTable', _t('Card Table'), _t('Cards Tables'));

ZC.NortelTopologyPanel = Ext.extend(ZC.ComponentGridPanel, {
    subComponentGridPanel: false,
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'NortelTopology',
            autoExpandColumn: 'sysname',
            fields: [
                {name: 'uid'},
                {name: 'severity'},
                {name: 'name'},
                {name: 'status'},
                {name: 'hasMonitor'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitored'},
                {name: 'monitor'},
                {name: 'localint'},
                {name: 'macaddr'},
                {name: 'chassistype'},
                {name: 'pingstatus'},
                {name: 'sysname'},
                {name: 'connection'},
                {name: 'locking'},
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                width: 60,
            },{
                id: 'sysname',
                dataIndex: 'sysname',
                header: _t('Remote Device'),
                renderer: render_link,
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('IP Address'),
            },{
                id: 'macaddr',
                dataIndex: 'macaddr',
                header: _t('Mac Address'),
                sortable: true,
                width: 120,
            },{
                id: 'localint',
                dataIndex: 'localint',
                header: _t('Local Interface'),
                renderer: render_link,
            },{
                id: 'chassistype',
                dataIndex: 'chassistype',
                header: _t('Chassis Type'),
                sortable: true,
                width: 160,
            },{
                id: 'pingstatus',
                dataIndex: 'pingstatus',
                header: _t('Switch Status'),
                sortable: true,
                width: 120,
                renderer: function(pS) {
        			if (pS=='Up') {
        			  return Zenoss.render.pingStatus('up');
        			} if (pS=='Down') {
          			  return Zenoss.render.pingStatus('down');
        			} else {
        			  return 'Unknown';
        			}
                },
            },{ 
                id: 'connection',
                dataIndex: 'connection',
                header: _t('Manage'),
                sortable: true,
                width: 220,
            }]
        });
        ZC.NortelTopologyPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('NortelTopologyPanel', ZC.NortelTopologyPanel);
ZC.registerName('NortelTopology', _t('Topology Table'), _t('Topology Table'));

ZC.NortelChassisPanel = Ext.extend(ZC.ComponentGridPanel, {
    subComponentGridPanel: false,
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'NortelChassis',
            autoExpandColumn: 'desc',
            fields: [
                {name: 'uid'},
                {name: 'severity'},
                {name: 'name'},
                {name: 'status'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitored'},
                {name: 'monitor'},
                {name: 'totalport'},
                {name: 'desc'},
                {name: 'chasstype'},
                {name: 'sernum'},
                {name: 'operstatus'},
                {name: 'locking'},
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                width: 60,
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Stack Members'),
                width: 120,
            },{
                id: 'chasstype',
                dataIndex: 'chasstype',
                header: _t('Chassis Type'),
                sortable: true,
                width: 120,
            },{
                id: 'desc',
                dataIndex: 'desc',
                header: _t('Description'),
                sortable: true,
            },{
                id: 'sernum',
                dataIndex: 'sernum',
                header: _t('Serial Number'),
                sortable: true,
                width: 120,            
            },{
                id: 'operstatus',
                dataIndex: 'operstatus',
                header: _t('Oper Status'),
                sortable: true,
            },{
                id: 'totalport',
                dataIndex: 'totalport',
                header: _t('Total Ports'),
                sortable: true,
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
            },{ 
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                width: 72,
                renderer: Zenoss.render.locking_icons,
            }]
        });
        ZC.NortelChassisPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('NortelChassisPanel', ZC.NortelChassisPanel);
ZC.registerName('NortelChassis', _t('Stack Member'), _t('Stack Members'));

ZC.NortelVlanTablePanel = Ext.extend(ZC.ComponentGridPanel, {
    subComponentGridPanel: false,
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'NortelVlanTable',
            autoExpandColumn: 'name',
            sortInfo: {
                field: 'vlanid',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'severity'},
				{name: 'name'},
                {name: 'status'},
                {name: 'hasMonitor'},
                {name: 'monitor'},
                {name: 'vlanid'},
                {name: 'vlanmac'},
                {name: 'vlantype'},
                {name: 'vlanname'},
                {name: 'vlanstgid'},	
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                width: 60,
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                width: 160,
			},{
                id: 'vlanid',
                dataIndex: 'vlanid',
                header: _t('Vlan ID'),
                sortable: true,
            },{
                id: 'vlantype',
                dataIndex: 'vlantype',
                header: _t('Type'),
                sortable: true,
                width: 120,
            },{
                id: 'vlanmac',
                dataIndex: 'vlanmac',
                header: _t('Mac Address'),
                sortable: true,
                width: 160,
			},{
                id: 'vlanstgid',
                dataIndex: 'vlanstgid',
                header: _t('STG Id'),
                sortable: true,
                width: 120,
            }]
        });
        ZC.NortelVlanTablePanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('NortelVlanTablePanel', ZC.NortelVlanTablePanel);
ZC.registerName('NortelVlanTable', _t('Vlan Table'), _t('Vlan Tables'));

ZC.NortelVlanPortPanel = Ext.extend(ZC.ComponentGridPanel, {
    subComponentGridPanel: false,
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'NortelVlanPort',
            autoExpandColumn: 'vlanportids',
            fields: [
                {name: 'uid'},
                {name: 'severity'},
				{name: 'name'},
				{name: 'intname'},
				{name: 'description'},
                {name: 'status'},
                {name: 'hasMonitor'},
                {name: 'monitor'},
                {name: 'vlanportids'},
                {name: 'vlanporttype'},
                {name: 'vlanpvid'},
                {name: 'vlantag'},		
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                width: 60,
            },{
                id: 'name',
                dataIndex: 'intname',
                header: _t('Name'),
                width: 160,
                renderer: render_link,
            },{
                id: 'description',
                dataIndex: 'description',
                header: _t('Description'),
                width: 180,
			},{
                id: 'vlanportids',
                dataIndex: 'vlanportids',
                header: _t('Vlan Members'),
                sortable: true,
			},{
                id: 'vlanporttype',
                dataIndex: 'vlanporttype',
                header: _t('Port Type'),
                sortable: true,
                width: 120,
            },{
                id: 'vlanpvid',
                dataIndex: 'vlanpvid',
                header: _t('PvId'),
                sortable: true,
			},{
                id: 'vlantag',
                dataIndex: 'vlantag',
                header: _t('Vlan Tag'),
                sortable: true,
            }]
        });
        ZC.NortelVlanPortPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('NortelVlanPortPanel', ZC.NortelVlanPortPanel);
ZC.registerName('NortelVlanPort', _t('Ports Table'), _t('Ports Tables'));

ZC.NortelFanPanel = Ext.extend(ZC.ComponentGridPanel, {
    subComponentGridPanel: false,
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'NortelFan',
            fields: [
                {name: 'uid'},
                {name: 'severity'},
				{name: 'name'},
                {name: 'status'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitored'},
                {name: 'monitor'},
                {name: 'fanstatus'},
                {name: 'fandesc'},
                {name: 'locking'},
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                width: 60,
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
            },{
                id: 'fandesc',
                dataIndex: 'fandesc',
                header: _t('Description'),
                sortable: true,
                width: 120,
            },{
                id: 'fanstatus',
                dataIndex: 'fanstatus',
                header: _t('Status'),
                sortable: true,
                width: 120,
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
            },{ 
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                width: 72,
                renderer: Zenoss.render.locking_icons,
            }]
        });
        ZC.NortelFanPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('NortelFanPanel', ZC.NortelFanPanel);
ZC.registerName('NortelFan', _t('Fan'), _t('Fans'));

ZC.NortelPowerPanel = Ext.extend(ZC.ComponentGridPanel, {
    subComponentGridPanel: false,
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'NortelPower',
            fields: [
                {name: 'uid'},
                {name: 'severity'},
				{name: 'name'},
                {name: 'status'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitored'},
                {name: 'monitor'},
                {name: 'powerstatus'},
                {name: 'powerdesc'},
                {name: 'locking'},
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                width: 60,
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
            },{
                id: 'powerdesc',
                dataIndex: 'powerdesc',
                header: _t('Description'),
                sortable: true,
                width: 180,
            },{
                id: 'powerstatus',
                dataIndex: 'powerstatus',
                header: _t('Status'),
                sortable: true,
                width: 120,
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
            },{ 
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                width: 72,
                renderer: Zenoss.render.locking_icons,
            }]
        });
        ZC.NortelPowerPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('NortelPowerPanel', ZC.NortelPowerPanel);
ZC.registerName('NortelPower', _t('Power Supply'), _t('Power Supplies'));

ZC.NortelStatusPanel = Ext.extend(ZC.ComponentGridPanel, {
    subComponentGridPanel: false,
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'NortelStatus',
            fields: [
                {name: 'uid'},
                {name: 'severity'},
				{name: 'name'},
                {name: 'status'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitored'},
                {name: 'monitor'},
                {name: 'tmpvalue'},
                {name: 'cpuusage'},
                {name: 'availablemem'},
                {name: 'totalmem'},
                {name: 'usedmem'},
                {name: 'locking'},
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                width: 60,
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
            },{
                id: 'cpuusage',
                dataIndex: 'cpuusage',
                header: _t('Cpu% Usage'),
                sortable: true,
                width: 120,
            },{
                id: 'totalmem',
                dataIndex: 'totalmem',
                header: _t('Total Mem'),
                sortable: true,
                width: 120,
            },{
                id: 'availablemem',
                dataIndex: 'availablemem',
                header: _t('Available Mem'),
                sortable: true,
                width: 120,
            },{
                id: 'usedmem',
                dataIndex: 'usedmem',
                header: _t('Used Mem'),
                sortable: true,
                width: 120,
            },{
                id: 'tmpvalue',
                dataIndex: 'tmpvalue',
                header: _t('Temperature'),
                sortable: true,
                width: 120,
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
            },{ 
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                width: 72,
                renderer: Zenoss.render.locking_icons,
            }]
        });
        ZC.NortelStatusPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('NortelStatusPanel', ZC.NortelStatusPanel);
ZC.registerName('NortelStatus', _t('Switch Status'), _t('Switch Status'));

ZC.NortelMltStatusPanel = Ext.extend(ZC.ComponentGridPanel, {
    subComponentGridPanel: false,
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'NortelMltStatus',
	    autoExpandColumn: 'nmltvlans',
            fields: [
                {name: 'uid'},
                {name: 'severity'},
		{name: 'name'},
                {name: 'nmltvlans'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitored'},
                {name: 'monitor'},
                {name: 'nmltenable'},
                {name: 'nmltstatus'},
                {name: 'locking'},
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                width: 60,
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
		width: 180,
            },{
                id: 'nmltvlans',
                dataIndex: 'nmltvlans',
                header: _t('Vlans'),
                sortable: true,
            },{
                id: 'nmltenable',
                dataIndex: 'nmltenable',
                header: _t('Enabled?'),
                sortable: true,
                width: 120,
            },{
                id: 'nmltstatus',
                dataIndex: 'nmltstatus',
                header: _t('Status'),
                sortable: true,
                width: 120,
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
            },{ 
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                width: 72,
                renderer: Zenoss.render.locking_icons,
            }]
        });
        ZC.NortelMltStatusPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('NortelMltStatusPanel', ZC.NortelMltStatusPanel);
ZC.registerName('NortelMltStatus', _t('MLT Status'), _t('MLT Status'));

ZC.PassportMltStatusPanel = Ext.extend(ZC.ComponentGridPanel, {
    subComponentGridPanel: false,
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'PassportMltStatus',
            autoExpandColumn: 'mltvlans',
            fields: [
                {name: 'uid'},
                {name: 'severity'},
		{name: 'name'},
                {name: 'mltvlans'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitored'},
                {name: 'monitor'},
                {name: 'mlttype'},
                {name: 'mltruntype'},
                {name: 'mltenable'},
                {name: 'mltstatus'},
                {name: 'locking'},
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                width: 60,
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
		width: 120,
            },{
                id: 'mltvlans',
                dataIndex: 'mltvlans',
                header: _t('Vlans'),
                sortable: true,
            },{
                id: 'mlttype',
                dataIndex: 'mlttype',
                header: _t('Configured Type'),
                sortable: true,
                width: 120,
            },{
                id: 'mltruntype',
                dataIndex: 'mltruntype',
                header: _t('Running type'),
                sortable: true,
                width: 120,
            },{
                id: 'mltenable',
                dataIndex: 'mltenable',
                header: _t('Enabled?'),
                sortable: true,
                width: 120,
            },{
                id: 'mltstatus',
                dataIndex: 'mltstatus',
                header: _t('Status'),
                sortable: true,
                width: 120,
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
            },{ 
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                width: 72,
                renderer: Zenoss.render.locking_icons,
            }]
        });
        ZC.PassportMltStatusPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('PassportMltStatusPanel', ZC.PassportMltStatusPanel);
ZC.registerName('PassportMltStatus', _t('MLT Status'), _t('MLT Status'));

ZC.NortelConDevicePanel = Ext.extend(ZC.ComponentGridPanel, {
    subComponentGridPanel: false,
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'NortelConDevice',
            autoExpandColumn: 'sysname',
            fields: [
                {name: 'uid'},
                {name: 'severity'},
                {name: 'name'},
                {name: 'status'},
                {name: 'hasMonitor'},
                {name: 'monitor'},
                {name: 'localint'},
                {name: 'macaddr'},
                {name: 'sysname'},
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                width: 60,
            },{
                id: 'sysname',
                dataIndex: 'sysname',
                header: _t('Remote Device'),
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('IP Address'),
            },{
                id: 'macaddr',
                dataIndex: 'macaddr',
                header: _t('Mac Address'),
                sortable: true,
                width: 120,
            },{
                id: 'localint',
                dataIndex: 'localint',
                header: _t('Local Interface'),
                sortable: true,
            },{
                id: 'monitor',
                dataIndex: 'monitor',
                header: _t('Monitored')
            }]
        });
        ZC.NortelConDevicePanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('NortelConDevicePanel', ZC.NortelConDevicePanel);
ZC.registerName('NortelConDevice', _t('Connected Devices'), _t('Connected Device'));

})();

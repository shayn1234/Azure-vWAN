from cloudify import ctx
from cloudify.state import ctx_parameters as inputs

sites = {
  "washington": {"wanname": "SampleVirtualWan", "hubname": "SampleVirtualHub", "ip": "1.2.3.4", "sitename" : "washington", "connectionname" : "washington-conn", "sitebgpasn" : 65516, "sitepeeringaddr" : "1.1.1.1", "siteaddressprefix" : "192.168.1.0/24"},
  "oregon": {"wanname": "SampleVirtualWan", "hubname": "SampleVirtualHub", "ip": "1.2.3.5", "sitename" : "oregon", "connectionname" : "oregon-conn", "sitebgpasn" : 65515, "sitepeeringaddr" : "1.1.1.2", "siteaddressprefix" : "192.168.2.0/24"}
}

ctx.logger.info('The site-config operation input is : {0}'
                .format(inputs))

ctx.instance.runtime_properties['wan_name'] = sites[inputs['site']]['wanname']
ctx.instance.runtime_properties['hub_name'] = sites[inputs['site']]['hubname']
ctx.instance.runtime_properties['site_ip'] = sites[inputs['site']]['ip']
ctx.instance.runtime_properties['site_name'] = sites[inputs['site']]['sitename']
ctx.instance.runtime_properties['connection_name'] = sites[inputs['site']]['connectionname']
ctx.instance.runtime_properties['site_bgpasn'] = sites[inputs['site']]['sitebgpasn']
ctx.instance.runtime_properties['site_peeringaddr'] = sites[inputs['site']]['sitepeeringaddr']
ctx.instance.runtime_properties['site_addrprefix'] = sites[inputs['site']]['siteaddressprefix']



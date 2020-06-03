#!/usr/bin/env python

import tempfile
from jinja2 import Template
from cloudify import ctx
from cloudify.state import ctx_parameters as inputs

def main():
    ctx.logger.info("Configuring vpngateway connections")
    template = Template(ctx.get_resource(inputs['template_file']))
    with tempfile.NamedTemporaryFile(delete=False) as temp_config:
        temp_config.write(template.render(connections=inputs['connection_list']))
    ctx.logger.info("Rendered file name is' {0}\n".format(temp_config.name))
    ctx.instance.runtime_properties['ARMfile'] = temp_config.name

if __name__ == "__main__":
    main()
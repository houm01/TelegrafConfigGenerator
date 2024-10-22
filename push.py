#!/usr/bin/env python3

from ops_automate.telegraf_config.build_telegraf_config import BuildTelegrafConfig




def build_config_push_remote_host(namespace, output_folder):
    build_telegraf_config = BuildTelegrafConfig(init_type='xlsx',
                                                resource_path='/app/ops_automate/ops_automate/data/test',
                                                output_path='/app/ops_automate/ops_automate/data/test')
    build_telegraf_config.init_config()
    # build_telegraf_config.output()




if __name__ == '__main__':
    build_config_push_remote_host(
        namespace='test',
        output_folder='/app/ops_automate/data',
        
    )
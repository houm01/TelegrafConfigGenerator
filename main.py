#!/usr/bin/env python3

import os
import toml
import argparse
from rich.console import Console
from rich.table import Table
from jinja2 import FileSystemLoader, Environment


console = Console()


# 创建解析器
parser = argparse.ArgumentParser(description='Telegraf Config Generator')

# 添加参数
parser.add_argument('--config', type=str, default='7', help='获取历史数据的天数, 默认为最近7天')
parser.add_argument('--instance', type=str, default='yes', help='是否获取所有主机, 默认为 yes')
parser.add_argument('--output', type=str, default='yes', help='是否获取所有主机, 默认为 yes')

# 解析参数
args = parser.parse_args()

config_path = args.config
instance_path = args.instance
output_path = args.output


console.log(f"config file path: {config_path}", style='blue')
console.log(f"instance file path: {instance_path}", style='blue')
console.log(f"output file path: {output_path}", style='blue')

instance_config = toml.load(instance_path)

# console.log(config)
console.log(instance_config)

# table = Table(title="instance_snmp")

# table.add_column("source", justify="right", style="cyan")
# table.add_column("hostname", style="magenta")
# table.add_column("ip", justify="center", style="green")
# table.add_column("port", justify="center", style="green")

snmp_instances = instance_config['instance']['snmp']
# for snmp_instance in snmp_instances:
    # print(snmp_instance)
    # table.add_row(snmp_instance['source'], snmp_instance['hostname'], snmp_instance['ip'], str(snmp_instance['port']))


# console.print(table)

def render_config(source, monitor_type, config, instances):
    jinja2_path = '/data/TelegrafConfigGenerator/jinja2'
    j2_loader = FileSystemLoader(jinja2_path)
    env = Environment(loader=j2_loader)
    j2_tmpl = env.get_template('telegraf_config.j2')

    
    # print(instance['config']['inputs'])
    result = j2_tmpl.render(config=instance_config['config'], monitor_type=monitor_type, instances=instances)

    # output_path = self.output_path + build_output_path_identifier() + '/'
    # if not os.path.exists(output_path):
    #     os.makedirs(output_path) 
    with open(output_path + f'telegraf_{source}_{monitor_type}.conf', 'w') as f:
        f.write(result)


def main():
    for source, instances in snmp_instances.items():
        render_config(source=source, monitor_type='snmp', config='', instances=instances)
    
    


if __name__ == '__main__':
    main()
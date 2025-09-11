import json
from src import Rule
from src import Packet

def load_rules(file_path):
    rules = []
    try:
        with open(file=file_path, mode='r',encoding='utf-8') as file: 
            for line in file:
                rule = rule_parser(line)
                rules.append(rule)
    except FileExistsError:
        print('Error: File doesn\'t exist')
    except IOError as e:
        print(f'Error: {e}')
    return rules


def rule_parser(str_rule):
    attributes = str_rule.split()
    rule = Rule(action = attributes[0], src_ip = attributes[1], dst_ip = attributes[2],
                protocol = attributes[3], src_port = attributes[4], dst_port = attributes[5])
    return rule

def load_packets(file_path):
    packets = []
    with open(file_path) as file:
        data = json.load(file)
    for packet_data in data:
        packet = Packet(packet_data['src'],packet_data['dst'], packet_data['proto'],
                        packet_data['sport', packet_data['dport']])  
        packets.append(packets)
    return packets


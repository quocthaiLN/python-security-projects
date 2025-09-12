from src import Rule
from src import Packet
from src import parser
from src import matcher
from src.logger import logger

def main():

    basic_rule_path = 'rules/basic_rules.txt'
    advanced_rule_path = 'rules/advanced_rules.txt'
    sample_packets_path = 'packets/sample_packets.json'

    rules = parser.load_rules(advanced_rule_path)
    packets = parser.load_packets(sample_packets_path)

    for packet in packets:
        matcher.match_packet(packet=packet, rules=rules)
       
if __name__ == '__main__':
    main()
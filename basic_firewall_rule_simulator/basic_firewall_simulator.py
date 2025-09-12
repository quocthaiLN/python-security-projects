import argparse
from src import parser
from src import matcher
from src import logger



def run_firewall(rules_path: str, packets_path: str):
    try:
        logger.info(f'Run firewall simulator...')
        rules = parser.load_rules(rules_path)
        logger.info(f'Load {len(rules)} rules from {rules_path}')
        packets = parser.load_packets(packets_path)
        logger.info(f'Load {len(packets)} packets from {packets_path}')
        for packet in packets:
            matcher.match_packet(packet=packet, rules=rules)
        logger.info(f'Stop firewall simulator...')
    except Exception as e:
        print(f'Firewall simulator fail: {e}')
        raise

def parse_args():
    parser_cli = argparse.ArgumentParser(
        description="Basic Firewall Rule Simulator",
        epilog='Example: python basic_firewall_simulator.py -r rules\\basic_rules.txt -p packets\\sample_packets.json'
    )
    parser_cli.add_argument(
        "--rules", "-r", type=str, required=True,
        help="Path to firewall rules file"
    )
    parser_cli.add_argument(
        "--packets", "-p", type=str, required=True,
        help="Path to packet JSON file"
    )
    return parser_cli.parse_args()

if __name__ == "__main__":
    args = parse_args()
    run_firewall(rules_path=args.rules,
                 packets_path=args.packets)
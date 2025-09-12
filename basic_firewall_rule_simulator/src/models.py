from ipaddress import IPv4Address
from ipaddress import IPv4Network
from ipaddress import AddressValueError
from ipaddress import NetmaskValueError
import logging

class Rule:
    def __init__(self, action, src_ip, dst_ip, protocol, src_port, dst_port):
        self.action = action
        self.src_ip = src_ip
        self.dst_ip = dst_ip
        self.protocol = protocol
        self.src_port = src_port
        self.dst_port = dst_port

    def matches(self, packet):
        
        try:
            # check src_ip
            if self.src_ip == 'ANY':
                pass
            elif self.src_ip.find('/') != -1:
                rule_src_ip_network = IPv4Network(self.src_ip)
                packet_src_ip_address = IPv4Address(packet.src_ip)
                if packet_src_ip_address not in rule_src_ip_network:
                    return False
            else:
                rule_src_ip_address = IPv4Address(self.src_ip)
                packet_src_ip_address = IPv4Address(packet.src_ip)
                if packet_src_ip_address != rule_src_ip_address:
                    return False
            
            # check dst_ip
            if self.dst_ip == 'ANY':
                pass
            elif self.dst_ip.find('/') != -1:
                rule_dst_ip_network = IPv4Network(self.dst_ip)
                packet_dst_ip_address = IPv4Address(packet.dst_ip)
                if packet_dst_ip_address not in rule_dst_ip_network:
                    return False
            else:
                rule_dst_ip_address = IPv4Address(self.dst_ip)
                packet_dst_ip_address = IPv4Address(packet.dst_ip)
                if packet_dst_ip_address != rule_dst_ip_address:
                    return False
                
            # check protocol
            if self.protocol == 'ANY':
                pass
            else:
                if self.protocol != packet.protocol:
                    return False
            
            # check src_port
            if self.src_port == 'ANY':
                pass
            else:
                if self.src_port != packet.src_port:
                    return False
            # check dst_port
            if self.dst_port == 'ANY':
                pass
            else:
                if self.dst_port != packet.dst_port:
                    return False
            return True
        except AddressValueError:
            logging.exception('Invalid IPv4 address!', exc_info=False)
        except NetmaskValueError:
            logging.exception('Invalid netmask!', exc_info=False)
        finally:
            return False

class Packet:
    def __init__(self, src_ip, dst_ip, protocol, src_port, dst_port):
        self.src_ip = src_ip
        self.dst_ip = dst_ip
        self.protocol = protocol
        self.src_port = src_port
        self.dst_port = dst_port
class Rule:
    def __init__(self, action, src_ip, dst_ip, protocol, src_port, dst_port):
        self.action = action
        self.src_ip = src_ip
        self.dst_ip = dst_ip
        self.protocol = protocol
        self.src_port = src_port
        self.dst_port = dst_port

    def matches(self, packet):
        pass

class Packet:
    def __init__(self, src_ip, dst_ip, protocol, src_port, dst_port):
        self.src_ip = src_ip
        self.dst_ip = dst_ip
        self.protocol = protocol
        self.src_port = src_port
        self.dst_port = dst_port
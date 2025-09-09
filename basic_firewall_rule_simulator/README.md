Basic Firewall Rule Simulator

1.  Mục tiêu đồ án: xây dựng một chương trình Python mô phỏng hành vi lọc gói tin của firewall theo bộ rule. Chương trình phải:
    Phân tích (parse) rule từ file,
    So khớp (match) mỗi packet với rule theo thứ tự,
    Trả về quyết định ALLOW hoặc DENY,
    Ghi log kết quả và hỗ trợ chế độ mô phỏng (simulate) với file input các packet.

2.  Yêu cầu chức năng (bắt buộc)
    2.1. Định nghĩa rule (format)
    Mỗi rule là một dòng text hoặc một entry trong JSON.
    Định dạng text (gợi ý):
    <ACTION> <SRC_IP> <DST_IP> <PROTOCOL> <SRC_PORT> <DST_PORT> [# optional comment]
    Ví dụ:
    ALLOW 192.168.1.0/24 ANY TCP ANY 80 # allow http from local net
    DENY ANY 10.0.0.5 TCP ANY 22 # block ssh to 10.0.0.5

             Giá trị hợp lệ:
                 ACTION ∈ {ALLOW, DENY}
                 SRC_IP, DST_IP = IPv4 address, CIDR (e.g., 192.168.1.0/24), IP range (optional), hoặc ANY
                 PROTOCOL ∈ {TCP, UDP, ICMP, ANY}
                 SRC_PORT, DST_PORT = integer (1-65535), port-range 1000-2000, hoặc ANY
                 # comment tùy chọn

             Gợi ý thêm: hỗ trợ JSON rules kiểu:
                 {"action":"ALLOW","src":"192.168.1.0/24","dst":"ANY","proto":"TCP","sport":"ANY","dport":"80","comment":"allow http"}

    2.2. Packet model
    Một packet mô phỏng tối thiểu gồm:
    src_ip, dst_ip (IPv4)
    proto (TCP/UDP/ICMP)
    src_port, dst_port (nếu proto không có port, set null)
    Chương trình cho phép đọc danh sách packet từ file JSON/CSV hoặc sinh ngẫu nhiên để test.

    2.3. Cơ chế so khớp rule
    First-match wins: duyệt rules theo thứ tự file; rule đầu tiên match là quyết định.
    Hỗ trợ:
    CIDR membership (ví dụ 192.168.1.10 in 192.168.1.0/24)
    ANY và \*
    Port ranges
    Exact match
    Nếu không rule nào match → áp dụng default policy (cấu hình được; mặc định DENY).

    2.4. I/O & CLI
    Chạy từ CLI:
    python fw_sim.py --rules rules.txt --packets packets.json --default DENY --log fw.log
    Ý nghĩa từng tham số:
    --rules rules.txt: đường dẫn file chứa rule.
    --packets packets.json: đường dẫn file chứa các packet để test.
    --default DENY: policy mặc định (nếu không rule nào match).
    --log fw.log: ghi log kết quả kiểm tra packet vào file fw.log.
    Nếu bỏ --packets, thì chương trình có thể chạy ở interactive mode (người dùng nhập packet qua CLI).

    2.5. Logging & Report
    Ghi log mỗi packet: timestamp, packet info, matched rule (line# or id), action.
    Hỗ trợ xuất báo cáo tóm tắt: tổng số packet, số ALLOW, số DENY, top rules triggered.

    2.6. Unit tests
    Viết test cases unit (ví dụ dùng pytest) bao gồm: IP in CIDR, port range, ANY, first-match, default policy, invalid rule handling.

3.  Yêu cầu kỹ thuật / công nghệ (bắt buộc) 🛠️
    Ngôn ngữ: Python 3.13
    Thư viện:
    ipaddress (builtin) — để xử lý IP/CIDR.
    argparse — CLI.
    pytest — testing.
    Code quality: type hints, docstrings, modular (tách parser, matcher, simulator, logger).
    Packaging: requirements.txt, README.md với hướng dẫn cài, chạy, test.

4.  Yêu cầu phi chức năng (chất lượng)
    Modularity: tách Rule, Packet, Firewall (class) rõ ràng.
    Documentation: README gồm mô tả, ví dụ rule file, cách chạy, ví dụ đầu ra.
    Robustness: validate input, xử lý lỗi rule không hợp lệ (log + skip).
    Test coverage: tối thiểu 70% cho phần core (matching logic).
    Coding style: chuẩn PEP8, commit sạch (git history có ý nghĩa).

5.  Deliverables
    Source code trong repo (git) có cấu trúc rõ ràng.
    rules/ folder: ít nhất 3 rule file ví dụ (basic, advanced, conflict).
    packets/ folder: file JSON/CSV test packets (ít nhất 10).
    tests/ folder: pytest test suite.
    README.md: install, run, ví dụ, license.

6.  Test cases mẫu (bắt buộc thử) 🧪
    6.1. Rules (rules.txt)

    # 1

         ALLOW 192.168.1.0/24 ANY TCP ANY 80 # allow local -> http

    # 2

         DENY ANY 10.0.0.5 TCP ANY 22 # block ssh to 10.0.0.5

    # 3

         ALLOW ANY ANY ICMP ANY ANY # allow ping

    # 4

         DENY 203.0.113.0/24 ANY ANY ANY ANY # block entire net

    # 5

         ALLOW ANY ANY ANY ANY ANY # allow everything else (if placed here, it overrides DENY below)

    6.2. Packets (packets.json) — kèm kết quả mong đợi:

    # 1

    {"src":"192.168.1.10","dst":"10.0.0.5","proto":"TCP","sport":12345,"dport":80}
    → ALLOW (match rule 1)

    # 2

    {"src":"8.8.8.8","dst":"10.0.0.5","proto":"TCP","sport":40000,"dport":22}
    → DENY (match rule 2)

    # 3

    {"src":"192.0.2.1","dst":"198.51.100.2","proto":"ICMP","sport":null,"dport":null}
    → ALLOW (match rule 3)

    # 4

    {"src":"203.0.113.5","dst":"1.2.3.4","proto":"UDP","sport":5000,"dport":53}
    → DENY (match rule 4)

    # 5

    {"src":"1.1.1.1","dst":"2.2.2.2","proto":"TCP","sport":4000,"dport":443}
    → ALLOW (match rule 5 OR default if rule 5 absent and default=ALLOW)

    # 6

    Edge case: invalid ip
    {"src":"300.1.1.1","dst":"2.2.2.2","proto":"TCP","sport":4000,"dport":443}
    → Behaviour: log error, skip packet or mark DENY (define in README).
    (…thêm các test cho port range, ANY, order conflicts…)

7.  Các test unit cần có (ít nhất)
    test_ip_in_cidr
    test_port_range_match
    test_any_matches
    test_first_match_priority
    test_default_policy
    test_invalid_rule_handling
    test_icmp_has_no_ports

8.  Ví dụ CLI & run commands

    # chạy simulation với rules.txt và packets.json

    python fw_sim.py --rules rules/rules.txt --packets packets/packets.json --default DENY --log out/fw.log

    # chỉ parse rules và show rule table

    python fw_sim.py --rules rules/rules.txt --show-rules

9.  Cấu trúc repo
    basic_firewall_simulator/
    ├─ rules/
    │ ├─ basic_rules.txt
    │ ├─ advanced_rules.json
    ├─ packets/
    │ ├─ sample_packets.json
    ├─ src/
    │ ├─ basic_firewall_simulator.py # nới điều phối và xử lí
    │ ├─ parser.py # dùng để đọc rule từ file và chuyển nó thành object để xử lý
    │ ├─ matcher.py # lặp qua từng packet để kiểm tra và trả về ALLOW/DENY/default privacy
    │ ├─ models.py # Rule, Packet classes
    │ ├─ logger.py # ghi log
    ├─ tests/
    │ ├─ test_matcher.py
    ├─ README.md

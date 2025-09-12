# Basic Firewall Rule Simulator --- Tài liệu yêu cầu

## Tổng quan

**Mục tiêu:** Xây dựng chương trình Python mô phỏng hành vi lọc gói tin
(firewall) theo bộ rule.\
Chương trình cần thực hiện:

- Phân tích (parse) rule từ file (text hoặc JSON).
- So khớp (match) mỗi packet theo thứ tự rules (first-match wins).
- Trả về quyết định **ALLOW** hoặc **DENY** cho mỗi packet.
- Ghi log kết quả và hỗ trợ chế độ mô phỏng (simulate) với file input
  các packet.

---

## 1. Yêu cầu chức năng (bắt buộc)

### 1.1 Định nghĩa rule (format)

Mỗi rule có thể là dòng text hoặc entry trong JSON.

**Định dạng text (gợi ý):**

    <ACTION> <SRC_IP> <DST_IP> <PROTOCOL> <SRC_PORT> <DST_PORT> [# optional comment]

**Ví dụ:**

    ALLOW 192.168.1.0/24 ANY TCP ANY 80 # allow http from local net
    DENY ANY 10.0.0.5 TCP ANY 22 # block ssh to 10.0.0.5

**Giá trị hợp lệ:** - `ACTION` ∈ {`ALLOW`, `DENY`} - `SRC_IP`, `DST_IP`
= IPv4 address, CIDR (vd. `192.168.1.0/24`), IP range (tuỳ chọn), hoặc
`ANY` - `PROTOCOL` ∈ {`TCP`, `UDP`, `ICMP`, `ANY`} - `SRC_PORT`,
`DST_PORT` = integer `1-65535`, port-range `1000-2000`, hoặc `ANY` -
`# comment` là tùy chọn (bắt đầu bằng `#`)

**JSON rule (gợi ý):**

```json
{
  "action": "ALLOW",
  "src": "192.168.1.0/24",
  "dst": "ANY",
  "proto": "TCP",
  "sport": "ANY",
  "dport": "80",
  "comment": "allow http"
}
```

---

### 1.2 Packet model

Mỗi packet mô phỏng tối thiểu gồm: - `src` (src_ip) --- IPv4 - `dst`
(dst_ip) --- IPv4 - `proto` --- `"TCP" | "UDP" | "ICMP"` - `sport`,
`dport` --- số nguyên hoặc `null` nếu proto không có port

**Input packets**: đọc từ file JSON hoặc CSV hoặc sinh ngẫu nhiên để
test.

**Ví dụ JSON packet:**

```json
{
  "src": "192.168.1.10",
  "dst": "10.0.0.5",
  "proto": "TCP",
  "sport": 12345,
  "dport": 80
}
```

---

### 1.3 Cơ chế so khớp rule

- **First-match wins**: duyệt rules theo thứ tự; rule đầu tiên `match`
  là quyết định.
- Hỗ trợ:
  - CIDR membership (vd. `192.168.1.10` in `192.168.1.0/24`)
  - `ANY` hoặc `*`
  - Port ranges (`1000-2000`)
  - Exact match
- Nếu không rule nào match → áp dụng **default policy** (cấu hình
  được; mặc định `DENY`).

---

### 1.4 I/O & CLI

Chạy từ CLI:

```bash
python fw_sim.py --rules rules.txt --packets packets.json --default DENY --log fw.log
```

**Tùy chọn:** - `--rules <file>`: đường dẫn file rules (text hoặc
json). - `--packets <file>`: đường dẫn file packet input (JSON/CSV). Nếu
không có, bật interactive mode. - `--default <ALLOW|DENY>`: policy mặc
định nếu không rule nào match. - `--log <file>`: file log (append hoặc
rotate tuỳ config). - `--show-rules`: chỉ parse và hiển thị rule
table. - `--simulate`: chế độ mô phỏng (in từng bước).

Nếu bỏ `--packets`, chương trình cho phép nhập packet qua CLI
(interactive) hoặc stdin.

---

### 1.5 Logging & Report

- **Log mỗi packet**: timestamp, packet info, matched rule (line# hoặc
  id), action (ALLOW/DENY), lý do nếu là lỗi.
- **Report tóm tắt**: tổng số packet, số ALLOW, số DENY, top rules
  triggered (theo count).
- Đề xuất định dạng log (CSV / JSON lines / plain text):

**Ví dụ JSON line log:**

```json
{
  "ts": "2025-09-12T15:00:00+07:00",
  "packet": {
    "src": "1.2.3.4",
    "dst": "5.6.7.8",
    "proto": "TCP",
    "sport": 1234,
    "dport": 80
  },
  "matched_rule": { "id": 3, "text": "ALLOW 1.0.0.0/8 ..." },
  "action": "ALLOW"
}
```

---

### 1.6 Unit tests

Viết test cases (pytest) bao gồm: - `test_ip_in_cidr` -
`test_port_range_match` - `test_any_matches` -
`test_first_match_priority` - `test_default_policy` -
`test_invalid_rule_handling` - `test_icmp_has_no_ports`

---

## 2. Yêu cầu kỹ thuật / công nghệ (bắt buộc) 🛠️

- **Ngôn ngữ:** Python 3.13
- **Thư viện:** builtin `ipaddress`, `argparse`, `logging`, `json`,
  `csv`, `dataclasses`, `typing`. Test: `pytest`.
- **Chất lượng code:** type hints, docstrings, modular (parser,
  matcher, simulator, logger tách riêng).
- **Packaging:** `requirements.txt` (nếu có thư viện ngoài),
  `README.md` hướng dẫn cài, chạy, test.

---

## 3. Yêu cầu phi chức năng (chất lượng)

- **Modularity:** tách `Rule`, `Packet`, `Firewall` (class) rõ ràng.
- **Documentation:** README có mô tả, ví dụ rule file, ví dụ chạy, kết
  quả mẫu.
- **Robustness:** validate input, xử lý rule không hợp lệ (log +
  skip).
- **Test coverage:** tối thiểu 70% cho phần core (matching logic).
- **Coding style:** PEP8, commit lịch sử rõ ràng.

---

## 4. Deliverables

- Source code trong repo (git) với cấu trúc rõ ràng.
- `rules/` folder: ≥3 rule file ví dụ (basic, advanced, conflict).
- `packets/` folder: sample packets JSON/CSV (ít nhất 10).
- `tests/` folder: pytest test suite.
- `README.md`: install, run, ví dụ, license.

---

## 5. Test cases mẫu

### 5.1 Rules (`rules.txt`)

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

### 5.2 Packets (`packets.json`) --- kèm kết quả mong đợi

```json
{"src":"192.168.1.10","dst":"10.0.0.5","proto":"TCP","sport":12345,"dport":80}
# → ALLOW (match rule 1)

{"src":"8.8.8.8","dst":"10.0.0.5","proto":"TCP","sport":40000,"dport":22}
# → DENY (match rule 2)

{"src":"192.0.2.1","dst":"198.51.100.2","proto":"ICMP","sport":null,"dport":null}
# → ALLOW (match rule 3)

{"src":"203.0.113.5","dst":"1.2.3.4","proto":"UDP","sport":5000,"dport":53}
# → DENY (match rule 4)

{"src":"1.1.1.1","dst":"2.2.2.2","proto":"TCP","sport":4000,"dport":443}
# → ALLOW (match rule 5 OR default if rule 5 absent and default=ALLOW)

# Edge case: invalid ip
{"src":"300.1.1.1","dst":"2.2.2.2","proto":"TCP","sport":4000,"dport":443}
# → Hành vi: log error, skip packet hoặc mark DENY (quy định rõ trong README).
```

---

## 6. Ví dụ CLI & run commands

- Chạy simulation:

```bash
python fw_sim.py --rules rules/rules.txt --packets packets/packets.json --default DENY --log out/fw.log
```

- Chỉ parse rules và show rule table:

```bash
python fw_sim.py --rules rules/rules.txt --show-rules
```

- Interactive (stdin):

```bash
cat packets/example.json | python fw_sim.py --rules rules/rules.txt --default DENY
```

---

## 7. Cấu trúc repo (gợi ý)

    basic_firewall_simulator/
    ├─ rules/
    │  ├─ basic_rules.txt
    │  ├─ advanced_rules.json
    ├─ packets/
    │  ├─ sample_packets.json
    ├─ src/
    │  ├─ fw_sim.py               # entrypoint: CLI & orchestrator
    │  ├─ parser.py               # parse rules -> Rule objects
    │  ├─ matcher.py              # matching logic, first-match wins
    │  ├─ models.py               # Rule, Packet dataclasses
    │  ├─ logger.py               # logging & report generation
    │  ├─ utils.py                # helper: port parsing, ip validation
    ├─ tests/
    │  ├─ test_matcher.py
    │  ├─ test_parser.py
    ├─ requirements.txt
    ├─ README.md

---

## 8. Gợi ý triển khai (kỹ thuật)

- **Parser:** đọc line-by-line; bỏ comment; tokenize; validate fields;
  convert to `Rule` object. Nếu rule invalid → log + skip.
- **IP/CIDR handling:** dùng `ipaddress` module (`IPv4Address`,
  `IPv4Network`). Để check CIDR membership:
  `IPv4Address in IPv4Network`.
- **Port parsing:** hỗ trợ `ANY`, single port (`80`), and range
  (`1000-2000`). Lưu dạng tuple `(low, high)` hoặc `None` cho ANY.
- **Matching order:** mỗi `Packet` được so khớp tuần tự với danh sách
  `Rule`. Trả về ngay khi match.
- **ICMP:** proto không có port --- `sport`/`dport` có thể là `None`
  --- matcher phải xử lý tương ứng.
- **Logging:** dùng `logging` module; cung cấp option
  `--log-format json|text`.
- **Testing:** viết pytest cho các hàm nhỏ (port parsing, ip_in_cidr)
  và integration test cho toàn bộ flow.
- **Performance:** rules thường không quá lớn; nếu mở rộng, có thể
  index theo protocol hoặc network để tối ưu matching.
- **Edge cases cần chỉ rõ trong README:** hành vi với invalid IP,
  ambiguous rules, overlapping CIDR (quy tắc first-match),
  case-sensitivity (`tcp` vs `TCP`).

---

## 9. Các quyết định cần định nghĩa rõ trong README

- Hành vi khi **rule invalid** (log + skip vs fail).
- Hành vi khi **packet invalid** (log + skip vs mark DENY).
- Format log mặc định (JSON lines khuyến nghị).
- Policy mặc định khi không rule nào match (mặc định `DENY`).
- Cách biểu diễn port-range trong file rules (gợi ý dùng `low-high`).

---

## 10. Tài liệu tham khảo & bước tiếp theo

- Nên thêm trong README: ví dụ rules, ví dụ log, hướng dẫn viết rule,
  cách thêm rule-range, cách đo coverage (`pytest --cov`).
- Nếu bạn muốn, tôi có thể:
  - Sinh sẵn template `parser.py` và `matcher.py` (kèm giải thích
    từng dòng).
  - Viết test suite mẫu `tests/test_matcher.py`.
  - Hoặc chuyển toàn bộ spec này thành `README.md` hoàn chỉnh trong
    repo.

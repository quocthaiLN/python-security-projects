# URL Scanner / Phishing Detector 🕵️‍♀️🔗

---

## 📌 Giới thiệu

Hệ thống **URL Scanner / Phishing Detector** là công cụ phân tích, đánh giá rủi ro và phát hiện trang lừa đảo (phishing).  
Mục tiêu: phát hiện nhanh các URL độc hại, phân loại mức độ nguy hiểm, và cung cấp lý giải rõ ràng cho kết quả.

---

## 🎯 Mục tiêu chính

- Phát hiện URL khả nghi (phishing / malware / scam).
- Cung cấp **risk score** và **giải thích (reasons)**.
- Hỗ trợ quét hàng loạt (bulk scan) và API.
- Có bộ kiểm thử và tiêu chí nghiệm thu rõ ràng.

---

## ✅ Phạm vi chức năng (MUST)

- **Đầu vào**: URL đơn, hoặc danh sách URL (CSV/JSON).
- **Phân tích tĩnh (static)**:
  - Kiểm tra cú pháp, chuẩn hoá URL.
  - Kiểm tra domain age, WHOIS, SSL/TLS validity.
  - Phát hiện Punycode / homograph.
  - So khớp blocklist / whitelist.
- **Phân tích động (dynamic)**:
  - Fetch HTML an toàn, phân tích form, script, redirect.
- **ML / Heuristic**: phân loại dựa trên feature.
- **Kết quả trả về**:
  - `label`: {SAFE, SUSPICIOUS, PHISHING, MALWARE}
  - `score`: 0.0 – 1.0
  - `reasons`: giải thích
  - `scan_details`: headers, cert, redirect chain
- **Logging & Audit**: lưu log scan theo policy.

---

## ⭐ Phạm vi chức năng (NICE-TO-HAVE)

- Screenshot trang web (headless).
- Phân tích JavaScript nâng cao.
- Tích hợp VirusTotal / Google Safe Browsing API.
- Dashboard thống kê.
- Quét theo lịch, alert (email/webhook).
- Tự học (retrain model).

---

## ⚙️ Yêu cầu phi chức năng

- **Hiệu suất**: scan đơn < 5s, hỗ trợ bulk concurrency.
- **Bảo mật**: sandbox request, sanitize input.
- **Riêng tư**: không log dữ liệu nhạy cảm.
- **Khả năng mở rộng**: modul hóa, dễ thay engine.
- **Ngôn ngữ**: Python 3.10+.

---

## 🧩 Kiến trúc đề xuất

1. **Ingest Layer** — CLI / API
2. **Preprocessor** — chuẩn hoá URL
3. **Scanner Engine** — Static + Dynamic + ML
4. **Threat DB** — blocklist/whitelist
5. **Storage & Logging** — SQLite/Postgres
6. **API / UI** — trả kết quả
7. **Worker / Queue** — bulk scan

---

## 🔌 API Spec (ví dụ)

### POST `/api/scan`

**Request**

```json
{
  "url": "http://tiny[.]ex",
  "options": {
    "timeout": 8,
    "follow_redirects": true,
    "user_agent": "URLScanner/1.0"
  }
}
```

**Response**

```json
{
  "job_id": "abc123",
  "submitted_at": "2025-09-12T15:30:00Z",
  "status": "completed",
  "result": {
    "label": "PHISHING",
    "score": 0.92,
    "reasons": [
      "domain_age < 7 days",
      "contains_punycode",
      "matched_blacklist_regex"
    ],
    "scan_details": {
      "redirect_chain": ["http://a.com", "http://b.com"],
      "tls": { "valid": false },
      "http_status": 200
    }
  }
}
```

---

## 💻 CLI Example

```
$ urlscan scan "http://example.com"
Result: PHISHING (0.86)
Reasons:
 - suspicious_tld
 - many_subdomains
```

---

## ✅ Test Cases & Acceptance

- **TC-001**: `https://www.wikipedia.org` → SAFE, score < 0.4
- **TC-002**: Domain < 7 days + login form → PHISHING, score >= 0.7
- **TC-003**: Punycode homograph → PHISHING
- **TC-004**: Malformed URL → HTTP 400
- **TC-005**: Bulk scan 1000 URLs → pass, no crash

Acceptance: tất cả test pass, false positive/negative trong giới hạn cho phép.

---

## 🔎 Dữ liệu & Intel

- Public datasets: PhishTank, OpenPhish.
- Local blocklist, WHOIS/DNS.

---

## 🔐 Chính sách bảo mật

- Không gửi token/cookie người dùng đi ngoài.
- Strip header nhạy cảm khi fetch.
- Tôn trọng robots.txt.

---

## 🛠️ Công cụ đề xuất

- HTTP: `requests` / `httpx`
- HTML parsing: `beautifulsoup4`, `lxml`
- Headless: `playwright` / `selenium`
- ML: `scikit-learn`, `xgboost`
- Queue: `celery` / `rq`
- DB: `sqlite` / `postgres`
- Testing: `pytest`
- Container: Docker

---

## 📦 Deliverables

- Source code GitHub + README.
- CLI + API (OpenAPI spec).
- Test-suite (pytest).
- Sample input/output.
- Dockerfile.

---

## ⏱️ Roadmap

- **Sprint 1**: Static scanner, CLI, unit tests.
- **Sprint 2**: API, bulk processing, basic ML.
- **Sprint 3**: Dynamic analysis, dashboard, threat-intel.

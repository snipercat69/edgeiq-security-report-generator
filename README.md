# 🛡️ EdgeIQ Security Report Generator

**Automated security assessment report generator — PDF/HTML reports from scan data.**

Aggregate vulnerability scan results from multiple EdgeIQ tools into polished, client-ready security reports with executive summaries and technical findings.

[![Project Stage](https://img.shields.io/badge/Stage-Beta-blue)](https://edgeiqlabs.com)
[![Python](https://img.shields.io/badge/Python-3.8+-green)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-orange)](LICENSE)

---

## What It Does

Takes raw scan output from EdgeIQ security tools (XSS Scanner, Network Scanner, etc.) and generates professional security reports — executive summary, severity breakdown, detailed findings, and remediation guidance.

---

## Key Features

- **Multi-tool aggregation** — combines output from all EdgeIQ scanners
- **Executive summary** — high-level overview for non-technical stakeholders
- **Severity scoring** — CVSS-style scoring for each finding
- **Remediation guidance** — actionable steps to fix each vulnerability
- **HTML/PDF export** — polished format ready for client delivery
- **Branded reports** — customizable logo, colors, and company name

---

## Prerequisites

- Python 3.8+
- `jinja2` for templating

---

## Installation

```bash
git clone https://github.com/snipercat69/edgeiq-security-report-generator.git
cd edgeiq-security-report-generator
pip install -r requirements.txt
cp config.json.example config.json
# Edit config.json with your company branding
```

---

## Quick Start

```bash
# Generate report from scan JSON
python3 scripts/generate_report.py --input scan_results.json --output report.html

# Generate from multiple sources
python3 scripts/generate_report.py --input xss_scan.json network_scan.json --format html --output report.html

# Email report
python3 scripts/generate_report.py --input scan.json --email client@example.com --subject "Q1 Security Report"
```

---

## Pricing

| Tier | Price | Features |
|------|-------|----------|
| **Free** | $0 | 5 reports/month, basic template |
| **Pro** | $20/mo | Unlimited reports, custom branding, PDF export, priority support |
| **Lifetime** | $100 one-time | All Pro features, forever |

---

## Integration with EdgeIQ Tools

Designed to work with all EdgeIQ scanners:

- **[EdgeIQ XSS Scanner](https://github.com/snipercat69/edgeiq-xss-scanner)** — XSS findings
- **[EdgeIQ Network Scanner](https://github.com/snipercat69/edgeiq-network-scanner)** — host/port findings
- **[EdgeIQ SQL Injection Scanner](https://github.com/snipercat69/edgeiq-sql-injection-scanner)** — injection findings

---

## Support

Open an issue at: https://github.com/snipercat69/edgeiq-security-report-generator/issues

---

*Part of EdgeIQ Labs — [edgeiqlabs.com](https://edgeiqlabs.com)*

#  Smart_Log_Analyzer

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)

A **modular, Python-based log auditing tool** built to automate server log analysis.  
Smart_Log_Analyzer parses raw server logs to detect error patterns, identify suspicious IP addresses, and generate actionable security and error reports.

Designed with **clarity, extensibility, and real-world use cases** in mind (DevOps monitoring, SOC analysis, firewall automation).

---

##  Table of Contents
- [Key Features](#-key-features)
- [Project Architecture](#-project-architecture)
- [Installation](#-installation)
- [Usage](#-usage)
- [Configuration](#-configuration)
- [Reports & Outputs](#-reports--outputs)
- [Limitations](#-limitations)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)

---

##  Key Features

- **Log Parsing Engine**  
  Regex-based extraction of IP addresses, timestamps, HTTP methods, and status codes.

- **Automated Error Analysis**  
  Aggregates and analyzes HTTP error responses (4xx & 5xx) to evaluate system health.

- **Security Threat Detection**  
  Identifies suspicious IPs based on abnormal request frequencies (401, 403, 404, 429).

- **Threshold-Based Alerting**  
  Triggers console alerts when error counts or suspicious IPs exceed safe limits.

- **Multi-Format Reporting**  
  Automatically generates:
  - `error_report.txt` – Error breakdown and counts
  - `security_report.csv` – Flagged IPs ready for firewall blocklists

---

## Project Architecture

```bash
Smart_Log_Analyzer/
│
├── main.py                  # Application entry point
├── logs/
│   └── sample.log           # Input log file
├── reports/
│   ├── error_report.txt
│   └── security_report.csv
│
└── analyzer/
    ├── __init__.py
    ├── log_parser.py        # Regex-based log parsing
    ├── error_analyzer.py    # HTTP error aggregation
    ├── security_analyzer.py # Suspicious IP detection logic
    ├── alert_manager.py     # Threshold-based alert system
    └── report_generator.py  # TXT / CSV report generation

```
##  Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Mohit-368/Smart_Log_Analyzer-Python
    cd Smart_Log_Analyzer-Python

    ```

2.  **Prerequisites:**
    This project relies on Python's standard library. No external `pip` dependencies are required.
    * Requires Python 3.x+
    * No external dependencies (Python standard library only)

3.  **Prepare Directories:**
    Ensure the `logs/` and `reports/` directories exist to avoid File I/O errors.
    ```bash
    mkdir logs reports
    ```

##  Usage

1.  Place your server log file inside the logs/ directory
2.  Rename it to sample.log (or update the path in main.py):
    ```bash
    python main.py
    ```

3.  **Run the analyzer:**
    ```text
    ⚠ ALERT: High number of errors detected!
    Total Errors: 45

    ⚠ ALERT: Suspicious IPs detected:
    - 192.168.1.15
    - 10.0.0.5

    ✅ Error report generated: reports/error_report.txt
    ✅ Security report generated: reports/security_report.csv

    --- SUMMARY ---
    Errors: Counter({404: 25, 500: 20})
    Suspicious IPs: ['192.168.1.15', '10.0.0.5']

    ```
#  Configuration

You can tune the sensitivity of the analyzer by modifying the default thresholds in the module files.

##  Security Thresholds
File: analyzer/security_analyzer.py
```bash
# Default: 5 failed attempts flags an IP
def detect_suspicious_ips(self, logs, threshold=5):
```
##  Alert Thresholds
File: analyzer/alert_manager.py
```bash
# Default: Alert if total errors > 20
def trigger_alerts(self, ..., error_threshold=20, ip_alert_threshold=0):
```

# Reports & Outputs

After execution, the tool generates two files in the `reports/` folder:

##  Security Report (`security_report.csv`)

-   **Format:** CSV
    
-   **Content:** Single-column list of suspicious IP addresses
    
-   **Use Case:** Can be fed directly into firewall blocklists
    

##  Error Report (`error_report.txt`)

-   **Format:** Plain Text
    
-   **Content:**
    
    -   Timestamp of report generation
        
    -   Count of specific error codes
        

#  Contributing

Contributions are welcome! Please follow these steps:

1.  Fork the repository
    
2.  Create a feature branch
    
    `git checkout -b feature/AmazingFeature`
    
3.  Commit your changes
    
4.  Open a Pull Request
    

#  License

Distributed under the **MIT License**.  
See `LICENSE` for more information.

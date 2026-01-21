# Smart_Log_Analyzer-Python

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)

A robust, modular Python-based tool designed to automate server log auditing. This system parses raw log files to detect error patterns, identify potential security threats (suspicious IPs), and generate actionable reports in CSV and TXT formats.

---

##  Table of Contents
- [Key Features](#-key-features)
- [Project Architecture](#-project-architecture)
- [Installation](#-installation)
- [Usage](#-usage)
- [Configuration](#-configuration)
- [Reports & Outputs](#-reports--outputs)
- [Roadmap](#-roadmap)

---

##  Key Features

* **Log Parsing Engine**: Utilizes Regex to extract IP addresses, timestamps, HTTP methods, and status codes from raw server logs.
* **Automated Error Analysis**: Aggregates and counts HTTP error codes (Status 400+) to highlight system stability issues.
* **Security Threat Detection**: Identifies suspicious IP addresses based on high frequencies of specific security events (e.g., 401, 403, 404, 429).
* **Real-time Alerting**: Triggers console alerts when error counts or suspicious IP lists exceed defined safety thresholds.
* **Multi-Format Reporting**: Automatically generates detailed summaries:
    * `error_report.txt`: Breakdown of error codes and frequencies.
    * `security_report.csv`: List of flagged malicious IPs for firewall integration.

---

##  Project Architecture

The project is structured as a modular Python package. To run successfully, ensure your directory looks like this:

```bash
log-analyzer/
│
├── main.py                  # Entry point for the application
├── logs/
│   └── sample.log           # Input log file
├── reports/                 # Output directory for generated reports
│   ├── error_report.txt
│   └── security_report.csv
│
└── analyzer/                # Core logic package
    ├── __init__.py
    ├── log_parser.py        # Regex-based log extraction
    ├── error_analyzer.py    # Status code analysis
    ├── security_analyzer.py # Suspicious IP detection logic
    ├── alert_manager.py     # Threshold-based alerting system
    └── report_generator.py  # File I/O for reports

```
##  Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Mohit-368/Smart_Log_Analyzer-Python]
    cd Smart_Log_Analyzer-Python
    ```

2.  **Prerequisites:**
    This project relies on Python's standard library. No external `pip` dependencies are required.
    * Requires Python 3.x+

3.  **Prepare Directories:**
    Ensure the `logs/` and `reports/` directories exist to avoid File I/O errors.
    ```bash
    mkdir logs reports
    ```

##  Usage

1.  **Setup:** Place your server log file inside the `logs/` directory and rename it to `sample.log` (or update the path in `main.py`).

2.  **Execution:** Run the main script:
    ```bash
    python main.py
    ```

3.  **Expected Console Output:**
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

Modify `analyzer/security_analyzer.py` to change how many failed attempts trigger a flag.

`# Default: 5 failed attempts flags an IP def detect_suspicious_ips(self, logs, threshold=5):`

##  Alert Thresholds

Modify `analyzer/alert_manager.py` to change when console alerts are triggered.

`# Default: Alert if total errors > 20 def trigger_alerts(self, ..., error_threshold=20, ip_alert_threshold=0):`

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

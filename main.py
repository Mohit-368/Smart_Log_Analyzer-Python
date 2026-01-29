from analyzer.log_parser import LogParser
from analyzer.error_analyzer import ErrorAnalyzer
from analyzer.security_analyzer import SecurityAnalyzer
from analyzer.alert_manager import AlertManager
from analyzer.report_generator import ReportGenerator


def main():
    log_file = "logs/sample.log"

    parser = LogParser(log_file)
    logs = parser.parse_logs()

    error_analyzer = ErrorAnalyzer()
    error_summary = error_analyzer.analyze_errors(logs)

    security_analyzer = SecurityAnalyzer()
    suspicious_ips = security_analyzer.detect_suspicious_ips(logs)

    alert_manager = AlertManager()
    alert_manager.trigger_alerts(error_summary, suspicious_ips)

    report_generator = ReportGenerator()
    report_generator.generate_error_report(error_summary)
    report_generator.generate_security_report(suspicious_ips)

    print("\n--- SUMMARY ---")
    print("Errors:", error_summary)
    print("Suspicious IPs:", suspicious_ips)


if __name__ == "__main__":
    main()

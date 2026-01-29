class AlertManager:
    def trigger_alerts(self, error_summary, suspicious_ips,
                       error_threshold=20, ip_alert_threshold=0):

        total_errors = sum(error_summary.values())

        if total_errors > error_threshold:
            print("⚠ ALERT: High number of errors detected!")
            print(f"Total Errors: {total_errors}")

        if len(suspicious_ips) > ip_alert_threshold:
            print("\n⚠ ALERT: Suspicious IPs detected:")
            for ip in suspicious_ips:
                print(f"- {ip}")

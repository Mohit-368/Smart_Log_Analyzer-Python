import csv
from datetime import datetime


class ReportGenerator:
    def generate_error_report(self, error_summary):
        with open("reports/error_report.txt", "w") as file:
            file.write("Error Report\n")
            file.write(f"Generated on: {datetime.now()}\n\n")

            for error_code, count in error_summary.items():
                file.write(f"HTTP {error_code}: {count}\n")

        print("✅ Error report generated: reports/error_report.txt")

    def generate_security_report(self, suspicious_ips):
        with open("reports/security_report.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Suspicious IP"])

            for ip in suspicious_ips:
                writer.writerow([ip])

        print("✅ Security report generated: reports/security_report.csv")

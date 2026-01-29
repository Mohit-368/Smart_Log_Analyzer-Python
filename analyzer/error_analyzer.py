from collections import Counter


class ErrorAnalyzer:
    def analyze_errors(self, logs):
        error_codes = [
            log["status"]
            for log in logs
            if 400 <= log["status"] < 600
        ]

        return Counter(error_codes)

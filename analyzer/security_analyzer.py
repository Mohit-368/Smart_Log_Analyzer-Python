from collections import defaultdict


class SecurityAnalyzer:
    def detect_suspicious_ips(self, logs, threshold=5):
        ip_counter = defaultdict(int)
        suspicious_ips = []

        for log in logs:
            if log["status"] in {401, 403, 404, 429}:
                ip_counter[log["ip"]] += 1

        for ip, count in ip_counter.items():
            if count >= threshold:
                suspicious_ips.append(ip)

        return suspicious_ips

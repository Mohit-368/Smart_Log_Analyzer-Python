import re


class LogParser:
    LOG_PATTERN = re.compile(
        r'(?P<ip>\d+\.\d+\.\d+\.\d+).*?\[(?P<time>.*?)\]\s+"(?P<method>GET|POST|PUT|DELETE|PATCH).*?"\s+(?P<status>\d{3})'
    )

    def __init__(self, file_path):
        self.file_path = file_path

    def parse_logs(self):
        parsed_logs = []

        try:
            with open(self.file_path, "r") as file:
                for line in file:
                    match = self.LOG_PATTERN.search(line)
                    if match:
                        parsed_logs.append({
                            "ip": match.group("ip"),
                            "timestamp": match.group("time"),
                            "method": match.group("method"),
                            "status": int(match.group("status"))
                        })
        except FileNotFoundError:
            print("❌ Log file not found.")
        
        return parsed_logs

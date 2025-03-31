import os
import requests
import argparse

class MakeDir:
    def __init__(self, output):
        self.output = output

    def mk_dir(self):
        try:
            if not os.path.exists(self.output):
                os.mkdir(self.output)
                files = ["logs.txt"]
                for f in files:
                    with open(os.path.join(self.output, f), "w"):
                        pass
        except Exception as e:
            print(f"(+) Error occurred: {e}")

class RequestSender:
    def __init__(self, hosts_file, output):
        self.hosts = self.load_hosts(hosts_file)
        self.output = output

    def load_hosts(self, hosts_file):
        try:
            with open(hosts_file, "r") as file:
                return [line.strip() for line in file if line.strip()]
        except Exception as e:
            print(f"(+) Error loading hosts file: {e}")
            return []

    def send_request(self):
        try:
            log_path = os.path.join(self.output, "logs.txt")
            with open(log_path, "a") as log_file:
                for host in self.hosts:
                    if not host.startswith("http"):
                        host = "https://" + host

                    try:
                        response = requests.get(host)
                        x_frame_options = response.headers.get("X-Frame-Options", "NOT IMPLEMENTED")
                        log_entry = f"[{response.status_code}] {host} => X-Frame-Options: {x_frame_options}\n"
                        print(log_entry.strip())
                        log_file.write(log_entry)
                    
                    except requests.RequestException as e:
                        error_msg = f"[ERROR] {host} => {e}\n"
                        print(error_msg.strip())
                        log_file.write(error_msg)
        except Exception as e:
            print(f"(+) Error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description="Testing for Clickjacking (X-Frame-Options)")
    parser.add_argument("-f", "--hosts-file", required=True, help="Path to file containing list of host URLs.")
    parser.add_argument("-o", "--output", required=True, help="Output directory for logs.")
    args = parser.parse_args()

    hosts_file = args.hosts_file
    output = args.output

    make_dirs = MakeDir(output)
    make_dirs.mk_dir()

    request_sender = RequestSender(hosts_file, output)
    request_sender.send_request()

if __name__ == "__main__":
    main()

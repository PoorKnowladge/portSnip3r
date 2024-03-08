from socket import socket, AF_INET, SOCK_STREAM, gethostbyname
from dataclasses import dataclass
from scan_ports import is_valid_target
from warna.color import Color
from time import sleep
import threading

print_lock = threading.Lock()

@dataclass
class ScanPortsVulnerable:
    ip_address: str
    vulnerabilities: list
    open_ports: list
    current_host: str = ""

    # Fungsi untuk scan port menggunakan socket
    def scan_open(self, port):
        try:
            s = socket(AF_INET, SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((self.ip_address, port))
            if result == 0:
                with print_lock:
                    self.open_ports.append(port)
            s.close()
        except ConnectionRefusedError as e:
            print(Color.FAIL + f"Error Connection: {e}" + Color.ENDC)
        except Exception as e:
            print(Color.FAIL + "Base Error: " + str(e) + Color.ENDC)

    # Fungsi untuk menjalankan thread
    def scan_open_ports(self, target, start_port, end_port, interval=1.0):
        if not is_valid_target(target):
            print(Color.FAIL + "Target tidak valid: [Errno -5] No address associated with hostname" + Color.ENDC)
            return
        
        self.current_host = target
        threads = []

        for port in range(start_port, end_port + 1):
            thread = threading.Thread(target=self.scan_open, args=(port,))
            threads.append(thread)
            thread.start()
            sleep(interval)

        for thread in threads:
            thread.join()

    # Fungsi untuk menyimpan hasil scan ke dalam file
    def report_vulnerabilities(self):
        if not is_valid_target(self.current_host):
            print("[-] Tidak ada laporan yang disimpan karena target tidak valid.")
            return  # Jangan menyimpan laporan jika target tidak valid
        
        report_path = f"reports/laporan_{self.current_host}.txt"
        with open(report_path, "w") as file:
            print(Color.OKBLUE + f"Host: {self.ip_address}" + "IP Address: {gethostbyname{self.ip_address}" + Color.ENDC)
            print(Color.OKGREEN + "Type:" + Color.ENDC)
            file.write(f"Host: {self.ip_address}\n")
            file.write("Type:\n")
            for vuln in self.vulnerabilities:
                print(Color.OKGREEN + f"- {vuln}" + Color.ENDC)
                file.write(f" - {vuln}\n")
            print(Color.OKGREEN + "Open Ports:" + Color.ENDC)
            file.write("Open Ports:\n")
            if self.open_ports:
                for port in self.open_ports:
                    print(Color.OKGREEN + f"- {port}" + Color.ENDC)
                    file.write(f" - {port}\n")
            else:
                print(Color.WARNING + "No open ports found" + Color.ENDC)
                file.write("No open ports found\n")

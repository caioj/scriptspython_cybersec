import nmap

def perform_nmap_scan(ip, port_range):
    nmap_scan = nmap.PortScanner()
    nmap_scan.scan(ip, port_range)

    for host in nmap_scan.all_hosts():
        print('Host: %s (%s)' % (host, nmap_scan[host].hostname()))
        print('State: %s' % nmap_scan[host].state())
        for proto in nmap_scan[host].all_protocols():
            print('----------')
            print('Protocol: %s' % proto)

            lport = nmap_scan[host][proto].keys()

            for port in lport:
                print('Port: %s\tState: %s' % (port, nmap_scan[host][proto][port]['state']))

if __name__ == "__main__":
    ip = input("Digite o endereço IP que deseja consultar: ")
    port_range = input("Digite o intervalo de portas (exemplo: 21-80): ")

    perform_nmap_scan(ip, port_range)

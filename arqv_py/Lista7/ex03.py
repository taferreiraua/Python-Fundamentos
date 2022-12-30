with open("IPs.txt", "w") as ips:
    ips.write('200.135.80.9\n'
              '192.168.1.1\n'
              '8.35.67.74\n'
              '257.32.4.5\n'
              '85.345.1.2\n'
              '1.2.3.4\n'
              '9.8.234.5\n'
              '192.168.0.256')

with open("IPs.txt", "r") as arq:
    ips = arq.readlines()
    for ip in ips:
        for num in ip.strip('\n').split('.'):
            if int(num) > 224:
                print(ip)

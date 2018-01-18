#coding=utf8
import sys
import ipaddress


def getCIDR(filename):
    with open(filename, 'r') as f:
        ip_list = [ip.strip() for ip in f.readlines() if ip]

    return ip_list


def transformCIDR(ip):
    return list(ipaddress.ip_network(ip, strict=False))


def transformRange(ip_range):
    startip = ip_range.split('-')[0]
    endip = ip_range.split('-')[1]
    start = int(ipaddress.ip_address(startip))
    end = int(ipaddress.ip_address(endip))

    return [str(ipaddress.ip_address(ip)) for ip in range(start, end + 1)]


def transformTailRange(ip_range):
    startip = ip_range.split('-')[0]
    suffix = ip_range.split('-')[1]

    preffix = '.'.join(startip.split('.')[:3])

    ip_range = startip + '-' + preffix + '.' + suffix

    return transformRange(ip_range)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python3 %s filename' % sys.argv[0])
        sys.exit(0)

    filename = sys.argv[1]
    ip_list = getCIDR(filename)
    result = []
    for ip in ip_list:
        tmp = []
        if '-' in ip:
            if '.' in ip.split('-')[-1]:
                tmp = transformRange(ip)
            elif '.' not in ip.split('-')[-1]:
                tmp = transformTailRange(ip)
        else:
            tmp = transformCIDR(ip)
            # CIDR to IP list 去除头尾无效地址
            tmp = tmp[1:-1]

        result.extend(tmp)

    result = list(set(result))
    sorted(result)

    with open(str(len(result)) + '_' + filename, 'w') as f:
        for ip in result:
            f.write(str(ip) + '\r\n')

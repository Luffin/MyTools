import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Usage:\n\tpython %s filename {output}' % sys.argv[0]
        sys.exit(0)

    in_name = sys.argv[1]
    if len(sys.argv) < 3:
        out_name = sys.argv[1]
    else:
        out_name = sys.argv[2]

    with open(in_name, 'r') as f:
        content = [line.strip() for line in f.readlines() if line]

    length_before = len(content)

    result = list(set(content))

    length_after = len(result)

    with open(out_name, 'w') as f:
        for line in result:
            f.write(line + '\r\n')

    print '[+] Done~'
    print '[+] The original %d, now %d' % (length_before, length_after)

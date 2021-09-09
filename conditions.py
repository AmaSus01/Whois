def conditions(result_domain, line, num):
    for i in result_domain:
        if '(DOMAIN NOT FOUND)' in i:
            print('№', num, '' + 'Domain:' + ' ' + line.rstrip().upper() + ' ' + 'not found')
            num += 1
        elif 'inetnum:' in i:
            print('№', num, 'IP:' + ' ' + line.rstrip().upper())
            num += 1
        else:
            if ':' not in i:
                pass
            else:
                if '>>>' in i or 'NOTICE' in i or '<<<' in i or '%' in i or '*' in i or 'descr:' in i or 'you agree to abide as follows' in i or 'Please' in i or 'visit' in i or 'ICANN' in i or '(c)' in i:
                    pass
                else:
                    if 'Domain Name:' in i or 'domain:' in i:
                        print('№', num, i, '\n')
                        num += 1
                    else:
                        print(i)
    print('---------------------------------------------------------------')

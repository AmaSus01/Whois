import argparse
import whois


def whois_file(file):
    with open(file, 'r') as file1:
        for line in file1:
            w = whois.whois(line[:-1])
            if line[0] == '#':
                pass
            else:
                w = whois.whois(line[:-1])
                print("""
                =============== Domain: {} ==============
                NameServer: {} \n
                Name: {} \n
                Organization: {} \n
                Register Date: {} \n
                Expiration Date: {} \n
                =========================================""".format(line[:-1], w.name_servers, w.name, w.org,
                                                                        w.creation_date, w.expiration_date))


if __name__ == '__main__':

    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--file", help="add file of domain names here")
    args = vars(ap.parse_args())

    if args['file']:
        whois_file(file=args["file"])



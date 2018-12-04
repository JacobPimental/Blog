import r2pipe
import argparse
import subprocess
import re


def get_address_of_code(r2):
    code = r2.cmdj('pfj Z @ 0x0040e0b0')
    return code[0]['string']

parser = argparse.ArgumentParser(description='Pull codes out of binaries')
parser.add_argument('filename', help='Name of file to evaluate')

args=parser.parse_args()
filename = args.filename
r2 = r2pipe.open(filename)
code = get_address_of_code(r2)
print('{0} : {1}'.format(filename, code))
out = subprocess.run('echo "{}" | wine {}'.format(code, filename), shell=True,
                     capture_output=True)
m = re.search(r'.*\.png.*', out.stdout.decode('utf-8'))
f = open('output', '+a')
f.write(m.group())
f.write('\n')
f.close()

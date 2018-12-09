import r2pipe
from decrypt_string import decrypt_string

def decrypt_string_at_location(location):
    info = r2.cmdj('pdj 1 @ ' + location)[0]
    val_offset = info['val']
    val_info = r2.cmdj('aij ' + hex(val_offset))
    if not val_info or val_info['read'] == False:
        print('Not a string, exiting...')
        exit()
    value = ' '.join(r2.cmd('pj 1 @ ' + hex(val_offset)).split())
    decrypted_string = decrypt_string(value, len(value)).strip()
    r2.cmd('CCa ' + location + ' ' + decrypted_string)

def decrypt_all_strings_in_function(func_location, current_location):
    info = r2.cmdj('pdj 1 @ ' + current_location)[0]
    val_offset = ''
    if "val" in info.keys():
        val_offset = info['val']
    else:
        print('Not valid command, exiting...')
        exit()
    func_info = r2.cmdj('pdfj')
    for line in func_info['ops']:
        if 'val' in line.keys() and line['val'] == val_offset:
            decrypt_string_at_location(hex(line['offset']))

if __name__ == '__main__':
    r2 = r2pipe.open()
    func_location = hex(r2.cmdj('pdj 1')[0]['fcn_addr'])
    location = hex(r2.cmdj('pdj 1')[0]['offset'])
    decrypt_all_strings_in_function(func_location, location)

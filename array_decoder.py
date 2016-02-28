from pprint import pprint
import re
 
debug = False
array_to_decode = raw_input("Copy and Paste the encoded array and press ENTER.\r\n")
print "\n"
int_list = [int(s) for s in re.findall('\\d+', array_to_decode)]
 
if debug:
    print array_to_decode
    print "int list:\n"
    printint_list[0]
    print("int list:\n")
    print regex.match(array_to_decode)
 
ascii_table = list(map(chr, range(128)))
delta_index = int_list[0] - 104
 
if debug:
    print delta_index
 
new_list = []
 
for i in int_list:
    new_list.append(ascii_table[i - delta_index])
 
print "\n[*] Building custom ascii table..."
print "[*] Decoding array...\n"
print ''.join(new_list)
 
print "\n"
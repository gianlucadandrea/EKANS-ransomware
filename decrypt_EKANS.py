#!/bin/bash
import re
import sys
import pefile
import struct
import binascii


data = open(sys.argv[1], 'rb').read()

pe = pefile.PE(data=data)
base = pe.OPTIONAL_HEADER.ImageBase
memdata = pe.get_memory_mapped_image()

remaining = binascii.hexlify(data)

t = []

while(len(remaining)>0):
	split = re.split("8d346e",remaining,1)
	work = split[0][-400:]
	if len(split) == 2:
		remaining = split[1]
		match = re.findall("8d05(......)0089442404c7442408(......)00.*8d(0|1)5(......)00",work)

		if (len(match) != 0):
			t.append(match)
	else:
		remaining = ""
	


for val in t:
	off1 = struct.unpack_from('<I', binascii.unhexlify(val[0][0]+"00"))[0] - base
	l = struct.unpack_from('<I', binascii.unhexlify(val[0][1]+"00"))[0]
	off2 = struct.unpack_from('<I', binascii.unhexlify(val[0][3]+"00"))[0] - base
	d1 = bytearray(memdata[off1:off1+l])
	d2 = bytearray(memdata[off2:off2+l])
	
	print('key pos: ' + hex(base + off1) + ' str pos: ' + hex(base + off2) + ' length: ' + str(l))
	output=""

	for i in range(len(d1)):
		output+=chr((d2[i] ^ (d1[i]+i*2)) & 0xFF)

	print(output+'\n')


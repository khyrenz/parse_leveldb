#!/usr/bin/python

#Parses leveldb (ldb) databases in a folder and dumps key/value pairs in pipe-delimited output to the console
#
#Uses golang ldbdump from https://github.com/golang/leveldb/tree/master/cmd/ldbdump
##Install via:
###go get github.com/golang/leveldb
###cd /root/go/src/github.com/golang/leveldb/cmd/ldbdump/ldbdump
###go build -o ldbdump main.go
#
#Written by Kathryn Hedley, Khyrenz Ltd
#khyrenz.com

import sys, os
from subprocess import Popen, PIPE

def main():
	if len(sys.argv) < 2:
		print 'Usage:', sys.argv[0], '<path to leveldb database folder>\n'
	else:
		#NOTE: This is the default install path for WSL - change if necessary so this points to your location for ldbdump
		ldbdump ='/root/go/src/github.com/golang/leveldb/cmd/ldbdump/ldbdump'
		print "Key|Value"
		
		for f in os.listdir(sys.argv[1]):
			if f.endswith(".ldb"):
				#print 'Parsing file:', os.path.join(sys.argv[1], f)
				process = Popen([ldbdump, os.path.join(sys.argv[1], f)], stdout=PIPE)
				output = process.communicate()
				#print len(output)
				try:
					for line in output[0].split('\n'):
						#print line
						if not line is None:
							#skip whitespace
							if line.strip() == "": continue
							key = line.split(": ")[0].strip(' ,\"')
							val = line.split(": ")[1].strip(' ,\"')
							print key,"|",val
				except ValueError: continue		
				
main()
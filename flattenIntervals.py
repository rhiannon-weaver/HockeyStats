#!/bin/env/python
import sys, commands

dictbysecond = {}
for i in range(3901):
	#special, homeplayer awayplayer
	dictbysecond[i] = [[], [], [] ]


season=sys.argv[1]
gcode = sys.argv[2]
url1 = "http://www.nhl.com/scores/htmlreports/"+ season + "/T"
url2 = "0"+gcode + ".HTM"
homeurl = url1 + "H"+ url2
visurl = url1 + "V" + url2
urllist = [homeurl, visurl]

for listval in urllist:
	cmd = "python getshifts.py "+ listval
	ranges = commands.getoutput(cmd).splitlines()
	for line in ranges:
		line = line.strip().split("|")
		homeaway = line[2]
		special = line[10].strip()
		player = line[4]
		shiftstart = int(line[11])
		shiftend = int(line[12])
		#print(homeaway + " " + special + " " + player + " " + str(shiftstart) + " " + str(shiftend))
		for i in range(shiftstart, shiftend):
			if special != '\xc2\xa0':
				dictbysecond[i][0] = dictbysecond[i][0] + [special]
			if(homeaway == "hometeam"):
				dictbysecond[i][1] = dictbysecond[i][1] + [player]
			else:
				dictbysecond[i][2] = dictbysecond[i][2] + [player]

for sec in sorted(dictbysecond.keys()):
	print str(sec) +":"
	print dictbysecond[sec]

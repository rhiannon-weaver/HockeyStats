#!/bin/env/python
import sys, os, commands

def GameSeconds( per, timestr):
	per = int(per)
	min, sec = map(int, timestr.split(":"))
	return str(60*((per-1)*20 + min) + sec)


fullname = sys.argv[1]
fname = fullname.split("/")
gmparts = fname[6].split(".")[0]
team = "awayteam"
if gmparts[1]=="H":
	team= "hometeam"
gnum = gmparts[4:]
headers = "|".join(x for x in ["Season", "Game", "Team", "Jersey#","Player", "Shift", "Period", "TimeOn", "TimeOff", "Duration", "Event", "GameSecondsOn","GameSecondsOff", "DurationSeconds"])
gid = "|".join(x for x in[ fname[5],gnum,team])
cmd = "python parsetable.py " + fullname + " 1"
cmdpipe = commands.getoutput(cmd).splitlines()
prevline = ""
curline = ""
curplayer = ""
curjersey = ""
inrecord = False
playerlines= []
totaldur = 0
for i in range(1,len(cmdpipe)):
	curline = cmdpipe[i]
	if (len(curline) > 0) and (inrecord==True):
		try:
			curline = curline.replace(" ","")
			linetoprint = gid + "|" + curplayer.split(" ")[0] +"|" + " ".join(x for x in curplayer.split(" ")[1:]) + "|" + curline + "|"
			x = curline.split("|")
			per = x[1]
			ts = GameSeconds(per, x[2].split("/")[0])
  			te = GameSeconds(per, x[3].split("/")[0])
			td = GameSeconds("1",x[4])
			totaldur = totaldur + int(td)
			linetoprint = linetoprint + ts + "|" + te + "|" + td
			playerlines = playerlines + [linetoprint]
		except:
			inrecord=False
			meandur = float(totaldur)/float(len(playerlines))
			if meandur < 300:
		 		for lineval in playerlines:
					print lineval
			playerlines = []
			totaldur = 0
	else:
		if curline[0:5] == "Shift":
			inrecord = True 
			curplayer = cmdpipe[i-1]
			

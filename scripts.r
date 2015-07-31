make.url = function(season, gcode, type)
{
header = "http://www.nhl.com/scores/htmlreports/"
tail = ".HTM"
gcode = paste("0",as.character(gcode), sep="")
paste(header, as.character(season), "/", type, gcode, tail, sep="")
}

makeallurl = function(vec) 
{
 season = vec[1] 
 gcode = vec[2]

  tp = c("RO", "GS", "ES", "FS", "PL", "SS", "TH", "TV", "SO")
  make.url(season, gcode, tp)

}

make.toi.url=function(rowval){
header = "http://www.nhl.com/scores/htmlreports/"
season = as.character(rowval$season)
av = c("H", "V")
tail = ".HTM"
gcode = paste("0",as.character(rowval$gcode), sep="")
paste(header, season, "/T", av, gcode, tail, sep="") 
}


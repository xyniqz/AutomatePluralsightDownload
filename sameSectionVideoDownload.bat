REM @author: SRvSaha
REM Date: 29-12-2018
REM Version: 1.0.0
REM Desc: This is created since many times, there will be a bunch of couses which will have same Certification Name/Path Name
REM and which belongs to the same section. So, in that case it is handy to pass just one parameter, the
REM parameter consists of the filename which has all the links and the filenames

REM Set input argument to arg1
set arg1=%1
REM Calling the python script for autodownload of the videos from the file with filename passed in arg1
python C:\Users\srvsaha\Downloads\download.py %arg1% "Cisco CCNA Routing and Switching" "Cisco CCENT  ICND1 100-105"
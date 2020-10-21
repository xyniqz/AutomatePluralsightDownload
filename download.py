# @author: SRvSaha
# Date: 28-12-2018
# Version: 1.0.0
# Desc: Script which take the links of videos as input and does a batch download of them using command
# line IDM. 

# There are certain hardcoding of filepath, which should ideally be read from file or passed as param.
# Please fix that. There are certain things in the code which are not recommened practice to write, but
# this module is written just to make things work as of now.

# As of now 3 parameters are to be passed for running the program.
# argument 1 : File (.json) which contains the mapping of video name, module name and the link
# argument 2: The Certificate Name/Path Name where the course belong
# argument 3: The Section Name/Sub Track name or kind of parent node of all the child video nodes
# NOTE: This script is written to make use of IDM as downloading tool/manager to download batchwise. IDM
# has the feature of batch download but the issue there is that it takes the name of the videos very generic
# like videoplayback or 1280x720 and hence this is used to give name of the video for download. Also to
# keep them in a similar directory structure as they are structred in PluralSight website

# TODO: Reads argumnents by making use of argparse which will make it a proper CMD line app
import sys
import subprocess
import shlex
import re
# ---------------------------------------------------------------------------------------------
# INITIALIZATIONS
# ---------------------------------------------------------------------------------------------
# Remove this harcoded path.
# The base directory 
DOWNLOAD_PATH = r"E:\PersonalProjects\AutomatePluralsight\Videos"
# Make sure this path is same for IDM
# Path where IDM is installed
IDM_PATH = r"C:\Program Files (x86)\Internet Download Manager\IDMan.exe"
# This is the name of the json file passed in argument 1 as it is saved as courseTitle.json
COURSE_NAME = ""
# The name of the module of the video
MODULE_NAME = ""
# The certification/path name
CERTIFICATION_NAME = '\\'+sys.argv[2].strip()
# The section/sub-track name which has many videos
SECTION_NAME = '\\'+sys.argv[3].strip()
# Name of the video which is to be downloaded
VIDEO_NAME = ""
# URL of the video which is to be downloaded
DOWNLOAD_URL = ""
# This contains the list of all params to be passed to cmd for IDM
BATCH_COMMAND = []
# If absolute path is given for the file, we take only the filename part and remove json as well
index_of_slash = sys.argv[1].rfind('\\')
index_of_dotjson = sys.argv[1].rfind('.json')
index_of_invertedcomma = ""
# ---------------------------------------------------------------------------------------------------

if  index_of_slash != -1:
    COURSE_NAME = sys.argv[1][index_of_slash:index_of_dotjson]
else:
    COURSE_NAME = '\\' +sys.argv[1][:index_of_dotjson]

DOWNLOAD_PATH += CERTIFICATION_NAME+SECTION_NAME+COURSE_NAME
DOWNLOAD_PATH = DOWNLOAD_PATH.strip()

splitted_line = []

# Fully qualified path where idman.exe exists
BATCH_COMMAND.append(IDM_PATH)
# The url which is to be used for downloading
BATCH_COMMAND.append('/d')
BATCH_COMMAND.append(DOWNLOAD_URL)
# The path where the video is to be saved
BATCH_COMMAND.append('/p')
BATCH_COMMAND.append(DOWNLOAD_PATH)
# The filename of the video by which it is to be saved
BATCH_COMMAND.append('/f')
BATCH_COMMAND.append(VIDEO_NAME)
# This is added so that IDM will work silently and will not pop out with something unless any issue occurs
BATCH_COMMAND.append('/n')

with open(sys.argv[1]) as f:
    for line in f.readlines()[1:-1]:
        # \\t instead of \t cause \ is used as escape character
        splitted_line = line.strip().split("\\t")
        # The module name for the video
        MODULE_NAME = splitted_line[1]
        # Change it later on when directory structure is automated
        VIDEO_NAME = MODULE_NAME+'_'+splitted_line[2]+'+.mp4'
        # Removing all the special characters with blank else filename can't be created
        VIDEO_NAME = re.sub('[^ a-zA-Z0-9_.]', '', VIDEO_NAME)
        print(VIDEO_NAME)
        # To remove the trailing " from each URLs
        index_of_invertedcomma = splitted_line[3].rfind("\"")
        DOWNLOAD_URL = splitted_line[3][:index_of_invertedcomma]
        # These two params are always changed based on video
        BATCH_COMMAND[2] = DOWNLOAD_URL
        BATCH_COMMAND[6] = VIDEO_NAME
        # Call the IDM cmd using subprocess which returns 0 if successful else error code
        if(subprocess.call(BATCH_COMMAND) != 0):
            print("Some error occured in subprocess!")
            sys.exit()
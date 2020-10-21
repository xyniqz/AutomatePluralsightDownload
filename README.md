# Automate Pluralsight Download
### Automate the Download of Pluralsight Videos for future reference. 

The Project is created to automate the process of Downloading of Pluralsight Clips which are a part if the course using IDM in Windows.
Also, another use case was after the files are downloaded, in case those get deleted, then there should be some way to recover it.
For the recovery part, we are making using of Recuva and doing some post processing so that we can get all the files back with proper renaming and moving in proper folders
as it were when downloaded.

Inline comments are done in the source code, which helps in understanding the whys!

Basically, the necessity of the process came when user has active Pluralsight Subscription and wants to download the clips in the course without using the Pluralsight Downloader 
so that the downloaded files doesn't get removed after the subscription in mind.

* To Download:

Flow of the Process:

- Step 1. Use the core.js to grab all the links for the clips in the course
- Step 2. Use download.py for pre-processing of the links grabbed from Step 1 to be used by IDM for downloading
- Step 3. Run the sameSectionVideoDownlod.bat script for triggering of IDM for the links which were found in Step 2 after post-processing

* To Recover Files:

Flow of the Process:

- Step 1. Use Recuva and scan for all deleted files/folder. In case the memory is not overwritten, files will get recovered. Recuva give a text file of all the possible recovery.
- Step 2. Recover the files using Recuva
- Step 3. Preprocess the txt file of Recuva using GenerateMappingRecuva.py file
- Step 4. Post process the files using the PluralsightFilesRecover.py for proper renaming, arranging and moving to folder.

Bingo! You should now have to files downloaded. Please modify the path of Downloads and other constants in the Source Code before using.

*Please NOTE*: This repository is in no means trying to hack Pluralsight nor is there any intention to misuse it. Use it as your own discretion as your account may get banned if
unusual hits are observed from an account.

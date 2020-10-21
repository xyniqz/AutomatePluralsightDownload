# Automate Pluralsight Download
### Automate the Download of Pluralsight Videos for future reference. 

#### This Project is created to automate the process of Downloading of Pluralsight Clips which are a part if the course using IDM in Windows.

### Inline comments are done in the source code, which helps in understanding the whys!

Basically, the necessity of the process came when user has active Pluralsight Subscription and wants to download the clips in the course without using the Pluralsight Downloader 
so that the downloaded files doesn't get removed after the subscription in mind.

Flow of the Process:

Step 1. Use the core.js to grab all the links for the clips in the course
Step 2. Use download.py for pre-processing of the links grabbed from Step 1 to be used by IDM for downloading
Step 3. Run the sameSectionVideoDownlod.bat script for triggering of IDM for the links which were found in Step 2 after post-processing

Bingo! You should now have to files downloaded. Please modify the path of Downloads and other constants in the Source Code before using.

Please NOTE: This repository is in no means trying to hack Pluralsight nor is there any intention to misuse it. Use it as your own discretion as your account may get banned if
unusual hits are observed from an account.

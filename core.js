// @author: SRvSaha
// Date: 27-12-2018
// Desc: Used to grab all the URLs of video, name of video, name of module of the video
// and course title, save them in a json file. This file is then parsed to autodownload
// NOTE: Each Video has expiry time of 1 hour only.

// How to run: You have to run the code section-wise. Section is mentioned in the code below.
// Go to pluralsight.com and the open any course. Play the first video of the course and then pause
// it. After that run the code section wise. Just copy the portion of a section and paste it 
// in the Console (Ctrl+Shift+I) in Chrome.

// First, copy the code of section 1 and paste. Then do same for other sections. NOTE: Don't copy paste 
// the whole code in one go

// SECTION 1
// Creating a script tag and adding the jquery in it
var jq = document.createElement('script');
jq.src = "https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js";
document.getElementsByTagName('head')[0].appendChild(jq);

// SECTION 2
// This is to make sure that our library of jQuery doesn't conflict with the existing ones
jQuery.noConflict();

// init
var counter = 1
var courseTitle = jQuery("h1")["context"]["title"]
var lastVideoName = "";
var lastModule = jQuery("h2").last().text().trim();
var lastVidToDl = false;
var nextVid = "";
var nextTitle = "";
var nextModule = "";
var videoURL = "";
var titlesArray = [];
var waitDuration = 10000; //10 seconds by default

// SECTION 3
// Utility for saving the console output to a file
(function(console){

    console.save = function(data, filename){
    
    if(!data) {
    console.error('Console.save: No data')
    return;
    }
    
    if(!filename) filename = 'console.json'
    
    if(typeof data === "object"){
    data = JSON.stringify(data, undefined, 4)
    }
    
    var blob = new Blob([data], {type: 'text/json'}),
    e = document.createEvent('MouseEvents'),
    a = document.createElement('a')
    
    a.download = filename
    a.href = window.URL.createObjectURL(blob)
    a.dataset.downloadurl = ['text/json', a.download, a.href].join(':')
    e.initMouseEvent('click', true, false, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null)
    a.dispatchEvent(e)
    }
    })(console);
    
// Core Logic

function dlVid()
{
    // Url of the video which is required for downloading
    videoURL = jQuery("video").attr("src");
    // Title/Name of the video by which it will be saved
    var currTitle = jQuery("ul.clips > li.selected").find("h3").text().trim();
    // Current Module Name
    var currMod = jQuery("ul.clips > li.selected").parent().parent().find("h2").text().trim();

    console.log(counter + " " + currMod + " " + currTitle + " " + videoURL);
    titlesArray.push(counter + "\t" + currMod + "\t" + currTitle + "\t" + videoURL);
    counter = counter + 1;

    jQuery("#next-control").click();

    setTimeout(function(){jQuery("#play-control").click();}, 10000);

    if(!lastVidToDl)
    {
        // Callback dlVid after waitDuration sec (by default 10 sec)
        setTimeout(dlVid, waitDuration);
        // Select the next video to be played
        nextVid = jQuery("ul.clips > li.selected").next();
        // Getting the title of the next video
        nextTitle = nextVid.find("h3").text().trim();
        // Fetching the name of the next module
        nextModule = nextVid.parent().parent().find("h2").text().trim();

        // This is a workaround to stop the function callback.
        // When we are at the last module, we check what is the last video in that module
        // This will break the recursion when lastVideo of the module is reached
        if(nextModule == lastModule)
        {
            lastVideoName = jQuery("li").last().find("h3").text().trim();
            if(nextTitle == lastVideoName)
            {
                // This will break the recursive call
                lastVidToDl = true;
            }
        }
        
    }
    else
    {
        // Saving the console logs at the end in a json file with coursename
        console.save(titlesArray, courseTitle+".json");
    }
}

// Section 4

waitDuration = 5000; // Change this param according to need. It is in ms. NOTE: Keep this high otherwise
// Pluralsight will block your account if they find high activity from your account. Ideally, 10000 or more is recommended
dlVid(); // Calling the core Function
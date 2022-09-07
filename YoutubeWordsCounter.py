import os
import sys
from youtube_transcript_api import YouTubeTranscriptApi

counter = 0
myWord = input("Nach welchem Wort soll gesucht werden?")
try:
    url = input("Wie lautet der Link zu dem YouTube Video?").split("=")[1].split("&")[0]
    transcript = YouTubeTranscriptApi.get_transcript(url, languages=['de'])
except:
    print("Either the link you entered is invalid or the video does not have a transcript.")
    sys.exit()


# remove older scripts
os.remove("./.script.txt")

# write script into text file
for transcripts in transcript:
    text = transcripts['text']
    try:
        f = open(".script.txt", "a")
    except OSError:
        print("Could not open/read file")
        sys.exit()
    with f:
        f.write(text + "\n")
        f.close()

#
try:
    file = open(".script.txt", "r")

except OSError:
    print("Could not open/read file")
    sys.exit()

with file:
    data = file.read()
    dataIntoList = data.replace('\n', '').split(".")
    for line in dataIntoList:
        for word in line.split():
            if word == myWord:
                counter += 1
    file.close()
    print(f"Das Wort '{myWord}' wurde in dem Video {counter} mal gesagt.")

# time complexity: O(n^2)
# script by Julian Kropp

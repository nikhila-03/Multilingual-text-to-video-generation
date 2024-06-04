import requests
import openpyxl
from bs4 import BeautifulSoup
import os
from mutagen.mp3 import MP3
from summary import *
from tokens import *
from image_gen import *
from text_to_speech import *
from imageSequenceClip import *
from bg_removed import *
from border_adding import *
url="https://pib.gov.in/Allrel.aspx"
r=requests.get(url)
htmlcontent=r.content
soup=BeautifulSoup(htmlcontent,'html.parser')

mainPart=soup.find('div',class_="content-area")
listItems=[]

for Listitems in mainPart.find_all('a'):
    fghn=Listitems.get('href')
    listItems.append(fghn)

counter=0;
finallist_names=[]
finallist_text=[]
while(counter<len(listItems)):
    #len(listitems
    innerUrl="https://pib.gov.in"+listItems[counter]
    innerR = requests.get(innerUrl)
    innerHtmlcontent = innerR.content
    innerSoup = BeautifulSoup(innerHtmlcontent, 'html.parser')

    ministryName=innerSoup.find('div',class_="MinistryNameSubhead text-center")
    ministryName_text=ministryName.get_text()
    actualMinistryName=''
    for i in ministryName_text:
        if(i!=' '):
            actualMinistryName=actualMinistryName+i


    contentName=innerSoup.find('h2')
    contentName_text=contentName.get_text()
    actualContentName=''
    for i in contentName_text:
        if(i!=' '):
            actualContentName=actualContentName+i

    fileName=actualMinistryName+"."+actualContentName

    content_text=''
    for content in innerSoup.find_all('p'):
        content_text=content_text+content.get_text()

    finaltext=''
    for j in content_text:
        if(j!='*'):
            finaltext=finaltext+j
        else:
            break

    if fileName not in finallist_names:
        name = ''.join(fileName.split('\n'))
        name = ''.join(name.split('\r'))
        name = ''.join(name.split(' '))
        name = ''.join(letter for letter in name if letter.isalnum())
        print(name)
        summarized_text = summary_func(finaltext)            ###summarizing the total press release
        print(summarized_text)
        final_tokens = tokens_generated(summarized_text)     ###generating tokens(important words)
        print(final_tokens)
        images(final_tokens, name)                           ###collecting images for the generated tokens
        final_audio = text_to_speech(summarized_text, name)
        # temp_audio = MP3(final_audio)                        ###generating speech from summarized text
        # audio_len = temp_audio.info.length
        # print(audio_len)
        loc = os.path.join(r"C:\Users\lenovo\PycharmProjects\SIH1\images", name)
        add_border(loc)
        BG_adder(loc)                                        ###adding background to the generated images
        imageSequence(loc, 3, name)                          ###sequencing all images to form like a slideshow
    finallist_names.append(fileName)
    finallist_text.append(finaltext)
    counter=counter+1


# import subprocess
#
# # List of commands to execute
# commands = [
#     'cd /path/to/PycharmProjects',
#     'cd opencv1',
#     'cd Wav2Lip',
#     'python inference.py --checkpoint_path checkpoints/wav2lip_gan.pth --face media/input_vedio.mp4 --audio media/input_audio.wav --outfile output.mp4'
# ]
#
# # Iterate through the commands and execute each one
# for cmd in commands:
#     try:
#         subprocess.run(
#             cmd,
#             shell=True,  # Use shell for running the command
#             check=True,  # Raise an error if the command fails
#             text=True  # Ensure the output is in text (str) format
#         )
#     except subprocess.CalledProcessError as e:
#         print(f"Command failed with an error: {e}")
#
#

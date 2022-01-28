#!/usr/bin/python

import sys
import os
import re
import beautifulsoup4
import scrapy
import requests
from bs4 import BeautifulSoup  #doesn't make sense, shows up as beautifulsoup4 in package list #import beautifulsoup4

print "Loading Configuration"

#webaddress
#teamid
#season
#rules for traversing the site
#rules for scrapping data

#INITIALIZE GLOBALS FROM CONFIGURATION.CONF
#cardset = webaddress:longname:shortname:season:conference:record:rank:divison:sanctions
try:
   confile = open("conf/dataset.conf", "r")
except IOError:
   print "Couldn't load config file"
   sys.exit()

  for line in confile
     cardset = dict(line.split('=')  #test this and make sure the scope is correct in pyton
     #www.sports-reference.com/cfb/schools/georgia/2017.html

stat_categories = {"passing","rushing_receiving","defense_and_fumbles","returns","kickcing_and_punting","scoring"}

print "Retrieving page from" #add address
page = requests.get(URL)  #REQUEST HEADER SHOULD INDICATE THE ARIA BROWSER
soup = BeautifulSoup(page.content, "html.parser")

print "Extracting datasets:"  #line return, then return each name as done
#SIMPLIFY THIS: WHILE CATEGORIES  - create a global array of categories of things and interpolate into names and object.finds

raw_passing_headers = div_passing#  it's in THEAD SECOND ROW, PULL THE ARIA LABEL
div_passing = soup.find(id=div_passing)# IT'S IN TBODY, PARSE THAT ROW BY ROW USING A WHILE ON THE HEADERS TO DO KEY-VALUE PARING

div_rushing_receiving = soup.find(id=div_rushing_and_receiving)
div_defense_fumbles = soup.find(id=div_defense_and_fumbles)
div_kick_puntreturns = soup.find(id=div_returns)
div_kicking_punting = soup.find(id=div_kicking_and_punting)
div_scoring = soup.find(id=div_scoring)




#print for each data set processing, then player as abstracted
div_passing_headers = do_somthing#TO RAW_PASSING_HEADERS
#FOR EACH.....

#  div_passing -> 2nd:<TR> --> forEach <TH> - grab value of aria-label  (might not be aria, must set it to look like aria with headers on request)
#OR JUST PULL "data-stat" field

#list of item names........
# PLAYER --> SHOVE ON ARRAY[player_NAME] Z> {STAT:value,STAT:value.......}
#AND THUS JUST BUILD A BIG HASH WITH A SINGLE row and value per item for each player_NAME
#master list of item names will overwrite creating a list of unique field names for post proecssing reconstruction of master array
#process the webdata and save CSV
     #Load your basic player information
     #parse it into a multi-value list
     #Spit it out to a file


#Associate data via player nam
#Spit it out to a file also


















print "Initializing Data Arrays"

# go lets you build structs, lets go ahead and create something like it.
# Structs
      # Basic Card


      # Defense Stats


      # Offensive Stats



# do your scrapping regex stuff etc



print "Scrapping Data."

record++




print "Record [[interpolate number]]."
#  athlete, def/of/sp, etc.   just basic info for each record done and return nuber parsed, etc.






print "Posting data to output file"




#STEP 1:  JUST SCRAPE AND LOAD BASIC DATA FOR EACH TEAMS PLAYERS ALONG WITH A SINGLE GRAPHIC
#STEP 2:  ADD MINTING OF BASIC CARDS AND TYING IT TO A BASIC GRAPHIC
#STEP 3:  SCRAPE, CHECKSUM AND STORE THE DATA OBJECT
#STEP 4:  GET THE REST OF THE TEAM ON BUILDING THE FRRONTENDS  (PUT ALL PROJECTS ON JIRA WITH TIMELINES)
#STEP 5:  CREATE FIVE SETS OF DEMO CARDS FOR EACH SCHOOL ON LOCAL NETWORK
#STEP 5.5:  CHECKSUM AND SIGN THE GRAPHICS
#STEP 6:  ENHANCE THE CARDS, MAKE THEM LOOK GOOD FOR DEMO, LOAD THEM ON A REAL TESTNET


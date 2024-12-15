import requests
from bs4 import BeautifulSoup

def queryO2CM(FirstName, LastName):
        
    response = requests.post(
        "https://results.o2cm.com/individual.asp",
        data = {
            "szFirst" : FirstName,
            "szLast"  : LastName,
            "Search"  : "Search"
            },
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.70 Safari/537.36"
        }
    )

    dancerData = BeautifulSoup(response.text, 'html.parser').find_all("td")
    del dancerData[0]
    del dancerData[-2:]

    return dancerData


def getDancerCompetitionList(FirstName, LastName):

    dancerData = queryO2CM(FirstName, LastName)
    
    competitions = {}
    currentCompetition = ""
    eventList = []

    for line in dancerData:
        text = line.get_text()
        
        eventLink = line.find(href=True)
        isCompetition = (eventLink == None)

        if isCompetition:
            if len(eventList) != 0:
                competitions[currentCompetition] = eventList
                eventList = []
            currentCompetition = text
        else:
            #event names have a variable amount "\xa0" characters in front of them for some reason, deleting that here
            eventList.append((text.replace(u'\xa0', u'') , eventLink['href']))

    return competitions

# yuvalData = getDancerCompetitionList("Yuval" , "Ailon")
# leaData = getDancerCompetitionList("Lea" , "Luchterhand")
# benjaminData = getDancerCompetitionList("Benjamin" , "Tadmor")

# print(leaData == yuvalData)                                         # True:  Yuval and Lea have only ever competed together
# print(leaData == benjaminData)                                      # False: Lea and Benjamin have competed in different competitions
# print('10-13-24 - Harvard Beginners 2024' in yuvalData.keys())      # True: Yuval has competed in Harvard Beginners 2024
# print('10-13-24 - Harvard Beginners 2024' in benjaminData.keys())   # False: Benjamin did not compete in Harvard Beginners 2024


#Output of getDancerCompetitionList("Yuval" , "Ailon") 
{'10-13-24 - Harvard Beginners 2024': 
 [('7) Amateur Collegiate Newcomer Am. Foxtrot', 'http://Results.o2cm.com/scoresheet3.asp?event=hbi24&heatid=4032203A'), 
  ('13) Amateur Collegiate Newcomer Intl. Waltz', 'http://Results.o2cm.com/scoresheet3.asp?event=hbi24&heatid=40322018'), 
  ('16) Amateur Collegiate Newcomer Am. Swing', 'http://Results.o2cm.com/scoresheet3.asp?event=hbi24&heatid=4032204A'), 
  ('14) Amateur Collegiate Newcomer Intl. Rumba', 'http://Results.o2cm.com/scoresheet3.asp?event=hbi24&heatid=4032202A')], 
'11-23-24 - Tufts University Ballroom Competition': 
 [('19) Amateur Collegiate Newcomer Am. Rumba', 'http://Results.o2cm.com/scoresheet3.asp?event=tub24&heatid=40322049'), 
  ('15) Amateur Collegiate Newcomer Intl. Jive', 'http://Results.o2cm.com/scoresheet3.asp?event=tub24&heatid=4032202C'), 
  ('33) Amateur Collegiate Newcomer Intl. Cha Cha', 'http://Results.o2cm.com/scoresheet3.asp?event=tub24&heatid=40322028'), 
  ('18) Amateur Collegiate Newcomer Intl. Tango', 'http://Results.o2cm.com/scoresheet3.asp?event=tub24&heatid=40322019'), 
  ('22) Amateur Collegiate Newcomer Am. Waltz', 'http://Results.o2cm.com/scoresheet3.asp?event=tub24&heatid=40322038'), 
  ('21) Amateur Collegiate Newcomer Am. Swing', 'http://Results.o2cm.com/scoresheet3.asp?event=tub24&heatid=4032204A'), 
  ('15) Amateur Collegiate Newcomer Am. Foxtrot', 'http://Results.o2cm.com/scoresheet3.asp?event=tub24&heatid=4032203A'), 
  ('13) Amateur Collegiate Newcomer Am. Tango', 'http://Results.o2cm.com/scoresheet3.asp?event=tub24&heatid=40322039'), 
  ('8) Amateur Collegiate Newcomer Intl. Quickstep', 'http://Results.o2cm.com/scoresheet3.asp?event=tub24&heatid=4032201C'), 
  ('10) Amateur Collegiate Newcomer Intl. Waltz', 'http://Results.o2cm.com/scoresheet3.asp?event=tub24&heatid=40322018'), 
  ('16) Amateur Collegiate Newcomer Am. Cha Cha', 'http://Results.o2cm.com/scoresheet3.asp?event=tub24&heatid=40322048'), 
  ('10) Amateur Collegiate Newcomer Intl. Rumba', 'http://Results.o2cm.com/scoresheet3.asp?event=tub24&heatid=4032202A')],
'12-08-24 - Terrier Dancesport Competition': 
 [('15) Amateur Collegiate Newcomer Am. Swing', 'http://Results.o2cm.com/scoresheet3.asp?event=bub24&heatid=4032204A'), 
  ('7) Amateur Collegiate Newcomer Am. Rumba', 'http://Results.o2cm.com/scoresheet3.asp?event=bub24&heatid=40322049'), 
  ('7) Amateur Collegiate Newcomer Intl. Cha Cha', 'http://Results.o2cm.com/scoresheet3.asp?event=bub24&heatid=40322028'), 
  ('8) Amateur Collegiate Newcomer Intl. Rumba', 'http://Results.o2cm.com/scoresheet3.asp?event=bub24&heatid=4032202A'), 
  ('7) Amateur Collegiate Newcomer Am. Foxtrot', 'http://Results.o2cm.com/scoresheet3.asp?event=bub24&heatid=4032203A'), 
  ('8) Amateur Collegiate Newcomer Am. Waltz', 'http://Results.o2cm.com/scoresheet3.asp?event=bub24&heatid=40322038'), 
  ('6) Amateur Collegiate Newcomer Intl. Waltz', 'http://Results.o2cm.com/scoresheet3.asp?event=bub24&heatid=40322018'), 
  ('6) Amateur Collegiate Newcomer Intl. Tango', 'http://Results.o2cm.com/scoresheet3.asp?event=bub24&heatid=40322019')]}
import requests
from bs4 import BeautifulSoup
import csv
date = input('please enter the date in MM/DD/YY: ')
page = requests.get(f"https://www.yallakora.com/match-center/%D9%85%D8%B1%D9%83%D8%B2-%D8%A7%D9%84%D9%85%D8%A8%D8%A7%D8%B1%D9%8A%D8%A7%D8%AA?date={date}#")

def main(page):
    src = page.content
    soup = BeautifulSoup(src,"lxml")
    matches_list=[]

    championships = soup.find_all("div",{'class':'matchCard'})
    
    def get_match_info(championships):
        championship_title = championships.contents[1].find('h2').text.strip()
        all_matches=championships.contents[3].find_all("div",{'class':'item finish liItem'})
        number_of_matches=len(all_matches)
        for i in range (number_of_matches):
            team_a = all_matches[i].find("div",{'class':'teams teamA'}).text.strip()
            team_b = all_matches[i].find("div",{'class':'teams teamB'}).text.strip()
            sc = all_matches[i].find("div",{'class':'MResult'}).find_all('span',{'class':'score'})
            sco=f'{sc[0].text.strip()} - {sc[1].text.strip()}'
            time = all_matches[i].find("div",{'class':'MResult'}).find('span',{'class':'time'}).text.strip()
            matches_list.append({'نوع البطوله':championship_title,'الفريق اﻻول':team_a,'الفريق الثانى':team_b,'ميعاد المباراه':time,'النتيجه':sco})
                

    for i in range (len(championships)):
        get_match_info(championships[i])

    keys = matches_list[0].keys()
    with open('test.csv',mode='w',newline='') as output_file:
        d_w = csv.DictWriter(output_file,keys)
        d_w.writeheader
        d_w.writerows(matches_list)



main(page)

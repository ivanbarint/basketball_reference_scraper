#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import requests
from bs4 import BeautifulSoup
from string import digits

def ShowStats(season):
    url = f"https://www.basketball-reference.com/leagues/NBA_{season}.html"
    response = requests.get(url)
    text = response.text
    soup = BeautifulSoup(text, features='lxml')
    
    teams_messed = []
    teams, wins, losses, perc, gb, scored, against, srs = ([], [], [], [], [], [], [], [])

    unfiltered_teams = soup.find_all("th", {"data-stat":"team_name"})

    for i in range(0, len(unfiltered_teams)):
            teams_messed.append(unfiltered_teams[i].get_text(strip=True))

    for team in teams_messed:
        if "Conference" in team:
            del team
        else:
            team = ''.join([i for i in team if not i.isdigit()])
            teams.append(team)

    unfiltered_wins = soup.find_all("td", {"data-stat":"wins"})
    unfiltered_losses = soup.find_all("td", {"data-stat":"losses"})
    unfiltered_perc = soup.find_all("td", {"data-stat":"win_loss_pct"})
    unfiltered_gb = soup.find_all("td", {"data-stat":"gb"})
    unfiltered_scored = soup.find_all("td", {"data-stat":"pts_per_g"})
    unfiltered_against = soup.find_all("td", {"data-stat":"opp_pts_per_g"})
    unfiltered_srs = soup.find_all("td", {"data-stat":"srs"})

    for i in range(0, len(teams)):
        wins.append(unfiltered_wins[i].get_text(strip=True))
        losses.append(unfiltered_losses[i].get_text(strip=True))
        perc.append(unfiltered_perc[i].get_text(strip=True))
        gb.append(unfiltered_gb[i].get_text(strip=True))
        scored.append(unfiltered_scored[i].get_text(strip=True))
        against.append(unfiltered_against[i].get_text(strip=True))
        srs.append(unfiltered_srs[i].get_text(strip=True))
        
    df = pd.DataFrame(list(zip(teams, wins, losses, perc, gb, scored, against, srs)), columns = ['Team', 'W', 'L', 'W/L%', 'GB', 'PS/G', 'PA/G', 'SRS'])
    
    df = df.drop_duplicates(subset=['Team'], keep='first')
    
    df['Team'] = df['Team'].str.replace("*", "", regex=True)
    df['Team'] = df['Team'].str.replace("(", "", regex=True)
    df['Team'] = df['Team'].str.replace(")", "", regex=True)
    df['Team'] = df['Team'].str.replace("Philadelphia ers", "Philadelphia 76ers", regex=True)
    
    return df
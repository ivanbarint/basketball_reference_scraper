#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import requests
from bs4 import BeautifulSoup

def ShowStats(season):
    url = f"https://www.basketball-reference.com/leagues/NBA_{season}_shooting.html"
    response = requests.get(url)
    text = response.text
    soup = BeautifulSoup(text, features='lxml')

    players, pos, age, team_id, g, mp, fg_pct, avg_dist, pct_fga_fg2a, pct_fga_00_03, pct_fga_03_10, pct_fga_10_16, pct_fga_16_xx, pct_fga_fg3a, fg_pct_fg2a, fg_pct_00_03, fg_pct_03_10, fg_pct_10_16, fg_pct_16_xx, fg_pct_fg3a, pct_ast_fg2, pct_ast_fg3, pct_fga_dunk, fg_dunk, pct_fg3a_corner3, fg_pct_corner3, fg3a_heave, fg3_heave = ([], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [])

    unfiltered_players = soup.find_all("td", {"data-stat":"player"})
    unfiltered_pos = soup.find_all("td", {"data-stat":"pos"})
    unfiltered_age = soup.find_all("td", {"data-stat":"age"})
    unfiltered_team_id = soup.find_all("td", {"data-stat":"team_id"})
    unfiltered_g = soup.find_all("td", {"data-stat":"g"})
    unfiltered_mp = soup.find_all("td", {"data-stat":"mp"})
    unfiltered_fg_pct = soup.find_all("td", {"data-stat":"fg_pct"})
    unfiltered_avg_dist = soup.find_all("td", {"data-stat":"avg_dist"})
    unfiltered_pct_fga_fg2a = soup.find_all("td", {"data-stat":"pct_fga_fg2a"})
    unfiltered_pct_fga_00_03 = soup.find_all("td", {"data-stat":"pct_fga_00_03"})
    unfiltered_pct_fga_03_10 = soup.find_all("td", {"data-stat":"pct_fga_03_10"})
    unfiltered_pct_fga_10_16 = soup.find_all("td", {"data-stat":"pct_fga_10_16"})
    unfiltered_pct_fga_16_xx = soup.find_all("td", {"data-stat":"pct_fga_16_xx"})
    unfiltered_pct_fga_fg3a = soup.find_all("td", {"data-stat":"pct_fga_fg3a"})
    unfiltered_fg_pct_fg2a = soup.find_all("td", {"data-stat":"fg_pct_fg2a"})
    unfiltered_fg_pct_00_03 = soup.find_all("td", {"data-stat":"fg_pct_00_03"})
    unfiltered_fg_pct_03_10 = soup.find_all("td", {"data-stat":"fg_pct_03_10"})
    unfiltered_fg_pct_10_16 = soup.find_all("td", {"data-stat":"fg_pct_10_16"})
    unfiltered_fg_pct_16_xx = soup.find_all("td", {"data-stat":"fg_pct_16_xx"})
    unfiltered_fg_pct_fg3a = soup.find_all("td", {"data-stat":"fg_pct_fg3a"})
    unfiltered_pct_ast_fg2 = soup.find_all("td", {"data-stat":"pct_ast_fg2"})
    unfiltered_pct_ast_fg3 = soup.find_all("td", {"data-stat":"pct_ast_fg3"})
    unfiltered_pct_fga_dunk = soup.find_all("td", {"data-stat":"pct_fga_dunk"})
    unfiltered_fg_dunk = soup.find_all("td", {"data-stat":"fg_dunk"})
    unfiltered_pct_fg3a_corner3 = soup.find_all("td", {"data-stat":"pct_fg3a_corner3"})
    unfiltered_fg_pct_corner3 = soup.find_all("td", {"data-stat":"fg_pct_corner3"})
    unfiltered_fg3a_heave = soup.find_all("td", {"data-stat":"fg3a_heave"})
    unfiltered_fg3_heave = soup.find_all("td", {"data-stat":"fg3_heave"}) 

    for i in range(0, len(unfiltered_players)):

        players.append(unfiltered_players[i].get_text(strip=True))
        pos.append(unfiltered_pos[i].get_text(strip=True))
        age.append(unfiltered_age[i].get_text(strip=True))
        team_id.append(unfiltered_team_id[i].get_text(strip=True))
        g.append(unfiltered_g[i].get_text(strip=True))
        mp.append(unfiltered_mp[i].get_text(strip=True))
        fg_pct.append(unfiltered_fg_pct[i].get_text(strip=True))
        avg_dist.append(unfiltered_avg_dist[i].get_text(strip=True))
        pct_fga_fg2a.append(unfiltered_pct_fga_fg2a[i].get_text(strip=True))
        pct_fga_00_03.append(unfiltered_pct_fga_00_03[i].get_text(strip=True))
        pct_fga_03_10.append(unfiltered_pct_fga_03_10[i].get_text(strip=True))
        pct_fga_10_16.append(unfiltered_pct_fga_10_16[i].get_text(strip=True))
        pct_fga_16_xx.append(unfiltered_pct_fga_16_xx[i].get_text(strip=True))
        pct_fga_fg3a.append(unfiltered_pct_fga_fg3a[i].get_text(strip=True))
        fg_pct_fg2a.append(unfiltered_fg_pct_fg2a[i].get_text(strip=True))
        fg_pct_00_03.append(unfiltered_fg_pct_00_03[i].get_text(strip=True))
        fg_pct_03_10.append(unfiltered_fg_pct_03_10[i].get_text(strip=True))
        fg_pct_10_16.append(unfiltered_fg_pct_10_16[i].get_text(strip=True))
        fg_pct_16_xx.append(unfiltered_fg_pct_16_xx[i].get_text(strip=True))
        fg_pct_fg3a.append(unfiltered_fg_pct_fg3a[i].get_text(strip=True))
        pct_ast_fg2.append(unfiltered_pct_ast_fg2[i].get_text(strip=True))
        pct_ast_fg3.append(unfiltered_pct_ast_fg3[i].get_text(strip=True))
        pct_fga_dunk.append(unfiltered_pct_fga_dunk[i].get_text(strip=True))
        fg_dunk.append(unfiltered_fg_dunk[i].get_text(strip=True))
        pct_fg3a_corner3.append(unfiltered_pct_fg3a_corner3[i].get_text(strip=True))
        fg_pct_corner3.append(unfiltered_fg_pct_corner3[i].get_text(strip=True))
        fg3a_heave.append(unfiltered_fg3a_heave[i].get_text(strip=True))
        fg3_heave.append(unfiltered_fg3_heave[i].get_text(strip=True))

    df = pd.DataFrame(list(zip(players, pos, age, team_id, g, mp, fg_pct, avg_dist, pct_fga_fg2a, pct_fga_00_03, pct_fga_03_10, pct_fga_10_16, pct_fga_16_xx, pct_fga_fg3a, fg_pct_fg2a, fg_pct_00_03, fg_pct_03_10, fg_pct_10_16, fg_pct_16_xx, fg_pct_fg3a, pct_ast_fg2, pct_ast_fg3, pct_fga_dunk, fg_dunk, pct_fg3a_corner3, fg_pct_corner3, fg3a_heave, fg3_heave)), columns = ['Player', 'Pos', 'Age', 'Tm', 'G', 'MP', 'FG%', 'Dist', '%FGA2P', '%FGA0-3', '%FGA3-10', '%FGA10-16', '%FGA16-3P', '%FGA3P', '2P%', '0-3%', '3-10%', '10-16%', '16-3P%', '3P%', '%Ast2P', '%Ast3P', '%Dunks', 'Dunks', '%Corner3', 'Corner3%', 'HeavesAtt', 'Heaves#'])

    df['Player'] = df['Player'].str.replace("*", "", regex=True)

    return df


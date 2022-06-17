#!/usr/bin/env python
# coding: utf-8

# In[74]:


import pandas as pd
import requests
from bs4 import BeautifulSoup

def ShowStats(season):
    url = f"https://www.basketball-reference.com/leagues/NBA_{season}_play-by-play.html"
    response = requests.get(url)
    text = response.text
    soup = BeautifulSoup(text, features='lxml')
    
    players, pos, age, team_id, g, mp, pct_1, pct_2, pct_3, pct_4, pct_5, pm_on, pm_net, tovbp, tovlb, fs, fo, dfs, dfo, astd_pts, and1s, blkd = ([], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [])
    
    unfiltered_players = soup.find_all("td", {"data-stat":"player"})
    unfiltered_pos = soup.find_all("td", {"data-stat":"pos"})
    unfiltered_age = soup.find_all("td", {"data-stat":"age"})
    unfiltered_team_id = soup.find_all("td", {"data-stat":"team_id"})
    unfiltered_g = soup.find_all("td", {"data-stat":"g"})
    unfiltered_mp = soup.find_all("td", {"data-stat":"mp"})
    unfiltered_pct_1 = soup.find_all("td", {"data-stat":"pct_1"})
    unfiltered_pct_2 = soup.find_all("td", {"data-stat":"pct_2"})
    unfiltered_pct_3 = soup.find_all("td", {"data-stat":"pct_3"})
    unfiltered_pct_4 = soup.find_all("td", {"data-stat":"pct_4"})
    unfiltered_pct_5 = soup.find_all("td", {"data-stat":"pct_5"})
    unfiltered_pm_on = soup.find_all("td", {"data-stat":"plus_minus_on"})
    unfiltered_pm_net = soup.find_all("td", {"data-stat":"plus_minus_net"})
    unfiltered_tovbp = soup.find_all("td", {"data-stat":"tov_bad_pass"})
    unfiltered_tovlb = soup.find_all("td", {"data-stat":"tov_lost_ball"})
    unfiltered_fs = soup.find_all("td", {"data-stat":"fouls_shooting"})
    unfiltered_fo = soup.find_all("td", {"data-stat":"fouls_offensive"})
    unfiltered_dfs = soup.find_all("td", {"data-stat":"drawn_shooting"})
    unfiltered_dfo = soup.find_all("td", {"data-stat":"drawn_offensive"})
    unfiltered_astd_pts = soup.find_all("td", {"data-stat":"astd_pts"})
    unfiltered_and1s = soup.find_all("td", {"data-stat":"and1s"})
    unfiltered_blkd = soup.find_all("td", {"data-stat":"own_shots_blk"})
    
    for i in range(0, len(unfiltered_players)):
        
        players.append(unfiltered_players[i].get_text(strip=True))
        pos.append(unfiltered_pos[i].get_text(strip=True))
        age.append(unfiltered_age[i].get_text(strip=True))
        team_id.append(unfiltered_team_id[i].get_text(strip=True))
        g.append(unfiltered_g[i].get_text(strip=True))
        mp.append(unfiltered_mp[i].get_text(strip=True))
        pct_1.append(unfiltered_pct_1[i].get_text(strip=True))
        pct_2.append(unfiltered_pct_2[i].get_text(strip=True))
        pct_3.append(unfiltered_pct_3[i].get_text(strip=True))
        pct_4.append(unfiltered_pct_4[i].get_text(strip=True))
        pct_5.append(unfiltered_pct_5[i].get_text(strip=True))
        pm_on.append(unfiltered_pm_on[i].get_text(strip=True))
        pm_net.append(unfiltered_pm_net[i].get_text(strip=True))
        tovbp.append(unfiltered_tovbp[i].get_text(strip=True))
        tovlb.append(unfiltered_tovlb[i].get_text(strip=True))
        fs.append(unfiltered_fs[i].get_text(strip=True))
        fo.append(unfiltered_fo[i].get_text(strip=True))
        dfs.append(unfiltered_dfs[i].get_text(strip=True))
        dfo.append(unfiltered_dfo[i].get_text(strip=True))
        astd_pts.append(unfiltered_astd_pts[i].get_text(strip=True))
        and1s.append(unfiltered_and1s[i].get_text(strip=True))
        blkd.append(unfiltered_blkd[i].get_text(strip=True))
    
    df = pd.DataFrame(list(zip(players, pos, age, team_id, g, mp, pct_1, pct_2, pct_3, pct_4, pct_5, pm_on, pm_net, tovbp, tovlb, fs, fo, dfs, dfo, astd_pts, and1s, blkd)), columns = ['Player', 'Pos', 'Age', 'Tm', 'G', 'MP', 'PG%', 'SG%', 'SF%', 'PF%', 'C%', '+/-On', '+/-Net', 'TOBP', 'TOLB', 'FCShoot', 'FCOff', 'FDShoot', 'FCOff', 'PGA', 'And1', 'Blkd'])
    
    df['Player'] = df['Player'].str.replace("*", "", regex=True)

    return df


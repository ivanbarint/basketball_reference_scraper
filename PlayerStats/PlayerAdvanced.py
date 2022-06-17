#!/usr/bin/env python
# coding: utf-8

# In[46]:


import pandas as pd
import requests
from bs4 import BeautifulSoup
    
def ShowStats(season):
    url = f"https://www.basketball-reference.com/leagues/NBA_2021_advanced.html"
    response = requests.get(url)
    text = response.text
    soup = BeautifulSoup(text, features='lxml')

    players, pos, age, team_id, g, mp, per, ts_pct, fg3a_per_fga_pct, fta_per_fga_pct, orb_pct, drb_pct, trb_pct, ast_pct, stl_pct, blk_pct, tov_pct, usg_pct, ows, dws, ws, ws_per_48, obpm, dbpm, bpm, vorp = ([], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [])

    unfiltered_players = soup.find_all("td", {"data-stat":"player"})
    unfiltered_pos = soup.find_all("td", {"data-stat":"pos"})
    unfiltered_age = soup.find_all("td", {"data-stat":"age"})
    unfiltered_team_id = soup.find_all("td", {"data-stat":"team_id"})
    unfiltered_g = soup.find_all("td", {"data-stat":"g"})
    unfiltered_mp = soup.find_all("td", {"data-stat":"mp"})
    unfiltered_per = soup.find_all("td", {"data-stat":"per"})
    unfiltered_ts_pct = soup.find_all("td", {"data-stat":"ts_pct"})
    unfiltered_fg3a_per_fga_pct = soup.find_all("td", {"data-stat":"fg3a_per_fga_pct"})
    unfiltered_fta_per_fga_pct = soup.find_all("td", {"data-stat":"fta_per_fga_pct"})
    unfiltered_orb_pct = soup.find_all("td", {"data-stat":"orb_pct"})
    unfiltered_drb_pct = soup.find_all("td", {"data-stat":"drb_pct"})
    unfiltered_trb_pct = soup.find_all("td", {"data-stat":"trb_pct"})
    unfiltered_ast_pct = soup.find_all("td", {"data-stat":"ast_pct"})
    unfiltered_stl_pct = soup.find_all("td", {"data-stat":"stl_pct"})
    unfiltered_blk_pct = soup.find_all("td", {"data-stat":"blk_pct"})
    unfiltered_tov_pct = soup.find_all("td", {"data-stat":"tov_pct"})
    unfiltered_usg_pct = soup.find_all("td", {"data-stat":"usg_pct"})
    unfiltered_ows = soup.find_all("td", {"data-stat":"ows"})
    unfiltered_dws = soup.find_all("td", {"data-stat":"dws"})
    unfiltered_ws = soup.find_all("td", {"data-stat":"ws"})
    unfiltered_ws_per_48 = soup.find_all("td", {"data-stat":"ws_per_48"})
    unfiltered_obpm = soup.find_all("td", {"data-stat":"obpm"})
    unfiltered_dbpm = soup.find_all("td", {"data-stat":"dbpm"})
    unfiltered_bpm = soup.find_all("td", {"data-stat":"bpm"})
    unfiltered_vorp = soup.find_all("td", {"data-stat":"vorp"})


    for i in range(0, len(unfiltered_players)):
        players.append(unfiltered_players[i].get_text(strip=True))
        pos.append(unfiltered_pos[i].get_text(strip=True))
        age.append(unfiltered_age[i].get_text(strip=True))
        team_id.append(unfiltered_team_id[i].get_text(strip=True))
        g.append(unfiltered_g[i].get_text(strip=True))
        mp.append(unfiltered_mp[i].get_text(strip=True))
        per.append(unfiltered_per[i].get_text(strip=True))
        ts_pct.append(unfiltered_ts_pct[i].get_text(strip=True))
        fg3a_per_fga_pct.append(unfiltered_fg3a_per_fga_pct[i].get_text(strip=True))
        fta_per_fga_pct.append(unfiltered_fta_per_fga_pct[i].get_text(strip=True))
        orb_pct.append(unfiltered_orb_pct[i].get_text(strip=True))
        drb_pct.append(unfiltered_drb_pct[i].get_text(strip=True))
        trb_pct.append(unfiltered_trb_pct[i].get_text(strip=True))
        ast_pct.append(unfiltered_ast_pct[i].get_text(strip=True))
        stl_pct.append(unfiltered_stl_pct[i].get_text(strip=True))
        blk_pct.append(unfiltered_blk_pct[i].get_text(strip=True))
        tov_pct.append(unfiltered_tov_pct[i].get_text(strip=True))
        usg_pct.append(unfiltered_usg_pct[i].get_text(strip=True))
        ows.append(unfiltered_ows[i].get_text(strip=True))
        dws.append(unfiltered_dws[i].get_text(strip=True))
        ws.append(unfiltered_ws[i].get_text(strip=True))
        ws_per_48.append(unfiltered_ws_per_48[i].get_text(strip=True))
        obpm.append(unfiltered_obpm[i].get_text(strip=True))
        dbpm.append(unfiltered_dbpm[i].get_text(strip=True))
        bpm.append(unfiltered_bpm[i].get_text(strip=True))
        vorp.append(unfiltered_vorp[i].get_text(strip=True))

    df = pd.DataFrame(list(zip(players, pos, age, team_id, g, mp, per, ts_pct, fg3a_per_fga_pct, fta_per_fga_pct, orb_pct, drb_pct, trb_pct, ast_pct, stl_pct, blk_pct, tov_pct, usg_pct, ows, dws, ws, ws_per_48, obpm, dbpm, bpm, vorp)),
                          columns = ['Player', 'Pos', 'Age', 'Tm', 'G', 'MP', 'PER', 'TS%', '3PAr', 'FTr', 'ORB%', 'DRB%', 'TRB%', 'AST%', 'STL%', 'BLK%', 'TOV%', 'USG%', 'OWS', 'DWS', 'WS', 'WS/48', 'OBPM', 'DBPM', 'BPM', 'VORP'])

    df['Player'] = df['Player'].str.replace("*", "", regex=True)

    return df
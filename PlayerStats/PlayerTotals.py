import pandas as pd
import requests
from bs4 import BeautifulSoup
    
def ShowStats(season):
    url = f"https://www.basketball-reference.com/leagues/NBA_{season}_totals.html"
    response = requests.get(url)
    text = response.text
    soup = BeautifulSoup(text, features='lxml')

    players, pos, age, team_id, g, gs, mp, fg, fga, fg_pct, fg3, fg3a, fg3_pct, fg2, fg2a, fg2_pct, efg_pct, ft, fta, ft_pct, orb, drb, trb, ast, stl, blk, tov, pf, pts = ([], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [])

    unfiltered_players = soup.find_all("td", {"data-stat":"player"})
    unfiltered_pos = soup.find_all("td", {"data-stat":"pos"})
    unfiltered_age = soup.find_all("td", {"data-stat":"age"})
    unfiltered_team_id = soup.find_all("td", {"data-stat":"team_id"})
    unfiltered_g = soup.find_all("td", {"data-stat":"g"})
    unfiltered_gs = soup.find_all("td", {"data-stat":"gs"})
    unfiltered_mp = soup.find_all("td", {"data-stat":"mp"})
    unfiltered_fg = soup.find_all("td", {"data-stat":"fg"})
    unfiltered_fga = soup.find_all("td", {"data-stat":"fga"})
    unfiltered_fg_pct = soup.find_all("td", {"data-stat":"fg_pct"})
    unfiltered_fg3 = soup.find_all("td", {"data-stat":"fg3"})
    unfiltered_fg3a = soup.find_all("td", {"data-stat":"fg3a"})
    unfiltered_fg3_pct = soup.find_all("td", {"data-stat":"fg3_pct"})
    unfiltered_fg2 = soup.find_all("td", {"data-stat":"fg2"})
    unfiltered_fg2a = soup.find_all("td", {"data-stat":"fg2a"})
    unfiltered_fg2_pct = soup.find_all("td", {"data-stat":"fg2_pct"})
    unfiltered_efg_pct = soup.find_all("td", {"data-stat":"efg_pct"})
    unfiltered_ft = soup.find_all("td", {"data-stat":"ft"})
    unfiltered_fta = soup.find_all("td", {"data-stat":"fta"})
    unfiltered_ft_pct = soup.find_all("td", {"data-stat":"ft_pct"})
    unfiltered_orb = soup.find_all("td", {"data-stat":"orb"})
    unfiltered_drb = soup.find_all("td", {"data-stat":"drb"})
    unfiltered_trb = soup.find_all("td", {"data-stat":"trb"})
    unfiltered_ast = soup.find_all("td", {"data-stat":"ast"})
    unfiltered_stl = soup.find_all("td", {"data-stat":"stl"})
    unfiltered_blk = soup.find_all("td", {"data-stat":"blk"})
    unfiltered_tov = soup.find_all("td", {"data-stat":"tov"})
    unfiltered_pf = soup.find_all("td", {"data-stat":"pf"})
    unfiltered_pts = soup.find_all("td", {"data-stat":"pts"})

    for i in range(0, len(unfiltered_players)):
        players.append(unfiltered_players[i].get_text(strip=True))
        pos.append(unfiltered_pos[i].get_text(strip=True))
        age.append(unfiltered_age[i].get_text(strip=True))
        team_id.append(unfiltered_team_id[i].get_text(strip=True))
        g.append(unfiltered_g[i].get_text(strip=True))
        gs.append(unfiltered_gs[i].get_text(strip=True))
        mp.append(unfiltered_mp[i].get_text(strip=True))
        fg.append(unfiltered_fg[i].get_text(strip=True))
        fga.append(unfiltered_fga[i].get_text(strip=True))
        fg_pct.append(unfiltered_fg_pct[i].get_text(strip=True))
        fg3.append(unfiltered_fg3[i].get_text(strip=True))
        fg3a.append(unfiltered_fg3a[i].get_text(strip=True))
        fg3_pct.append(unfiltered_fg3_pct[i].get_text(strip=True))
        fg2.append(unfiltered_fg2[i].get_text(strip=True))
        fg2a.append(unfiltered_fg2a[i].get_text(strip=True))
        fg2_pct.append(unfiltered_fg2_pct[i].get_text(strip=True))
        efg_pct.append(unfiltered_efg_pct[i].get_text(strip=True))
        ft.append(unfiltered_ft[i].get_text(strip=True))
        fta.append(unfiltered_fta[i].get_text(strip=True))
        ft_pct.append(unfiltered_ft_pct[i].get_text(strip=True))
        orb.append(unfiltered_orb[i].get_text(strip=True))
        drb.append(unfiltered_drb[i].get_text(strip=True))
        trb.append(unfiltered_trb[i].get_text(strip=True))
        ast.append(unfiltered_ast[i].get_text(strip=True))
        stl.append(unfiltered_stl[i].get_text(strip=True))
        blk.append(unfiltered_blk[i].get_text(strip=True))
        tov.append(unfiltered_tov[i].get_text(strip=True))
        pf.append(unfiltered_pf[i].get_text(strip=True))
        pts.append(unfiltered_pts[i].get_text(strip=True))

    df = pd.DataFrame(list(zip(players, pos, age, team_id, g, gs, mp, fg, fga, fg_pct, fg3, fg3a, fg3_pct, fg2, fg2a, fg2_pct, efg_pct, ft, fta, ft_pct, orb, drb, trb, ast, stl, blk, tov, pf, pts)),
                          columns = ['Player', 'Pos', 'Age', 'Tm', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', '2P', '2PA', '2P%', 'eFG%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS'])

    df['Player'] = df['Player'].str.replace("*", "", regex=True)

    return df
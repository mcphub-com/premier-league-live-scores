import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/heisenbug/api/premier-league-live-scores'

mcp = FastMCP('premier-league-live-scores')

@mcp.tool()
def team(name: Annotated[str, Field(description='')]) -> dict: 
    '''Returns info about the team'''
    url = 'https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague/team'
    headers = {'x-rapidapi-host': 'heisenbug-premier-league-live-scores-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'name': name,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def venue(name: Annotated[str, Field(description='')]) -> dict: 
    '''Returns venue data'''
    url = 'https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague/venue'
    headers = {'x-rapidapi-host': 'heisenbug-premier-league-live-scores-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'name': name,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def referees_statistics() -> dict: 
    '''Referees statistics'''
    url = 'https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague/table/referee'
    headers = {'x-rapidapi-host': 'heisenbug-premier-league-live-scores-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def season_matches_results(matchday: Annotated[Union[str, None], Field(description='Return all matches results for the specified match day')] = None,
                           season: Annotated[Union[str, None], Field(description='Season code (default 2017-18)')] = None,
                           date: Annotated[Union[str, None], Field(description='Returns all match in the date (format mmddyyyy)')] = None,
                           live: Annotated[Union[bool, None], Field(description='Returns results for playing matches (live) (default false, overwrite others parameters)')] = None,
                           team1: Annotated[Union[str, None], Field(description='Returns all matches with team1')] = None,
                           team2: Annotated[Union[str, None], Field(description='Returns all matches with team2')] = None) -> dict: 
    '''Return season matches results for a match day'''
    url = 'https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague'
    headers = {'x-rapidapi-host': 'heisenbug-premier-league-live-scores-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'matchday': matchday,
        'season': season,
        'date': date,
        'live': live,
        'team1': team1,
        'team2': team2,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def match_scorers(team1: Annotated[str, Field(description='Home team name')],
                  team2: Annotated[str, Field(description='Away team name')],
                  live: Annotated[Union[bool, None], Field(description='Returns data for a playing match (default false)')] = None) -> dict: 
    '''Return scorers for a match. Not available for BASIC plan.'''
    url = 'https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague/scorers'
    headers = {'x-rapidapi-host': 'heisenbug-premier-league-live-scores-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'team1': team1,
        'team2': team2,
        'live': live,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def lineups_and_substitutes_for_agame(team1: Annotated[str, Field(description='Home team name')],
                                      team2: Annotated[str, Field(description='Away team name')],
                                      live: Annotated[Union[str, None], Field(description='Returns data for a playing match (default false)')] = None) -> dict: 
    '''Return lineups, substitutes and coaches for a game (only after the game is finished). Not available for BASIC plan.'''
    url = 'https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague/formations'
    headers = {'x-rapidapi-host': 'heisenbug-premier-league-live-scores-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'team1': team1,
        'team2': team2,
        'live': live,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def match_events(team2: Annotated[str, Field(description='Amat team name')],
                 team1: Annotated[str, Field(description='Home tema name')],
                 live: Annotated[Union[bool, None], Field(description='Returns data for a playing match (default false)')] = None) -> dict: 
    '''Return the events for a match (yellow and red cards, substitutions, shots on post and formations module). Not available for BASIC plan.'''
    url = 'https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague/match/events'
    headers = {'x-rapidapi-host': 'heisenbug-premier-league-live-scores-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'team2': team2,
        'team1': team1,
        'live': live,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def player_stats_for_amatch(team1: Annotated[str, Field(description='Home team name')],
                            team2: Annotated[str, Field(description='Away team name')],
                            player: Annotated[str, Field(description='Player name')],
                            live: Annotated[Union[bool, None], Field(description='Returns data for a playing match (default false)')] = None) -> dict: 
    '''Return the player's statistics for a match. Not available for BASIC plan.'''
    url = 'https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague/match/player'
    headers = {'x-rapidapi-host': 'heisenbug-premier-league-live-scores-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'team1': team1,
        'team2': team2,
        'player': player,
        'live': live,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def top_scorers(todate: Annotated[Union[str, None], Field(description='Compute the table only with matches played todate (format mmddyyyy)')] = None,
                page: Annotated[Union[int, float, None], Field(description='Page result to return. Default is 1 that are results from 1 to 5 (max. value is 20).')] = None,
                _from: Annotated[Union[int, float, None], Field(description='Optional parameter to specify the first match number to use to compute the result (default 1)')] = None,
                player: Annotated[Union[str, None], Field(description='Optional parameter to get goals number only for the player name specified')] = None,
                team: Annotated[Union[str, None], Field(description='Team name')] = None,
                to: Annotated[Union[int, float, None], Field(description='Optional parameter to specify the last match number to consider to compute the result (default last match number played registered on system)')] = None,
                mode: Annotated[Union[str, None], Field(description='Optional parameter to restrict the table compute on home or away games (possible values are home, away or all, that is the default)')] = None,
                fromdate: Annotated[Union[str, None], Field(description='Compute the table only with matches played fromdate (forma mmddyyyy)')] = None,
                how: Annotated[Union[str, None], Field(description='Return only goals scored according the how parameter. Its value can be: left, right, head or any, that is the default.')] = None) -> dict: 
    '''Returns top scorers for the league'''
    url = 'https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague/table/scorers'
    headers = {'x-rapidapi-host': 'heisenbug-premier-league-live-scores-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'todate': todate,
        'page': page,
        'from': _from,
        'player': player,
        'team': team,
        'to': to,
        'mode': mode,
        'fromdate': fromdate,
        'how': how,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def match_statistics(team1: Annotated[str, Field(description='Home team name')],
                     team2: Annotated[str, Field(description='Away team name')],
                     live: Annotated[Union[bool, None], Field(description='Returns data for a playing match (default false)')] = None) -> dict: 
    '''Return statistics for a match after a while it is finished or live. Not available for BASIC plan.'''
    url = 'https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague/match/stats'
    headers = {'x-rapidapi-host': 'heisenbug-premier-league-live-scores-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'team1': team1,
        'team2': team2,
        'live': live,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def league_players(team: Annotated[str, Field(description='Team name')]) -> dict: 
    '''Returns all players for a team. Not available for BASIC plan.'''
    url = 'https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague/players'
    headers = {'x-rapidapi-host': 'heisenbug-premier-league-live-scores-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'team': team,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def missing_players_for_amatch(team1: Annotated[str, Field(description='Home team name')],
                               team2: Annotated[str, Field(description='Away team name')]) -> dict: 
    '''Return missing players for a match. Not available for BASIC plan.'''
    url = 'https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague/match/missing'
    headers = {'x-rapidapi-host': 'heisenbug-premier-league-live-scores-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'team1': team1,
        'team2': team2,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def players_statistic_table(stat: Annotated[str, Field(description='Statistic name')],
                            _from: Annotated[Union[str, None], Field(description='Match day number from which compute the table')] = None,
                            player: Annotated[Union[str, None], Field(description='Player name')] = None,
                            to: Annotated[Union[str, None], Field(description='Match day number till which compute the table')] = None,
                            team: Annotated[Union[str, None], Field(description='Team name')] = None) -> dict: 
    '''Return the players table for a specified statistic. Not available for BASIC plan.'''
    url = 'https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague/table/playerstat'
    headers = {'x-rapidapi-host': 'heisenbug-premier-league-live-scores-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'stat': stat,
        'from': _from,
        'player': player,
        'to': to,
        'team': team,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def teams_statistic_table(stat: Annotated[str, Field(description='Statistic name')],
                          avg: Annotated[Union[str, None], Field(description='Set to true if you want average statistic value, that is the table computed as (total value statistic/played games). Default false.')] = None,
                          _from: Annotated[Union[str, None], Field(description='Match day number from which to compute the table')] = None,
                          mode: Annotated[Union[str, None], Field(description='Set with top to get the top 5, with bottom to get the worse 5 teams (default top)')] = None,
                          team: Annotated[Union[str, None], Field(description='Team name')] = None,
                          to: Annotated[Union[str, None], Field(description='Match day number till which compute the table')] = None) -> dict: 
    '''Teams table for a specified statistic. Not available for BASIC plan.'''
    url = 'https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague/table/teamstat'
    headers = {'x-rapidapi-host': 'heisenbug-premier-league-live-scores-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'stat': stat,
        'avg': avg,
        'from': _from,
        'mode': mode,
        'team': team,
        'to': to,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def player_details(player: Annotated[str, Field(description='Player name')],
                   team: Annotated[str, Field(description='Team name')],
                   honours: Annotated[Union[bool, None], Field(description='Return only the honours for the player (default false)')] = None) -> dict: 
    '''Returns all data about a player. Available only with ULTRA and MEGA plans!'''
    url = 'https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague/playerdetails'
    headers = {'x-rapidapi-host': 'heisenbug-premier-league-live-scores-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'player': player,
        'team': team,
        'honours': honours,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def league_table(_from: Annotated[Union[int, float, None], Field(description='Optional parameter to specify the first match number to use to compute the table (default 1)')] = None,
                 mode: Annotated[Union[str, None], Field(description='Optional parameter to restrict the table compute on home or away games (default all)')] = None,
                 season: Annotated[Union[str, None], Field(description='Season code (default 2017-18)')] = None,
                 time: Annotated[Union[str, None], Field(description='Let to compute the table considering only the first half (FH) or the second time (SH) results. Default is full time (FT).')] = None,
                 to: Annotated[Union[int, float, None], Field(description='Optional parameter to specify the last match number to consider to compute the table (default last match number played registered on system)')] = None,
                 fromdate: Annotated[Union[str, None], Field(description='Compute the table only with matches played fromdate (format mmddyyyy)')] = None,
                 todate: Annotated[Union[str, None], Field(description='Compute the table only with matches played todate (format mmddyyyy)')] = None) -> dict: 
    '''Returns the table for the league'''
    url = 'https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague/table'
    headers = {'x-rapidapi-host': 'heisenbug-premier-league-live-scores-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'from': _from,
        'mode': mode,
        'season': season,
        'time': time,
        'to': to,
        'fromdate': fromdate,
        'todate': todate,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def prediction(team2: Annotated[str, Field(description='Away team name (case sensitiva)')],
               team1: Annotated[str, Field(description='Home team name (case sensitive)')]) -> dict: 
    '''Returns match result perdiction (use an AI deep learning engine)'''
    url = 'https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague/predict'
    headers = {'x-rapidapi-host': 'heisenbug-premier-league-live-scores-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'team2': team2,
        'team1': team1,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def bookmakers_list(team1: Annotated[str, Field(description='Home team')],
                    team2: Annotated[str, Field(description='Away team')]) -> dict: 
    '''Return the list of the available bookmakers for a match. Not available for BASIC plan.'''
    url = 'https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague/listbookmakers'
    headers = {'x-rapidapi-host': 'heisenbug-premier-league-live-scores-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'team1': team1,
        'team2': team2,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def odds_list(team1: Annotated[str, Field(description='Home team')],
              bookmaker: Annotated[str, Field(description='Bookmaker name')],
              team2: Annotated[str, Field(description='Away team')]) -> dict: 
    '''Returns the available odds for a match and a bookmaker. Not available for BASIC plan.'''
    url = 'https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague/listodds'
    headers = {'x-rapidapi-host': 'heisenbug-premier-league-live-scores-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'team1': team1,
        'bookmaker': bookmaker,
        'team2': team2,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def bet_stats(bet: Annotated[str, Field(description='Type of data required, result, totalgoals,underover,1x2,goalnogoal')],
              team: Annotated[Union[str, None], Field(description='Team name')] = None,
              time: Annotated[Union[str, None], Field(description='Let you to select only first half (FH) result, second half (SH) or full time (FT) default')] = None,
              fromdate: Annotated[Union[str, None], Field(description='Only matches fromdate (format mmddyyyy)')] = None,
              todate: Annotated[Union[str, None], Field(description='Only matches todate (format mmddyyyy)')] = None,
              over: Annotated[Union[int, float, None], Field(description='Over values, mandatory for underover bet')] = None,
              mode: Annotated[Union[str, None], Field(description='Together with team parameter, let you to select only games where team has played home, away or all (default)')] = None,
              handicap: Annotated[Union[int, float, None], Field(description='Handicap values (only for 1x2 bet)')] = None,
              when: Annotated[Union[str, None], Field(description='Let you to select only games with win, loss, draw or all (default)')] = None) -> dict: 
    '''Returns aggregate data about results, goal-nogoal, underover, 1x2 and totalgoals to support your bet activities. Not available for BASIC plan.'''
    url = 'https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague/table/betting'
    headers = {'x-rapidapi-host': 'heisenbug-premier-league-live-scores-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'bet': bet,
        'team': team,
        'time': time,
        'fromdate': fromdate,
        'todate': todate,
        'over': over,
        'mode': mode,
        'handicap': handicap,
        'when': when,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def odd_quotas(bookmaker: Annotated[str, Field(description='Bookmaker name')],
               odd: Annotated[str, Field(description='Odd name')],
               team1: Annotated[str, Field(description='Home team')],
               team2: Annotated[str, Field(description='Away team')]) -> dict: 
    '''Return quotas for an odd a match and a bookmaker. Not available for BASIC plan.'''
    url = 'https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague/odds'
    headers = {'x-rapidapi-host': 'heisenbug-premier-league-live-scores-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'bookmaker': bookmaker,
        'odd': odd,
        'team1': team1,
        'team2': team2,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def events_subscribed() -> dict: 
    '''Returns all the events subscribed. Not available for BASIC plan.'''
    url = 'https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague/push/list'
    headers = {'x-rapidapi-host': 'heisenbug-premier-league-live-scores-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def subscribe(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Register to an event for push notifications. Not available for BASIC plan.'''
    url = 'https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague/push/subscribe'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'heisenbug-premier-league-live-scores-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def activate_webhook(token: Annotated[str, Field(description='Token')]) -> dict: 
    '''Activate a webhook registered with the subscribe endpoint. Not available for BASIC plan.'''
    url = 'https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague/push/activate'
    headers = {'x-rapidapi-host': 'heisenbug-premier-league-live-scores-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'token': token,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")

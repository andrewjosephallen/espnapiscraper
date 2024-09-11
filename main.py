import csv
from espn_api.football import League

# Replace with your actual cookie values
league_id = int(input('Input your league id: '))
year = int(input('Input your year: '))
espn_s2 = input('Input your espns2: ')
swid = input('Input your swid: ')

# Initialize the League object with authentication
league = League(league_id=league_id, year=year, espn_s2=espn_s2, swid=swid)


def get_weekly_scores_with_players_and_free_agents_to_csv(week=None):
    """Get matchups, player scores, free agents, and save to a CSV."""
    if not week:
        week = league.nfl_week

    # File path to save the CSV
    file_path = f'week_{week}_player_scores_with_free_agents.csv'

    # Open a CSV file for writing
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['PlayerName', 'Score', 'Team', 'SlotPosition'])

        # Fetch matchups and player scores (including bench players)
        matchups = league.box_scores(week=week)
        for matchup in matchups:
            # Away team players (including bench)
            for player in matchup.away_lineup:
                writer.writerow([player.name, player.points, matchup.away_team.team_name, player.slot_position])

            # Home team players (including bench)
            for player in matchup.home_lineup:
                writer.writerow([player.name, player.points, matchup.home_team.team_name, player.slot_position])

        # Fetch free agents/waiver players
        free_agents = league.free_agents(week=week, size=500)
        for player in free_agents:
            writer.writerow([player.name, player.points, 'Free Agent / Waivers', 'N/A'])

    print(f"CSV file saved to: {file_path}")


# Call the function to generate the CSV
get_weekly_scores_with_players_and_free_agents_to_csv(week=1)

from bs4 import BeautifulSoup
import requests
import datetime
import re

URLS = [
    ("https://hokiesports.com/sports/football/schedule", "Football"),
    ("https://hokiesports.com/sports/mens-basketball/schedule", "Men\'s Basketball")
]

DATE_PATTERN = re.compile(r"([a-zA-Z]+) ([0-9]+) \([a-zA-Z]+\)")


# array to be populated with games
games = []

# the months of the football/basketball season,
# with an "additional" year so that we can
# sort chronologically. kind of a hack
SEASON_MONTHS = {
    "Sep": 0,
    "Oct": 0,
    "Nov": 0,
    "Dec": 0,
    "Jan": 1,
    "Feb": 1,
    "Mar": 1,
    "Apr": 1
}
MONTHS = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]


def get_latest_game():
    global games
    for url, sport in URLS:
        req = requests.get(url)
        soup = BeautifulSoup(req.text, "html.parser")
        game_elements = soup.find_all(
            "li", class_="sidearm-schedule-game-completed")

        for game_element in game_elements:
            date_element = game_element.find(
                class_="sidearm-schedule-game-opponent-date")

            date_text = date_element.text.strip()
            date_match = DATE_PATTERN.match(date_text)
            month_name = date_match.group(1)
            month = MONTHS.index(month_name) + 1
            day = int(date_match.group(2))
            year = 2020 + SEASON_MONTHS[month_name]

            date = datetime.date(year, month, day)

            opponent_element = game_element.find(
                class_="sidearm-schedule-game-opponent-name")

            opponent = opponent_element.text.strip().split("\n")[-1].strip()

            result_element = game_element.find(
                class_="sidearm-schedule-game-result")

            result = " ".join([x.strip()
                               for x in result_element.text.split("\n")]).strip()

            result_bool = None

            if result.startswith("W"):
                result_bool = True
            elif result.startswith("L"):
                result_bool = False

            games.append(
                (date, sport, opponent, result_bool, result)
            )

    # get latest game
    # make sure result_bool isn't None
    games = [x for x in games if x[3] != None]
    games.sort(key=lambda x: x[0])  # sort by date
    latest = games[-1]

    return latest

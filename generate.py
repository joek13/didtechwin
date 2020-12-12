import render
import scrape
import sys

OUTPUT_PATH = "./docs/index.html"

latest_game = scrape.get_latest_game()

with open("./docs/index.html", "w") as out:
    date, sport, opponent, win, score = latest_game
    search_string = f"virginia tech {sport} {opponent}"
    # google search url for this game
    query = f"https://google.com/search?q={search_string}"
    rendered = render.render_page(
        win=win,
        score=score,
        query=query
    )
    out.write(rendered)

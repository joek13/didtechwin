import render
import sys

OUTPUT_PATH = "./docs/index.html"

if len(sys.argv) != 2:
    print(f"{sys.argv[0]}: incorrect number of arguments")
    print(f"usage: {sys.argv[0]} <win: True/False>")
    sys.exit(1)

if sys.argv[1].lower() not in ["true", "false"]:
    print(f"{sys.argv[0]}: invalid argument {sys.argv[1]}")
    print(f"usage: {sys.argv[0]} <win: True/False>")
    sys.exit(1)

win = True if sys.argv[1].lower() == "true" else False

with open("./docs/index.html", "w") as out:
    rendered = render.render_page(win)
    out.write(rendered)

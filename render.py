from jinja2 import Template

TEMPLATE_PATH = "./templates/index.html"  # path to template file

_template = None

with open(TEMPLATE_PATH, "r") as template_file:
    _template = Template(template_file.read())


def render_page(**kwargs):
    """
    Returns rendered index.html, saying YES/NO depending on whether `tech_wins` is True.
    """
    return _template.render(**kwargs)

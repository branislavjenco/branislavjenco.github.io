import markdown
from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape()
)

template = env.get_template("index.html")
markdown.markdownFromFile(input="about.md", output="about.html")
with open("about.html") as f:
    about_str = f.read()
    result = template.render(about=about_str)

print(result)
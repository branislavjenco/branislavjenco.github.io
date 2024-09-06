import os
import shutil
import markdown
from jinja2 import Environment, FileSystemLoader, select_autoescape

build_folder = "build"

if os.path.isdir(build_folder):
    shutil.rmtree(build_folder)
os.mkdir(build_folder)


env = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape()
)

template = env.get_template("index.html")
markdown.markdownFromFile(input="about.md", output=f"{build_folder}/about.html")

posts_folder = 'posts'
posts_html = ''

posts_to_publish = [
    f for f
    in sorted(os.listdir(posts_folder), reverse=True)
    if not f.startswith("xx") and f.endswith(".md")
]

for filename in posts_to_publish:
    file_path = os.path.join(posts_folder, filename)
    if os.path.isfile(file_path):
        html_file_path = f"{build_folder}/{filename}".replace(".md", ".html")
        markdown.markdownFromFile(input=file_path, output=html_file_path)
        with open(html_file_path) as f:
            posts_html = posts_html + f.read()


with open(f"{build_folder}/about.html") as f:
    about_str = f.read()
    result = template.render(about=about_str, posts=posts_html)


with open(f"{build_folder}/index.html", 'w') as f:
    f.write(result)
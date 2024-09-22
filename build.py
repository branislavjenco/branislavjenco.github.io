import os
import shutil
import markdown
from jinja2 import Environment, FileSystemLoader, select_autoescape

build_folder = "build"
extensions = ['fenced_code', 'extra']

if os.path.isdir(build_folder):
    shutil.rmtree(build_folder)
os.mkdir(build_folder)


env = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape()
)

index_template = env.get_template("index.html")
about_template = env.get_template("about.html")

markdown.markdownFromFile(input="about.md", output=f"{build_folder}/about.html", extensions=extensions)
about_html = ''

with open(f"{build_folder}/about.html") as f:
    about_html = f.read()

posts_folder = 'posts'
posts_html = ''

posts_to_publish = [
    f for f
    in sorted(os.listdir(posts_folder), reverse=True)
    if not f.startswith("xx") and f.endswith(".md")
]

def preprocess(lines: list[str]):
    lines.pop(0)
    title = f"## {lines.pop(0)}"
    date = f"_{lines.pop(0)[:-1]}_\n"
    lines.pop(0)
    new_lines = ["___\n", title, date, *lines]
    return "".join(new_lines)

for filename in posts_to_publish:
    file_path = os.path.join(posts_folder, filename)
    if os.path.isfile(file_path):
        with open(file_path) as f:
            post_lines = f.readlines()
            if "hosts" in post_lines[1]:
                print(post_lines)
            post_md = preprocess(post_lines) 
            if "hosts" in post_lines[1]:
                print(post_md)
            post_html = markdown.markdown(post_md, extensions=extensions)
            posts_html = posts_html + post_html


with open(f"{build_folder}/about.html", 'w') as f:
    result = about_template.render(about=about_html)
    f.write(result)


with open(f"{build_folder}/index.html", 'w') as f:
    result = index_template.render(posts=posts_html)
    f.write(result)

shutil.copytree("images", "build/images", dirs_exist_ok=True)
shutil.copytree("styles", "build/styles", dirs_exist_ok=True)
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
post_template = env.get_template("mainpage_post.html")
single_post_template = env.get_template("single_post.html")

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
    title = lines.pop(0)
    date = lines.pop(0)
    lines.pop(0)
    return title, date, "".join(lines)

for filename in posts_to_publish:
    file_path = os.path.join(posts_folder, filename)
    if os.path.isfile(file_path):
        with open(file_path) as f:
            post_lines = f.readlines()
            title, date, post_md = preprocess(post_lines) 
            title_link = f"<a href='{filename.replace('.md','')}'>{title}</a>"
            post_html = markdown.markdown(post_md, extensions=extensions)
            post_rendered = post_template.render(title=title_link, date=date, body=post_html)
            posts_html = posts_html + post_rendered
            print(title)
            single_post_rendered = single_post_template.render(title=title, date=date, body=post_html)
            with open(f"{build_folder}/{filename.replace('.md','')}.html", 'w') as f:
                f.write(single_post_rendered)


with open(f"{build_folder}/about.html", 'w') as f:
    result = about_template.render(about=about_html)
    f.write(result)


with open(f"{build_folder}/index.html", 'w') as f:
    result = index_template.render(posts=posts_html)
    f.write(result)

shutil.copytree("images", "build/images", dirs_exist_ok=True)
shutil.copytree("styles", "build/styles", dirs_exist_ok=True)
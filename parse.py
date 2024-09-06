import os
import markdown


posts_folder = "posts"
posts_to_publish = [
    f for f
    in sorted(os.listdir(posts_folder), reverse=True)
    if not f.startswith("xx") and f.endswith(".md")
]

def add_frontmatter(lines):
    sep = '---\n'
    if lines[0].startswith(sep):
        # don't do anything
        return lines
    title = f"title: {lines[0].replace('# ', '')}"
    text_without_title = lines[1:]
    new_lines = [sep, title, sep] + text_without_title
    return new_lines

with open("til.md") as f:
    til_posts = f.read().split("\n\n")
    print(til_posts)
    # TODO turn til posts into posts
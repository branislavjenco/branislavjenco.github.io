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

    lines[0] = lines[0].replace('# ', '')
    date, lines[0] = lines[0].split(" ")[0], " ".join(lines[0].split(" ")[1:])
    title = f"title: {lines[0]}\n"
    text_without_title = lines[1:]
    new_lines = [sep, title, sep] + text_without_title
    filename = date + "-" + "-".join(lines[0].split(" ")[:3])
    return new_lines, filename

with open("til.md") as f:
    til_posts = f.read().split("\n\n\n")
    for post in til_posts:
        lines = post.split("\n")
        new_lines, filename = add_frontmatter(lines)
        with open(f"{posts_folder}/{filename}.md", 'w') as f:
            f.writelines(new_lines)

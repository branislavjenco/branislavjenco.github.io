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

def insert_dates(posts, posts_folder):
    for filename in posts:
        if filename.endswith(".md"):
            date_part = filename[:10]
            
            file_path = os.path.join(posts_folder, filename)
            
            with open(file_path, 'r') as file:
                lines = file.readlines()
            
            if len(lines) >= 2:
                lines.insert(2, f"{date_part}\n")
            else:
                lines.append(f"{date_part}\n")
            
            with open(file_path, 'w') as file:
                file.writelines(lines)

insert_dates(posts_to_publish, posts_folder)
from os import listdir

import frontmatter as fm
import toml  # required by frontmatter to parse toml metadata

from file import copy_file, create_empty_dir
from post import Post


def read_post_files(input_dir: str) -> list[Post]:
    posts = []
    filenames = listdir(input_dir)
    for filename in filenames:
        if filename.endswith('.md') or filename.endswith('.markdown'):
            file = open(input_dir + '/' + filename).read()
            data = fm.loads(file, fm.TOMLHandler)
            date = data.get('date')
            if date is not None:
                post = Post(filename, date.year, date.month)
                posts.append(post)
    print("Found %s posts." % len(posts))
    return posts


def sort_posts(posts: list[Post]):
    #  sort files like so:
    #  "2023": {
    #    "01": [
    #      "filename.md"
    #    ]
    #  }
    sorted_posts = {}
    for post in posts:
        if post.year not in sorted_posts:
            sorted_posts[post.year] = {}
        if post.month not in sorted_posts[post.year]:
            sorted_posts[post.year][post.month] = []
        sorted_posts[post.year][post.month].append(post.filename)
    print("Sorted posts.")
    return sorted_posts


def write_sorted_posts(input_dir: str, base_output_dir: str, posts):
    for year in posts.keys():
        year_str = str(year)
        create_empty_dir(base_output_dir + "/" + str(year))
        for month in posts[year].keys():
            month_str = str(month)
            if month < 10: month_str = "0" + month_str
            output_dir = base_output_dir + "/" + year_str + "/" + month_str
            create_empty_dir(base_output_dir + "/" + year_str + "/" + month_str)
            for filename in posts[year][month]:
                copy_file(input_dir, output_dir, filename)

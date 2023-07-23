from organiser import read_post_files, sort_posts, write_sorted_posts

in = "in"
out = "out"

posts = read_post_files(in)  # read posts from given source directory
sorted_posts = sort_posts(posts)  # sort posts into desired folder structure
clear_dir(out)  # clear output folder
write_sorted_posts(in, out, sorted_posts)  # write new post files

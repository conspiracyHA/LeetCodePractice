from os import path


def path_join(*args):
    cur_dir = path.abspath(path.curdir)
    x, y = path.split(cur_dir)
    return path.join(x, *args)



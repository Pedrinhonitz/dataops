def recreate_path(dir_path):
    from os import mkdir
    from shutil import rmtree
    
    try:
        mkdir(dir_path)
    except FileExistsError:
        rmtree(dir_path)
        mkdir(dir_path)


def create_if_not_exists(dir_path):
    from os import makedirs

    try:
        makedirs(dir_path)
    except FileExistsError:
        pass
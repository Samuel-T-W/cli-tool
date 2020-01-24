import click
import os


def get_dir_name(dirName):
    i = dirName.rfind('\\')
    if i == -1:
        return dirName
    else:
        return dirName[ dirName.rindex('\\')+1:]

def get_relative_depth(dir_path, level_offset):
    return dir_path.count(os.path.sep) - level_offset

class Config(object):
    def __init__(self):
        self.home_dir= '.'

pass_config = click.make_pass_decorator(Config, ensure=True)

@click.group()
@pass_config
def cli(config):
    pass


@cli.command()
@pass_config
def tree(config):
    rootDir='.'

    if os.path.isdir(rootDir) and os.path.exists(rootDir):
        indent=' '
        levelOffset = rootDir.count(os.path.sep) 

        
        for dirName, subdirlist, fileList in os.walk(rootDir):
            level = get_relative_depth(dirName, levelOffset)
            if level == 0:
                print('{}'.format(get_dir_name(dirName)))
            else:
                print(indent*(level-1) + '{}.{}'.format(level-1, get_dir_name(dirName)))

            for fname in fileList:
                print(indent*level + '{}.{}'.format(level, fname))  
 


if __name__ == 'main':
    unix()
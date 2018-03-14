import os

examplesdir = os.path.dirname(os.path.realpath(__file__))
projects = ['common_emitter', 'joule_thief', 'mcu', 'sallen_key', 'voltage_divider']


def build_dir_path(example):
    return os.path.join(examplesdir, example, 'build')


def file_path(example, file):
    return os.path.join(examplesdir, example, file)


def build_file_path(example, file):
    return os.path.join(build_dir_path(example), file)


def build(path):
    os.system('python3 %s' % path)


def clean(path):
    os.system('rm -rf %s' % path)


def open_svg(path):
    os.system('chromium %s &' % path)


if __name__ == '__main__':
    clean('build')
    for project in projects:
        print('Building', project)
        build(file_path(project, project + '.py'))

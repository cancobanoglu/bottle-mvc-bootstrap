#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import shutil
from zipfile import ZipFile

CONTENT = {
    'controllers_init': '\
import os\n\
import glob\n\
__all__ = [\n\
            os.path.basename(f)[:-3]\n\
            for f in glob.glob(os.path.dirname(__file__) + "/*.py")\n\
        ]',

    'controllers_index': '\
# -*- coding: utf-8 -*-\n\
from {project} import app\n\
from bottle import view\n\
\n\
\n\
@app.route("/", method="GET")\n\
@view("index")\n\
def index():\n\
    return dict()',

    'controllers_static': '\
# -*- coding: utf-8 -*-\n\
from {project} import app\n\
from bottle import static_file\n\
\n\
\n\
@app.route("/:file#(favicon.ico|humans.txt)#")\n\
def favicon(file):\n\
    return static_file(file, root="{project}/static/misc")\n\
\n\
\n\
@app.route("/:path#(img|css|js|fonts)\/.+#")\n\
def server_static(path):\n\
    return static_file(path, root="{project}/static")',

    'init': '\
# -*- coding: utf-8 -*-\n\
__version__ = "0.1"\n\
from bottle import Bottle, TEMPLATE_PATH\n\
app = Bottle()\n\
TEMPLATE_PATH.append("./{project}/views/")\n\
TEMPLATE_PATH.remove("./views/")\n\
from {project}.controllers import *',

    'run': '\
#!/usr/bin/env python\n\
# -*- coding: utf-8 -*-\n\
import os\n\
from {project} import app\n\
from bottle import debug, run\n\
\n\
debug(True)\n\
if __name__ == "__main__":\n\
    port = int(os.environ.get("PORT", 8080))\n\
    run(app, reloader=True, host="0.0.0.0", port=port)\n\
'
}

_PATH = os.sep.join([
    sys.prefix,
    'lib',
    'python' + '.'.join(str(i) for i in sys.version_info[:2]),
    'site-packages',
    'bottle_mvc_bootstrap',
    'static_files'
])

CONTENT_FILES = {
    'index': os.sep.join([_PATH, 'index.tpl']),
    'bootstrap': os.sep.join([_PATH, 'bootstrap.zip']),
    'jquery': os.sep.join([_PATH, 'jquery.js'])
}

CONTROLLERS = 'controllers'
MODELS = 'models'
STATIC = 'static'
VIEWS = 'views'


def create_file(path, content):
    f = open(path, 'w')
    f.write(content)
    f.close()


def create_scaffold(name):
    # Creating folders:
    os.makedirs(name)
    for folder in [CONTROLLERS, MODELS, VIEWS, STATIC]:
        path = os.sep.join([name, folder])
        os.makedirs(path)
    os.makedirs(os.sep.join([name, STATIC, 'misc']))

    # Creating files:

    # Models init:
    create_file(
        os.sep.join([name, MODELS, '__init__.py']),
        ''
    )
    # Controllers init:
    create_file(
        os.sep.join([name, CONTROLLERS, '__init__.py']),
        CONTENT['controllers_init']
    )

    # Controllers index:
    create_file(
        os.sep.join([name, CONTROLLERS, 'index.py']),
        CONTENT['controllers_index'].format(project=name)
    )

    # Controllers static:
    create_file(
        os.sep.join([name, CONTROLLERS, 'static.py']),
        CONTENT['controllers_static'].format(project=name)
    )

    # init:
    create_file(
        os.sep.join([name, '__init__.py']),
        CONTENT['init'].format(project=name)
    )

    # runserver:
    create_file(
        'run_' + name + '.py',
        CONTENT['run'].format(project=name)
    )


def new_project(name):
    create_scaffold(name)
    shutil.copy(CONTENT_FILES['index'], os.sep.join([name, VIEWS]))
    ZipFile(CONTENT_FILES['bootstrap']).extractall(os.sep.join([name, STATIC]))
    shutil.copy(CONTENT_FILES['jquery'], os.sep.join([name, STATIC, 'js']))


def show_help():
    help_text = """\
Usage: bottle-mvc-bootstrap [PROJECT_NAME]
Creates a scaffold for a mvc bottle project with bootstrap.

Arguments:
    -h, --help        shows this help and exits"""
    print(help_text)

if __name__ == '__main__':
    from sys import argv as args

    help = {
        '-h': show_help,
        '--help': show_help
    }

    if len(args) == 2 and args[1] not in help.keys():
        new_project(args[1])
    else:
        help['-h']()

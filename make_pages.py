#!/usr/bin/env python
import os, os.path, shutil, codecs, sys

import jinja2

TARGET = 'to-deploy/'

pages = [ {
    'filename': 'index.html',
    'context':  {
        'active_tab': '/',
    }
} ]

def main():
    here = os.path.dirname(__file__)
    deploy_target = os.path.join(here, TARGET)
    loader = jinja2.FileSystemLoader(os.path.join(here, 'templates'))
    templates = jinja2.Environment(loader=loader)

    if os.path.exists(deploy_target):
        shutil.rmtree(deploy_target)
    os.makedirs(deploy_target)
    shutil.copytree(os.path.join(here, 'static'), os.path.join(deploy_target, 'static'))

    for page in pages:
        tem = templates.get_template(page['filename'])
        ctx = page['context']
        if page['filename'] == 'index.html':
            target = os.path.join(deploy_target)
        else:
            os.makedirs(os.path.join(deploy_target, page['route']))
            target = os.path.join(deploy_target, page['route'])
        with codecs.open(os.path.join(target, 'index.html'), 'w') as out:
            out.write(tem.render(**ctx))


if __name__ == '__main__':
    main()

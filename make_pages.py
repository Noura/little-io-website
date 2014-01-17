#!/usr/bin/env python
import os, os.path, shutil, codecs, sys

import jinja2

TARGET = 'to-deploy/'

pages = [
  {
    'template': 'index.html',
    'path': '',
    'tabname': 'Little LFO',
  },
  {
    'template': 'termite.html',
    'path': 'termite',
    'tabname': 'Cursynth',
  },
  {
    'template': 'cursynth.html',
    'path': 'cursynth',
    'tabname': 'Cursynth',
  },
]

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
    tem = templates.get_template(page['template'])
    ctx = { 'pages': pages , 'current_page': page }
    out_dir = os.path.join(deploy_target, page['path'])
    if page['path']:
      os.makedirs(out_dir)
    with codecs.open(os.path.join(out_dir, 'index.html'), 'w') as out:
      out.write(tem.render(**ctx))

if __name__ == '__main__':
  main()

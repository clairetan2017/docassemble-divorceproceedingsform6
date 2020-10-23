import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.divorceproceedingsform6',
      version='0.0.1',
      description=('A docassemble extension to generate a draft form 6 statement of claim required to file a divorce proceedings.'),
      long_description="# Divorce Proceedings - Draft Form 6 \r\nA docassemble package for clients and lawyers to obtain a draft form 6 which includes most of the basic information required before uncontested divorce proceedings can commence. \r\n\r\nRefer to [this link](https://www-familyjusticecourts-gov-sg-admin.cwp.sg/docs/default-source/resources/forms/divorce/form006_soc_divorcejudsep.docx?sfvrsn=66249082_2) is a template word document of Form 6 for which the client's information will be inputted. \r\n",
      long_description_content_type='text/markdown',
      author='Brenda Khoo Yu Qing, Chua Su Ann, Claire Tan Su Yin',
      author_email='claire.tan.2017@law.smu.edu.sg',
      license='The MIT License (MIT)',
      url='https://guided.page',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/divorceproceedingsform6/', package='docassemble.divorceproceedingsform6'),
     )


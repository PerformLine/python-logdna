import setuptools
setuptools.setup(
  name = 'logdna',
  packages = ['logdna'],
  version = '1.2.9.1',
  description = 'A python package for sending logs to LogDNA',
  author = 'Answerbook Inc.',
  author_email = 'help@logdna.com',
  maintainer = 'Gary Hetzel',
  maintainer_email = 'gary@performline.com',
  url = 'https://github.com/PerformLine/python-logdna',
  keywords = ['logdna', 'logging', 'logs', 'python', 'logdna.com', 'logger'],
  install_requires=[
    'requests',
  ],
  classifiers = [],
)

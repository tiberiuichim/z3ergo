from setuptools import setup, find_packages

setup(name='LearningJourney',

      # Fill in project info below
      version='0.1',
      description="",
      long_description="",
      keywords='',
      author='',
      author_email='',
      url='',
      license='',
      # Get more from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=['Programming Language :: Python',
                   'Environment :: Web Environment',
                   'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
                   'Framework :: Zope3',
                   ],

      packages=find_packages('src'),
      package_dir = {'': 'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'ZODB3',
                        'ZConfig',
                        'zdaemon',
                        'zope.publisher',
                        'zope.traversing',
                        'zope.app.wsgi>=3.4.0',
                        'zope.app.appsetup',
                        'zope.app.zcmlfiles',
                        # The following packages aren't needed from the
                        # beginning, but end up being used in most apps
                        'zope.annotation',
                        'zope.copypastemove',
                        'zope.formlib',
                        'zope.i18n',
                        'zope.app.authentication',
                        'zope.app.session',
                        'zope.app.intid',
                        'zope.app.keyreference',
                        'zope.app.catalog',
                        # The following packages are needed for functional
                        # tests only
                        'zope.testing',
                        'zope.app.testing',
                        'zope.app.securitypolicy',
                        
                        #custom dependencies
                        "zope.sendmail",
                        "z3c.layer.minimal",
                        "zope.server"
                        ],
      entry_points = """
      [console_scripts]
      learningjourney-debug = learningjourney.startup:interactive_debug_prompt
      learningjourney-ctl = learningjourney.startup:zdaemon_controller
      [paste.app_factory]
      main = learningjourney.startup:application_factory
      [colective.recipe.sphinxbuilder]
      default = learningjourney.docs
      """,
      )

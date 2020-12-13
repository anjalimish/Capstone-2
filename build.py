from pybuilder.core import use_plugin, init, Author

use_plugin('filter_resources')

use_plugin('python.core')
use_plugin('python.coverage')
use_plugin('python.install_dependencies')


name = 'capstone 2'
authors = [Author('Anjali Mishra', 'anjalimish6@gmail.com')]
          
license = 'Apache License, Version 2.0'
summary = 'Lane detection application for flask.'
url = 'https://github.com/anjalimish/Capstone-2'
version = '0.1.2'


default_task = ['install_dependencies', 'analyze', 'publish']


@init
def set_properties (project):
    project.set_property("coverage_exceptions", ['run',])
    project.build_depends_on('coverage')
    project.build_depends_on('pyassert')     
    project.depends_on('flask')    
    project.set_property('coverage_break_build', False)
    project.get_property('filter_resources_glob').append('./test_app.py')
    project.get_property('filter_resources_glob').append('./test_app1.py')

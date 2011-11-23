import datetime
from setuptools import setup
from sphinx.setup_command import BuildDoc

cmdclass={}

class local_BuildDoc(BuildDoc):
    def run(self):
        for builder in ['html', 'man']:
            self.builder = builder
            self.finalize_options()
            BuildDoc.run(self)
cmdclass['build_sphinx'] = local_BuildDoc

setup(name='openstack-qa',
      version="%d.%02d" % (datetime.datetime.now().year, datetime.datetime.now().month), 
      description="OpenStack Quality Assurance and Scripts",
      author="OpenStack QA Team",
      author_email="openstack-qa@lists.launchpad.net",
      url="http://launchpad.net/openstack-qa",
      cmdclass=cmdclass)

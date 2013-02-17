try:
    from allink_essentials.fabfiles.nexa_class_fabfile import *
    from allink_essentials.fabfiles.nexa_class_fabfile import _setup_path
except ImportError:
    import subprocess

    def update_local_requirements():
        """installs local requirements"""
        subprocess.call(["pip", "install", "--requirement", "REQUIREMENTS_LOCAL"])
else:
    env.project_python = 'biblio'


def production():
    _setup_path('production')

from hydra.core.config_search_path import ConfigSearchPath
from hydra.plugins.search_path_plugin import SearchPathPlugin

class {{cookiecutter.package_name}}SearchPath(SearchPathPlugin):
    def manipulate_search_path(self, search_path: ConfigSearchPath) -> None:
        search_path.append(
            provider="{{cookiecutter.package_name}}-searchpath-plugin",
            path="pkg://{{cookiecutter.package_name}}.config"
        )

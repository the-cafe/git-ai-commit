import requests
import pkg_resources

from ai_commit_msg.utils.logger import Logger

PACKAGE_NAME = "git-ai-commit"

class PipService:
    @staticmethod
    def get_latest_version(package_name: str = PACKAGE_NAME) -> str:
      try:
        url = f"https://pypi.org/pypi/{package_name}/json"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data['info']['version']
      except requests.exceptions.RequestException as e:
        return None

    @staticmethod
    def get_version():
      return pkg_resources.get_distribution(PACKAGE_NAME).version

    @staticmethod
    def version_is_older(current_version: str, latest_version: str) -> bool:
        current_version_parts = list(map(int, current_version.split('.')))
        latest_version_parts = list(map(int, latest_version.split('.')))
        return current_version_parts < latest_version_parts

    @staticmethod
    def display_outdated_version_message():
        current_version = PipService.get_version()
        latest_version = PipService.get_latest_version()

        if current_version and latest_version:
            is_outdated = PipService.version_is_older(current_version, latest_version)
        else:
            is_outdated = False

        if is_outdated:
          # print a warning banner using ANSI escape codes:
          # \033[43m sets the background color to yellow
          # \033[30m sets the text color to black
          # \033[0m resets all formatting
          # \033[33m sets the text color to yellow for the second line
            print(f"\033[43m\033[30m New version of {PACKAGE_NAME} available \033[0m")
            print(f"\033[33m Run 'pip install --upgrade {PACKAGE_NAME}' to update to version {latest_version}\033[0m")
            print()

import requests
import urllib3


class CyberManager:
    config_org_name = "pgmfernandes"
    config_repo_name = "config-files-examples"
    config_branch_name = "main"

    def __init__(self, github_auth):
        self.session = requests.Session()
        self.session.verify = False
        self.session.headers.update({
            'Authorization': f"Bearer {github_auth}",
            "Content-Type": "application/json",
            'Accept': "application/vnd.github+json"
        })
        urllib3.disable_warnings()

    def get_config(self, owner_and_repo_name):
        url = f"https://api.github.com/repos/{CyberManager.config_org_name}/{CyberManager.config_repo_name}/contents/{owner_and_repo_name}.json"
        print(f"URL: {url}")
        response = self.session.get(url)
        print(f"Response: {response.status_code}")
        if response.status_code == 200:
            config = response.json()
            return config
        return None

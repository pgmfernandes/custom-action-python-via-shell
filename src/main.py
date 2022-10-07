import os
from cyberconfig import *

auth = os.environ['GH_TOKEN']
config_manager = CyberManager(github_auth=auth)
github_repository = os.environ['GITHUB_REPOSITORY']
print(f"[{github_repository}] Busca de arquivo específico de configuração")
config = config_manager.get_config(owner_and_repo_name=github_repository)
print(f"[{github_repository}]", config)

github_repository = "test-" + github_repository
print(f"::set-output name=dockerfiles::{github_repository}")
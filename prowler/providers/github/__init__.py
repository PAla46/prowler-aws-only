from dataclasses import dataclass
from typing import Any, Optional

@dataclass
class GithubAppIdentityInfo:
    installation_id: str = ""
    app_id: str = ""
    client_id: str = ""
    name: str = ""

@dataclass
class GithubIdentityInfo:
    actor: str = ""
    org: str = ""
    repo: str = ""
    repository_url: str = ""
    identity: str = ""

@dataclass
class GithubOutputOptions:
    output_options: bool = False
    verbose: bool = False
    output_directory: str = "./"
    output_filename: str = ""
    outputs: list = []

def get_provider_credentials(provider: Any) ->Any:
    return None

def get_provider_session(provider: Any) -> Any:
    return None
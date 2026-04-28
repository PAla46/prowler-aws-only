from dataclasses import dataclass

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
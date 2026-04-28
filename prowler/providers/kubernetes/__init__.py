from dataclasses import dataclass
from typing import Any, Optional

@dataclass
class KubernetesIdentityInfo:
    context: str = ""
    cluster: str = ""
    namespace: str = ""

@dataclass
class KubernetesOutputOptions:
    output_options: bool = False
    verbose: bool = False
    output_directory: str = "./"
    output_filename: str = ""
    outputs: list = []

def get_provider_credentials(provider: Any) ->Any:
    return None

def get_provider_session(provider: Any) -> Any:
    return None
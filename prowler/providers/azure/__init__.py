from dataclasses import dataclass
from typing import Any, Optional

@dataclass
class AzureIdentityInfo:
    identity_id: str = ""
    identity_type: str = ""
    tenant_id: str = ""
    domain: str = ""

@dataclass
class AzureOutputOptions:
    output_options: bool = False
    verbose: bool = False
    output_directory: str = "./"
    output_filename: str = ""
    outputs: list = []

def get_provider_credentials(provider: Any) ->Any:
    return None

def get_provider_session(provider: Any) -> Any:
    return None
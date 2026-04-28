from dataclasses import dataclass
from typing import Any, Optional

@dataclass
class AlibabaCloudIdentityInfo:
    account_id: str = ""
    identity_id: str = ""
    partition: str = ""
    region: str = ""

@dataclass
class AlibabaCloudOutputOptions:
    output_options: bool = False
    verbose: bool = False
    output_directory: str = "./"
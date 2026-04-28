from dataclasses import dataclass

@dataclass
class AlibabaCloudOutputOptions:
    output_options: bool = False
    verbose: bool = False
    output_directory: str = "./"
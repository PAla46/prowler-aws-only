from dataclasses import dataclass

@dataclass
class CloudflareOutputOptions:
    output_options: bool = False
    verbose: bool = False
    output_directory: str = "./"

@dataclass
class GCPOutputOptions:
    output_options: bool = False
    verbose: bool = False
    output_directory: str = "./"

@dataclass
class GithubOutputOptions:
    output_options: bool = False
    verbose: bool = False
    output_directory: str = "./"

@dataclass
class GoogleWorkspaceOutputOptions:
    output_options: bool = False
    verbose: bool = False
    output_directory: str = "./"

@dataclass
class IACOutputOptions:
    output_options: bool = False
    verbose: bool = False
    output_directory: str = "./"

@dataclass
class ImageOutputOptions:
    output_options: bool = False
    verbose: bool = False
    output_directory: str = "./"

@dataclass
class KubernetesOutputOptions:
    output_options: bool = False
    verbose: bool = False
    output_directory: str = "./"

@dataclass
class LLMOutputOptions:
    output_options: bool = False
    verbose: bool = False
    output_directory: str = "./"

@dataclass
class M365OutputOptions:
    output_options: bool = False
    verbose: bool = False
    output_directory: str = "./"

@dataclass
class MongoDBAtlasOutputOptions:
    output_options: bool = False
    verbose: bool = False
    output_directory: str = "./"

@dataclass
class NHNOutputOptions:
    output_options: bool = False
    verbose: bool = False
    output_directory: str = "./"

@dataclass
class OpenStackOutputOptions:
    output_options: bool = False
    verbose: bool = False
    output_directory: str = "./"

@dataclass
class OCIOutputOptions:
    output_options: bool = False
    verbose: bool = False
    output_directory: str = "./"

@dataclass
class VercelOutputOptions:
    output_options: bool = False
    verbose: bool = False
    output_directory: str = "./"
from dataclasses import dataclass

@dataclass
class AlibabaCloudOutputOptions:
    output_options: bool = False
    verbose: bool = False

@dataclass
class MongoDBAtlasOutputOptions:
    output_options: bool = False
    verbose: bool = False

@dataclass
class NHNOutputOptions:
    output_options: bool = False
    verbose: bool = False

@dataclass
class OpenStackOutputOptions:
    output_options: bool = False
    verbose: bool = False

@dataclass
class OCIOutputOptions:
    output_options: bool = False
    verbose: bool = False

@dataclass
class VercelOutputOptions:
    output_options: bool = False
    verbose: bool = False
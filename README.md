# Prowler AWS

AWS-only security auditing tool, stripped from Prowler for CloudShell deployment.

## Installation

```bash
pip install -e .
```

## Usage

```bash
# Run all AWS checks
python -m prowler

# Run specific service
python -m prowler -s iam

# Run specific check
python -m prowler -f iam_root_mfa_enabled

# Output formats
python -m prowler -M json csv html
```

## Requirements

- Python 3.10+
- boto3 (pre-installed in CloudShell)

## Based on Prowler

This is an AWS-only version of [Prowler](https://github.com/prowler-cloud/prowler), designed for environments where only AWS checks are needed.

License: Apache-2.0
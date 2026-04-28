# Prowler AWS

AWS-only security auditing tool (stripped from Prowler) for CloudShell.

## Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Install in development mode (optional)
pip install -e .
```

## Usage

```bash
# Run all AWS checks
python -m prowler aws

# Run specific service
python -m prowler aws -s iam

# Run with output
python -m prowler aws -M json csv html

# List available checks
python -m prowler aws --list-checks
```

## Requirements

- Python 3.9+ (tested in CloudShell)
- boto3 (pre-installed in CloudShell)

All dependencies are listed in requirements.txt
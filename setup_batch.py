"""Setup for AWS Batch

This file contains the python code to setup AWS batch compute environment,
job queue and job definition.

TODO IMPORTANT:
Implement
Convert this to a AWS Cloudformation template
"""

import boto3
from dotenv import load_dotenv

# Import environment variables from .env
load_dotenv()


def create_compute_environment():
    pass


def create_job_queue():
    pass


def create_job_definition():
    pass


if __name__ == "__main__":
    # Create the compute environment
    create_compute_environment()

    # Create the job queue
    create_job_queue()

    # Create the job definition
    create_job_definition

"""The entrypoint for the script.

The main steps for running a microservice in python on AWS are as follows:

[AWS Batch]
- Create a compute environment
- Create a job queue
- Create a job definition

[AWS ECS]
- Create a cluster
- Create a task definition

[Code]
- Install dependencies
- Write code logic for the microservice
- Upload / Dockerize the code to S3 / ECR

[Usage]
- Run a task using the task definition created, with command overrides for the
  input arguments
"""

import argparse


def main():
    # Create an argument parser
    parser = argparse.ArgumentParser(
        description="Print the arguments passed to the script as a single string"
    )

    # Add the arguments to the parser
    parser.add_argument("args", nargs="*", type=str, help="Arguments to be printed")

    # Parse the arguments
    args = parser.parse_args()

    # Print the arguments
    print(" ".join(args.args))


if __name__ == "__main__":
    main()

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

"""
Create an AWS Batch Job Definition:

Go to the AWS Batch console.

Create a new job definition.

Set the image to the one you pushed to Amazon ECR.

Specify the command as python microservice.py.

Save the job definition.

Submit a Batch Job:

Go to the AWS Batch console.

Create a new job queue and associate it with the job definition you created.

Submit a job with the necessary parameters, such as the input argument.

Monitor the job's progress in the AWS Batch console.
"""

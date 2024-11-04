#!/usr/bin/env python3
import sys


def validate_commit_message(commit_msg_file):
    try:
        with open(commit_msg_file, "r") as file:
            commit_msg = file.read().strip()
    except Exception as e:
        print(f"Error: Unable to read commit message file: {e}")
        sys.exit(1)

    if commit_msg[0] == "#":
        print("Error: Empty commit")
        sys.exit(1)

    # Check if the message starts with a capital letter
    if not commit_msg[0].isupper():
        print("Error: Commit message must start with a capital letter.")
        sys.exit(1)

    # Check if the message ends with a period
    if commit_msg.endswith("."):
        print("Error: Commit message must not end with a period.")
        sys.exit(1)

    # If both checks pass, exit successfully
    sys.exit(0)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: Commit message file not provided.")
        sys.exit(1)

    commit_msg_file = sys.argv[1]
    validate_commit_message(commit_msg_file)

import argparse

from file_system import FileSystem # type: ignore

def main():
    # Create the ArgumentParser object
    parser = argparse.ArgumentParser(prog="imfs", description="An in memory file system.")
    # Add a positional argument
    parser.add_argument("name", help="Your name")
    
    # Parse the arguments
    args = parser.parse_args()



    # Use the arguments
    print(f"Hello, {args.name}!")


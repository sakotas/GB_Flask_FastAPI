import argparse
from reader import URLFileReader

class CommandLineParser:
    """Parses command line arguments for URL input."""

    @classmethod
    def parse_args(cls) -> list:
        parser = argparse.ArgumentParser(description="Process a list of image URLs.")
        parser.add_argument('--urls', type=str, help="Comma-separated URLs.")
        parser.add_argument('--file', type=str, help="File containing URLs, one per line.")

        args = parser.parse_args()
        urls = []

        if args.urls:
            urls += [url.strip() for url in args.urls.split(',')]
        if args.file:
            urls += URLFileReader.read(args.file)

        return urls

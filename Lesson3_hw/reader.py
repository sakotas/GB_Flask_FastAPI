class URLFileReader:
    """Reads URLs from a given file, returning them as a list."""

    @classmethod
    def read_urls(cls, filepath) -> list:
        with open(filepath, 'r') as file:
            urls = file.read().splitlines()
        return urls

    @staticmethod
    def read(file_path) -> list:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]

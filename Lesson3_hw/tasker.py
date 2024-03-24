from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import asyncio
from time import time
from loader import ImageDownloader

class ImageTaskHandler:
    """
    Manages download tasks for images using different concurrency models: threading, multiprocessing, and async.
    """

    @staticmethod
    def download_with_threads(urls: list, save_dir: str) -> None:
        start = time()
        with ThreadPoolExecutor() as executor:
            executor.map(ImageDownloader.download_image, urls, [save_dir] * len(urls))
        print(f'Threaded download completed in {time() - start:.2f} seconds.')

    @staticmethod
    def download_with_processes(urls: list, save_dir: str) -> None:
        start = time()
        with ProcessPoolExecutor() as executor:
            executor.map(ImageDownloader.download_image, urls, [save_dir] * len(urls))
        print(f'Process-based download completed in {time() - start:.2f} seconds.')

    @staticmethod
    async def download_async(urls: list, save_dir: str) -> None:
        start = time()
        await asyncio.gather(*(ImageDownloader.async_download_image(url, save_dir) for url in urls))
        print(f'Async download completed in {time() - start:.2f} seconds.')


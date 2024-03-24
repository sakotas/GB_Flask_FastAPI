import os
import aiohttp
import requests
from time import time

class ImageDownloader:
    """
    Handles the downloading of images from URLs and saving them to a specified directory.
    """

    @staticmethod
    def download_image(url: str, save_dir: str = './downloaded_images') -> None:
        start_time = time()

        if '?' in url:
            url = url.split('?')[0]

        file_name = url.split('/')[-1]
        if not os.path.splitext(file_name)[1]:
            file_name += '.jpg'

        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        full_path = os.path.join(save_dir, file_name)

        response = requests.get(url)
        with open(full_path, 'wb') as file:
            file.write(response.content)

        print(f'Downloaded {file_name} in {time() - start_time:.2f} seconds.')

    @staticmethod
    async def async_download_image(url: str, save_dir: str = './downloaded_images_async') -> None:
        start_time = time()

        if '?' in url:
            url = url.split('?')[0]

        file_name = url.split('/')[-1]
        if not os.path.splitext(file_name)[1]:
            file_name += '.jpg'

        full_path = os.path.join(save_dir, file_name)
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                content = await response.read()

                with open(full_path, 'wb') as file:
                    file.write(content)

        print(f'Asynchronously downloaded {file_name} in {time() - start_time:.2f} seconds.')

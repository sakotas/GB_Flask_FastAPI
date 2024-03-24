# Задание
# Написать программу, которая скачивает изображения с заданных URL-адресов и сохраняет их на диск.
# Каждое изображение должно сохраняться в отдельном файле, название которого соответствует названию изображения
# в URL-адресе.
# Например, URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
# — Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы.
# — Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.
# — Программа должна выводить в консоль информацию о времени скачивания каждого изображения
# и общем времени выполнения программы.
import asyncio

from tasker import ImageTaskHandler
from parser import CommandLineParser

if __name__ == "__main__":
    urls = CommandLineParser.parse_args()
    ImageTaskHandler.download_with_threads(urls, './images_threaded')
    ImageTaskHandler.download_with_processes(urls, './images_multiprocessed')
    asyncio.run(ImageTaskHandler.download_async(urls, './async_downloads'))

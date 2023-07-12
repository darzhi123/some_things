import requests
from bs4 import BeautifulSoup
import re
import sys

def get_text_from_chapter(url: str, way: int = 0):
    """Данная функция создает файл .txt в папке со скриптом и записывает в него текст с главы."""
    url = url  # input() # ссылка на главу
    answer = requests.get(url=url)
    novel_name = re.search('(?<=novel\/).+(?=\/\d+)', answer.url).group().title().replace("-", " ")
    number_chapter = re.findall(r"\d?\d", url)[0]
    status_code_site = answer.status_code  # 200
    bs = BeautifulSoup(answer.text, "lxml")
    text1 = bs.find("div", "text-left")
    work_text = text1.text.split("\n")
    with open(f"D:\Program Files\PyCharm Proj\Parsing\{novel_name}_chapter_{number_chapter}.txt", "w", encoding="utf-8") as file:
        for item in work_text:
            item = re.sub(" ", "", item)
            file.write(item)
            file.write("\n")

argument = sys.argv
way = 0

if __name__ == "__main__":
    get_text_from_chapter(argument[1], way)
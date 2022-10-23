import requests
import lxml.html
from lxml import etree
import lxml


def get_titles(html_text):
    tree = lxml.html.document_fromstring(html_text)
    text_titles = tree.xpath("//*[@class='tm-article-snippet']/h2/a/span/text()")
    text_contents = tree.xpath(
        "//*[@class='article-formatted-body article-formatted-body article-formatted-body_version-1']/br/text()")
    return text_titles, text_contents


html_text = requests.get("https://habr.com/ru/feed/")
if html_text.status_code == 200:
    text_title, text_content = get_titles(html_text.text)
    # for i, t in enumerate(text_title):
    #     text = """
    #     ========================
    #     Заголовок ---- {title}
    #     Контент   ---- {content}
    #     =========================""".format(title=t, content=text_content[i])
    # print(text)
    print(text_title, text_content)

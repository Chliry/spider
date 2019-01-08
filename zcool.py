import os
import time
import requests
from lxml import etree


def message(url1):
    """
    获取链接
    :param url:链接
    :return: [lianjie]
    """
    html1 = requests.get(url1).text
    html2 = etree.HTML(html1)
    result1 = html2.xpath('//*[@id="body"]/main/div[3]/div/div/div[1]/a/@href')
    result2 = html2.xpath('//*[@id="body"]/main/div[3]/div/div/div[2]/p[1]/a/text()')
    return result1, result2


def picture_message(picture_url):
    """
    图片链接
    :param picture_url: []
    :return: []
    """
    list1 = []
    for i in picture_url:
        html1 = requests.get(i).text
        html2 = etree.HTML(html1)
        result1 = html2.xpath('//*[@id="body"]/main/div/div[@class="work-details-content"]/div/div/div[@class="work-show-box"]/div/img/@src')

        list1.append(result1)

    return list1


def picture(things, names):
    """
    下载图片
    :param things: [[ ]]
    :return: None
    """
    for i in range(len(names)):
        try:
            if os.path.exists(f'D:/zcool/{names[i]}'):
                print(f"{names[i]}-文件夹已存在")
            else:
                os.mkdir(f'D:/zcool/{names[i]}')
                print(f"创建{names[i]}-文件夹成功!")
            os.chdir(f'D:/zcool/{names[i]}')
        except Exception as e:
            print(e)
            if os.path.exists(f'D:/zcool/{i}'):
                print(f"{i}-文件夹已存在")
            else:
                os.mkdir(f'D:/zcool/{i}')
            os.chdir(f'D:/zcool/{i}')
            print(f"创建{i}-文件夹成功!")

        for n1, n2 in enumerate(things[i]):
            resp = requests.get(n2)
            img_byts = resp.content
            print(f"准备保存第{n1+1}张...")

            with open(f'第{n1+1}张.jpg', 'wb') as file:
                file.write(img_byts)
                print(f"第{n1+1}张保存成功!")
                time.sleep(1)


if __name__ == "__main__":
    list1, list2 = message('https://www.zcool.com.cn/')
    # print(len(list2), len(list1))
    list3 = picture_message(list1)
    # print(len(list2), len(list3))
    # print(list, list2)
    picture(list3, list2)
    # print(picture_message(list1))

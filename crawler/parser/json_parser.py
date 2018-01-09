import json
from crawler.beans import result_bean


class JsonParser(object):
    # 将json字符创解析为一个对象
    def json_to_object(self, json_content):
        if json_content is None:
            print('parse error!json is None!')
            return None
        print('json', str(json_content))
        return json.loads(str(json_content))

    # 从JSON构成的对象中提取出文章的title、link、collectionCount等数据，并将其封装成一个Bean对象，最后将这些对象添加到结果列表中
    def build_bean_from_json(self, json_collection, baseline):
        if json_collection is None:
            print('build bean from json error! json_collection is None!')
        list = json_collection['d'] # 文章的列表
        result_list = []    # 结果的列表
        for element in list:
            starCount = element['collectionCount']  # 获得的收藏数，即获得的赞数
            if int(starCount) > baseline:   # 如果收藏数超过baseline，则勾结结果对象并添加到结果列表中
                title = element['title']
                link = element['originalUrl']
                result = result_bean.ResultBean(title, link, starCount)
                result_list.append(result)      # 添加到结果列表中
                print(title, link, starCount)
        return result_list

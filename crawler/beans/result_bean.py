# 将每条文章保存为一个bean，其中包含：题目、链接、获得的赞数 属性
class ResultBean(object):
    def __init__(self, title, link, starCount=10):
        self.title = title
        self.link = link
        self.starCount = starCount

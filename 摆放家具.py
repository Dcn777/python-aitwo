class jiaju:
    """家具类"""

    def __init__(self, name, area):
        self.name = name  # 名字
        self.area = area  # 占地面积

    def __str__(self):
        return "%s占地%d平米" % (self.name, self.area)


class house:
    """房子类"""

    def __init__(self, huxing, xjm):
        self.huxing = huxing  # 户型
        self.xjm = xjm  # 总面积
        self.symj = xjm  # 剩余面积
        self.jiajulb = []  # 家具列表

    def __str__(self):
        return ">>>>>户型：%s\t总面积：%.2f平米\t剩余面积：%.2f平米\t家具名称列表：%s" % (self.huxing, self.xjm, self.symj, self.jiajulb)

    def add(self, jiaju):
        """添加家具列表"""
        if self.symj > jiaju.area:  # 对象的area变量
            print(">>>已添加%s" % jiaju)
            self.jiajulb.append(jiaju.name)  # 将家具添加到家具列表里面
            self.symj -= jiaju.area  # 添加后将剩余面积再减去添加的家具面积
        else:
            print("房子不能添加家具了")


"""主程序"""
while True:
    print("***************摆放家具小程序***************")
    jj = int(input("请告诉我要创建几个家具："))
    """循环对象赋值"""
    jju = 1  # 计数器
    libiao = []  # 家具对象列表
    while jju <= jj:
        a = input("请输入第%d个家具名称：" % jju)
        b = float(input("请输入第%d个家具面积：" % jju))
        libiao.insert(jju, jiaju(a, b))
        jju += 1

    """创建房子对象"""
    fz_hx = input("请输入房子户型：")
    fz_zmj = float(input("请输入房子总面积："))
    fz = house(fz_hx, fz_zmj)

    """输出家具列表"""
    print("--序号---家具-----占地面积------")
    jsq = 0  # 计数器
    while jsq < len(libiao):
        print("\t%d\t%s\t\t%.2f平米" % ((jsq + 1), libiao[jsq].name, libiao[jsq].area))
        jsq += 1
    print("-" * 24)

    """选择要摆放的家具"""
    while True:
        bfjj = int(input("请选择家具序号："))
        fz.add(libiao[bfjj - 1])
        jx = input("是否继续摆放家具？（y继续/任意字符退出）：")
        if jx != "y":
            break

    """输出房子"""
    print(fz)

    """判断程序是否继续"""
    cxjx = input("是否继续（y继续/任意字符退出）：")
    if cxjx != "y":
        print("感谢使用摆放家具小程序【小黄python版】！")
        break

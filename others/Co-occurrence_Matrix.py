# encoding:utf-8
__author__ = 'shiliang'
__date__ = '2019/4/4 9:55'


def get_Co_authors(filePath):
    '''
    读取csv文件获取作者信息并存储到列表中
    :param filePath: csv文件路径
    :return co_authors_list: 一个包含所有作者的列表
    '''
    # 设置编码为utf-8-sig防止首部\ufeff的出现,它是windows系统自带的BOM,用于区分大端和小端UTF-16编码
    with open(filePath, 'r', encoding='utf-8-sig') as f:
        text = f.read()
        co_authors_list = text.split('\n')  # 分割数据中的换行符'\n'两边的数据
        co_authors_list.remove('')          # 删除列表结尾的空字符
        return co_authors_list

def str2csv(filePath, s):
    '''
    将字符串写入到本地csv文件中
    :param filePath: csv文件路径
    :param s: 待写入字符串(逗号分隔格式)
    '''
    with open(filePath, 'w', encoding='utf-8') as f:
        f.write(s)
    print('写入文件成功,请在'+filePath+'中查看')

def sortDictValue(dict, is_reverse):
    '''
    将字典按照value排序
    :param dict: 待排序的字典
    :param is_reverse: 是否按照倒序排序
    :return s: 符合csv逗号分隔格式的字符串
    '''
    # 对字典的值进行倒序排序,items()将字典的每个键值对转化为一个元组,key输入的是函数,item[1]表示元组的第二个元素,reverse为真表示倒序
    tups = sorted(dict.items(), key=lambda item: item[1], reverse=is_reverse)
    s = ''
    for tup in tups:  # 合并成csv需要的逗号分隔格式
        s = s + tup[0] + ',' + str(tup[1]) + '\n'
    return s

def build_matrix(co_authors_list, is_reverse):
    '''
    根据共同作者列表,构建共现矩阵(存储到字典中),并将该字典按照权值排序
    :param co_authors_list: 共同作者列表
    :param is_reverse: 排序是否倒序
    :return node_str: 三元组形式的节点字符串(且符合csv逗号分隔格式)
    :return edge_str: 三元组形式的边字符串(且符合csv逗号分隔格式)
    '''
    node_dict = {}  # 节点字典,包含节点名+节点权值(频数)
    edge_dict = {}  # 边字典,包含起点+目标点+边权值(频数)
    # 第1层循环,遍历整表的每行作者信息
    for row_authors in co_authors_list:
        row_authors_list = row_authors.split(',') # 依据','分割每行所有作者,存储到列表中
        # 第2层循环,遍历当前行所有作者中每个作者信息
        for index, pre_au in enumerate(row_authors_list): # 使用enumerate()以获取遍历次数index
            # 统计单个作者出现的频次
            if pre_au not in node_dict:
                node_dict[pre_au] = 1
            else:
                node_dict[pre_au] += 1
            # 若遍历到倒数第一个元素,则无需记录关系,结束循环即可
            if pre_au == row_authors_list[-1]:
                break
            connect_list = row_authors_list[index+1:]
            # 第3层循环,遍历当前行该作者后面所有的合作者,以统计两两作者合作的频次
            for next_au in connect_list:
                A, B = pre_au, next_au
                # 固定两两作者的顺序
                # 格式化为逗号分隔A,B形式,作为字典的键
                # 若该关系不在字典中,则初始化为1,表示作者间的合作次数
                if key noif A > B:
                    A, B = B, A
                key = A+','+B  t in edge_dict:
                    edge_dict[key] = 1
                else:
                    edge_dict[key] += 1
    # 对得到的字典按照value进行排序
    node_str = sortDictValue(node_dict, is_reverse)  # 节点
    edge_str = sortDictValue(edge_dict, is_reverse)   # 边
    return node_str, edge_str


if __name__ == '__main__':
    readfilePath = r'C:\Users\Administrator\Desktop\empty.csv'
    writefilePath1 = r'C:\Users\Administrator\Desktop\node.csv'
    writefilePath2 = r'C:\Users\Administrator\Desktop\edge.csv'
    # 读取csv文件获取作者信息并存储到列表中
    co_authors_list = get_Co_authors(readfilePath)
    # 根据共同作者列表, 构建共现矩阵(存储到字典中), 并将该字典按照权值排序
    node_str, edge_str = build_matrix(co_authors_list, is_reverse=True)
    print(edge_str)
    # 将字符串写入到本地csv文件中
    str2csv(writefilePath1, node_str)
    str2csv(writefilePath2, edge_str)
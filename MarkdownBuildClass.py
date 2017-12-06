# ---------------------------------
# MD文件生成                      |
# Author:  tony                   |
# Email: luffywang622@gmail.com   |
# Date:  2017/8/26                |
# Time:  15:22                    |
# ---------------------------------

class MarkDownBuild:

    table_header = '|字段名称|字段类型|允许为空|字段含义|\n| --- | --- | :---: | --- |\n'
    table_content_template = '|%s|%s|%s|%s|\n'

    def __init__(self):
        pass

    def buildMarkdown(self, table_data):
        text = '# 数据库文档\n\n'
        text += '* 共计`' + str(len(table_data)) + '`张数据表\n\n'
        # text += '<a name="返回顶部"></a>\n\n## 数据表列表\n\n'
        for table in table_data:
            text = text + '* [' + table[0][0] + '(' + table[0][1] + ')](#' + table[0][0] + '_pointer)\n\n'
        text += '\n\n## 数据表说明\n\n'
        for table in table_data:
            #text = text + '<a name="'+table[0][0]+'_pointer"></a>\n\n'
            #text = text + '## ' + table[0][0] + ' (' + table[0][1] + ')[↑](#返回顶部)\n\n'
            text = text + '### ' + table[0][1] + '  `' + table[0][0] + '`\n\n'
            text += self.table_header
            for column in table[1]:
                text = text + '|' + column[0] + '|' + column[1] + '|' + column[2] +'|' + column[3] + '|\n'
            text += '\n'
        return text
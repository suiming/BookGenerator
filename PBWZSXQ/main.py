import selectcollection
import markcollection


def deal_select_collect():
    selectcollection.deal_selected_collect('', '')

def deal_mark_collect():
    markcollection.deal_mark_collect('', '')


if __name__ == '__main__':
    # 处理精华内容
    selectcollection.deal_selected_collect('/Users/suiming/Documents/读书笔记/精华帖', '/Users/suiming/Documents/读书笔记/__精华成品')

    # 处理书籍
    markcollection.deal_marked_collect('/Users/suiming/Documents/读书笔记/bookmark', '/Users/suiming/Documents/读书笔记/__读书成品', '/Users/suiming/Documents/读书笔记/__temp')


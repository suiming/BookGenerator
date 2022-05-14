
def get_formatted_topic(topic_content):
    return remove_tag(topic_content)


def remove_tag(write_content):
    remove_str1 = '<e type="hashtag" hid="88855182211542" title="%23%E5%85%B1%E8%AF%BB%E6%89%93%E5%8D%A1%23" />'
    remove_str2 = write_content.replace(remove_str1, '')
    remove_str3 = remove_str2.replace('【打卡内容】', '')

    return remove_str3


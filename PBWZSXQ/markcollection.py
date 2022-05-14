import json
import os
import filemanager
import topicformate
import re


def get_file_content(file_path, topic_dict):
    with open(file_path) as f:
        file_data = json.load(f)
        topics = file_data['resp_data']['topics']
        for topic in topics:
            topic_id = topic['topic_id']
            # 这里create_time 精度足够
            create_time = topic['create_time']
            owner = topic['talk']['owner']['name']
            owner_content = topic['talk']['text']
            time = topic['create_time']
            topic_dict[topic_id] = {
                'owner': owner,
                'owner_content': owner_content,
                'time': time
            }


def write_topics_to_file_by_owner(topic_dict, target_path, tmp_path):
    filemanager.make_path_exist(tmp_path)

    topics_array = topic_dict.values()

    new_topics_array = []
    # reverse, 这里不知道怎么调用
    for topic in topics_array:
        new_topics_array.insert(0, topic)
    for topic in new_topics_array:
        owner = topic['owner']
        owner_content = topic['owner_content']

        pattern = re.compile(r'<[^>]+>', re.S)
        result = pattern.sub('', owner_content)

        # 写文件
        topic_content = topicformate.get_formatted_topic(result)
        new_dir = os.path.join(tmp_path, owner + '.md')
        filemanager.write_content(new_dir, "\n" + '### ' + owner + ":" + topic_content)

    # 聚合
    write_to_one_file(tmp_path, target_path)


def write_to_one_file(tmp_path, target_path):
    tmp_list = []
    tmp_list = filemanager.get_file_list(tmp_path, tmp_list)
    tmp_list.sort()

    filemanager.make_path_exist(target_path)
    target_file_path = os.path.join(target_path, '读书会_聚合版.md')
    for file_path in tmp_list:
        filemanager.write_content(target_file_path, '## ' + file_path)
        with open(file_path, 'r', encoding="utf-8") as f:
            filemanager.write_content(target_file_path, "\n" + f.read())


def deal_marked_collect(path_dir, target_path, tmp_path):
    file_list = []
    file_list = filemanager.get_file_list(path_dir, file_list)
    file_list.sort()
    print('debug: 即将处理以下标签文件{}', file_list)

    # create_time - dict
    topics_dict = dict()
    for file_path in file_list:
        get_file_content(file_path, topics_dict)

    # topics_dict 包含了这个文件夹下所有的内容
    write_topics_to_file_by_owner(topics_dict, target_path, tmp_path)

    # 合并文件

    print('debug: 处理完成'.format(target_path))

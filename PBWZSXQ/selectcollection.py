import json
import os
import filemanager


# 根据不同的数据拼装
def get_file_content(file_path, topic_dict):
    with open(file_path) as f:
        file_data = json.load(f)
        topics = file_data['resp_data']['topics']
        for topic in topics:
            if topic['type'] == 'q&a':
                create_time = topic['create_time']
                topic_id = topic['topic_id']
                owner = topic['question']['owner']['name']
                owner_content = '问:' + topic['question']['text']

                answer = topic['answer']['owner']['name']
                answer_content = '\n' + answer +'答:' + topic['answer']['text']
                topic_dict[topic_id] = {
                    'owner': owner,
                    'owner_content': owner_content + answer_content,
                    'time': time
                }
            elif topic['type'] == 'talk':
                create_time = topic['create_time']
                topic_id = topic['topic_id']
                owner = topic['talk']['owner']['name']

                owner_content = topic['talk'].setdefault('text', "error")
                time = topic['create_time']
                if owner_content == 'error':
                    continue
                topic_dict[topic_id] = {
                    'owner': owner,
                    'owner_content': owner_content,
                    'time': time
                }


def write_topics_to_file_by_one(topic_dict, target_path):
    new_dir = os.path.join(target_path, '精华_聚合版.md')
    filemanager.make_path_exist(target_path)

    sorted(topic_dict, reverse=False)
    topics_array = topic_dict.values()
    new_topics_array = []
    # reverse, 这里不知道怎么调用
    for topic in topics_array:
        new_topics_array.insert(0, topic)
    for topic in new_topics_array:
        owner = topic['owner']
        owner_content = topic['owner_content']

        # 写文件
        filemanager.write_content(new_dir, "\n" + owner + ":" + owner_content)


def deal_selected_collect(path_dir, target_path):
    file_list = []
    file_list = filemanager.get_file_list(path_dir, file_list)
    file_list.sort()
    print('debug: 即将处理以下精华文件{}', file_list)

    # topic_id - dict
    topics_dict = dict()
    for file_path in file_list:
        get_file_content(file_path, topics_dict)

    # topics_dict 包含了这个文件夹下所有的内容
    write_topics_to_file_by_one(topics_dict, target_path)
    print('debug: 处理完成'.format(target_path))

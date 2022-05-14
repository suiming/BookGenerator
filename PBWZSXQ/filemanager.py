import os
import io


# 获取文件列表
def get_file_list(file_dir: object, file_list: object) -> object:
    new_dir = file_dir
    if os.path.isfile(file_dir):
        file_list.append(file_dir)
    elif os.path.isdir(file_dir):
        for file in os.listdir(file_dir):
            if not file.startswith('.'):
                new_dir = os.path.join(file_dir, file)
                get_file_list(new_dir, file_list)
    return file_list


# 往一个文件写内容
def write_content(file_path, content):
    file = io.open(file_path, 'a', encoding="utf-8")
    file.write(u"{}".format(content))


def make_path_exist(file_path):
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    else:
        try:
            os.remove(file_path)
        except OSError as error:
            print("这里报错，请手动删除文件，否则会有重复内容{}".format(error))

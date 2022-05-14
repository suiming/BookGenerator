# BookGenerator
用于处理星球抓包的json数据

## 如何使用

找到 main.py 下 selectcollection.deal_selected_collect 和 markcollection.deal_marked_collect 方法，修改入参，准备好数据。

  ```
  # 不区分人
  selectcollection.deal_selected_collect('json文件路径', '输出路径')

  # 区分人
  markcollection.deal_marked_collect('json文件路径', '输出路径', '临时路径：按人切分文件')

```

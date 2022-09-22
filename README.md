# 羊了个羊通关/刷次数方法汇总 9-22 12:00测试可用
#### 本项目仅供学习交流，严禁用于商业用途，请于24小时内删除。

羊了个羊更新后，通关的接口加了一个MatchPlayInfo，这个是根据过关时的操作加密所得，所以直接构造请求有些难度，但是应该可以复制通关后的接口数据来构造通关请求，所以我们现在的任务就是怎么进行第一次通关。
![191156597-68b504be-606a-45f4-8db9-394b03655880](https://user-images.githubusercontent.com/58501978/191182419-c6142551-7a80-4040-83f3-fb1663d3b746.jpeg)
这张图我忘记是在哪个issue下看到的了，谢谢老哥。

### 一、重写方法
重写方法我们采用修改 blockTypeData 来实现，在删除小程序后，第一次启动时，会调用 https://cat-match-static.easygame2021.com/maps/fc7c34c18e09f4b29ed75ccb52ad0225.txt 来获取第二关的关卡信息，里面就有 blockTypeData ，我们将"blockTypeData":{XXXXXXXXXXXXXXX}，重写为"blockTypeData":{}，即可实现第二关的所有块变成空白模块。（建议使用正则表达式来写重写规则，这样一段时间应该就不需要更新了）

使用Storm Sniffer重写方法在【重写规则.txt】或参考 https://zhuanlan.zhihu.com/p/564740778 或参考 Github 上其他软件的教程。

#### Storm Sniffer口令：Y 口令: SSC#7nYZc7xSLw# 复制本段文本并打开Storm Sniffer(https://t.cn/A6Xjh5bu) 
![34D410BE-9842-444E-99DF-C5170D3BE632](https://user-images.githubusercontent.com/58501978/191191784-48a4c021-f99b-4a9f-9245-834827d8e118.jpeg)

### 二、构造请求（无效）
构造请求主要用来刷关，通过第一步通关后进行抓包，我们可以获得“正常”通关下的 MatchPlayInfo，即可用来构造请求。经过测试，方法无效

### 三、构造请求2
但是我无意中发现，通关后会获取新皮肤，获取皮肤接口的接口 https://cat-match.easygame2021.com/sheep/v1/game/update_user_skin?skin=24 ，可以直接增加一次通关次数，并且排行榜可见！

具体实现方法见【main.py】
![84E0C895-6353-47D7-883E-08A3C1658425_1_102_o](https://user-images.githubusercontent.com/58501978/191184491-49a6bd09-552a-48f1-8e7a-b371a8a8043a.jpeg)

### 四、如何刷皮肤
在方法一删除小程序后，本地的皮肤数据就会被删除，把系统时间调到以前未通关的时间，返回小程序再次加入羊群即可刷皮肤了。或者参考issue中提出的办法。

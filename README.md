# 基于Django+LayUI+HBase的文献数据挖掘系统的实现

> 引言：本系统的目标是设计并实现一个基于分布式数据库HBase的文献数据挖掘系统，以帮助科研人员**分析**出相关科技前沿领域的**专家、机构等的学术影响力**。并**挖掘领域高频词**和不同**协作者之间**的**关系图谱**，如此便可达到**科研决策支持的**目的。以下将从几个方面进行简要介绍。

## 一、开发意义
科研文献是科技与学术的载体，高效的分析科研文献对科技的发展有着重要的推动作用。准确地提取出期刊会议中科研文献元数据里所隐藏的信息，可提高科研文献分析的准确度与效率。
## 二、功能架构设计
本系统的功能主要分为三个模块，分别是**数据统计分析结果展示平台**、**后台管理系统**和**数据存储平台**，其总体功能架构如图所示。

![在这里插入图片描述](https://img-blog.csdnimg.cn/20190531233632532.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1NMX1dvcmxk,size_16,color_FFFFFF,t_70)
## 三、系统实现
#### 3.1 开发环境及框架配置
考虑到系统需求，采用在**CentOS**系统上，搭建整个开发和运行环境，其中包括Hadoop分布式平台以及**HBase分布式数据库**，在**Win10**上搭建**Django框架**和**关系型数据库MySQL**等必要的开发环境。
| 环境/框架 | 名称/版本 |
|--|--|
| 操作系统 | CentOS 7.5+Win10 |
| 数据库 | **MySQL 5.7+HBase 2.1.0** |
| 数据库管理软件 | Navicat-10.1.7 |
| 主要编程语言 | Python-3.6.6 |
| Web服务器 | Nginx服务器 |
| 后端框架**Django** | 2.0.1 |
| 前端框架**LayUI** | 2.4.5 |
| 前端框架**Bootstrap** | 3.3.7 |
| 可视化图库**ECharts** | 4.2.1 |
| **Hadoop** | 3.0.3 |
| **Zookeeper** | 3.4.13 |
| **Gephi**复杂网络分析软件 | 0.9.2 |
#### 3.2 主要技术实现过程

 1. **搭建Hadoop平台**。使用**四台云主机**(CentOS7.5)搭建集群，配置好**HDFS**，**ZooKeeper**和**HBase**。
 2. **异步爬取数据**。使用Python中的`asyncio`和`aiohttp`库实现异步爬虫，从而异步爬取[AAAI人工智能会议的历年论文](https://aaai.org/ocs/index.php/AAAI/AAAI18/schedConf/presentations)元数据(包括论文**标题、摘要、作者、机构以及关键词**等数据)存储到Excel表中，并对爬取的数据进行**规则清洗**和必要的人工清洗得到**较为干净的数据**。
 3. **数据分析**。①利用**Excel函数**进行数据**去重、统计、排序**；②利用**Python构建作者数据的共现矩阵**，然后将其**三元组**数据导入至`Gephi`软件进行**复杂网络可视化**并导出`SVG`可伸缩矢量图片；③利用**LDA主题模型**对论文摘要进行主题聚类，得到**top5热门话题**；④最终将**清洗后的完整数据**以及**分析结果数据**存储至位于云端的**HBase**中。
 4. **Web系统开发**。使用`Django`+`LayUI`+`Bootstrap`开发(对于前端样式冲突问题可通过提升优先级解决)，主要功能有**注册登录、忘记密码邮箱验证、个人中心信息修改、全局检索、论文下载、数据分析结果展示**(使用`Echarts`和`Gephi`进行数据可视化)以及**词云图**（中文使用`jieba`分词，英文使用`wordcloud`分词）等。同时使用Django第三方插件`xadmin`进行**后台管理系统**的快速注册和绑定。
 5. **系统部署**。最后将系统部署到云端Nginx服务器中。
## 四、系统界面展示
#### 4.1 系统主界面展示
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190601115209619.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1NMX1dvcmxk,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190601115458161.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1NMX1dvcmxk,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190601115328489.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1NMX1dvcmxk,size_16,color_FFFFFF,t_70)
#### 4.2 用户注册登录页面
①注册页面如下：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190601113301218.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1NMX1dvcmxk,size_16,color_FFFFFF,t_70)
点击注册按钮后，系统邮箱会自动给注册用户邮箱发激活链接（如下图），当用户在个人邮箱中点击激活链接后方可登录，以此来确认注册为本人操作。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190601113334985.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1NMX1dvcmxk,size_16,color_FFFFFF,t_70)
②登录页面如下：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190601113453977.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1NMX1dvcmxk,size_16,color_FFFFFF,t_70)
③忘记密码页面如下，使用邮箱验证修改密码：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190601113555421.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1NMX1dvcmxk,size_16,color_FFFFFF,t_70)
用户在收到邮件后点击修改页面链接后，跳转到如下页面进行密码修改。点击“提交”按钮后会自动跳转到登录页面进行登录。如图为修改密码页面图。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190601113724226.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1NMX1dvcmxk,size_16,color_FFFFFF,t_70)
#### 4.3 用户个人中心
用户成功登录进入系统主页面后，可进入个人中心查看个人信息，同时可以完善或修改自己的个人信息，其中包括头像、密码、昵称、性别和地址等信息。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190601114602491.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1NMX1dvcmxk,size_16,color_FFFFFF,t_70)
#### 4.4 全局检索功能
全局检索功能主要方便用户快速查找所需信息。其中，本系统提供了“**标题**”、“**作者**”和“**机构**”三个方面的**模糊查询**服务，并对**英文关键词大小写不敏感**。如图为按论文标题查找，关键词为`Machine LEARNING`。

![在这里插入图片描述](https://img-blog.csdnimg.cn/20190601114002986.png)
#### 4.5 系统各项功能模块
###### 4.5.1 论文所属国家分布(图表基于`Echarts`实现)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190601115705494.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1NMX1dvcmxk,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190601115806687.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1NMX1dvcmxk,size_16,color_FFFFFF,t_70)
向下滑动可看到top10国家以及各个国家的具体论文发表机构分布(该表**样式**由`LayUI`提供)。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190601115902400.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1NMX1dvcmxk,size_16,color_FFFFFF,t_70)
###### 4.5.2 AAAI会议历年中稿率
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190601120257929.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1NMX1dvcmxk,size_16,color_FFFFFF,t_70)
###### 4.5.3 AAAI词云图
①动态词云图，使用[WordArt](https://wordart.com/)第三方在线工具导入。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190601120841618.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1NMX1dvcmxk,size_16,color_FFFFFF,t_70)
②静态词云图，使用Python中的`wordcloud`制作。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190601120803601.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1NMX1dvcmxk,size_16,color_FFFFFF,t_70)
###### 4.5.4 AAAI作者关系图谱
在对作者数据构建**共现矩阵**并得出其三元组存储形式后，将数据导入到`Gephi`，使用**力引导布局**绘制出如下`知识图谱`，并以`SVG`矢量可伸缩图片保存，将其导入到`HTML`中，借用开源JavaScript包`svg_Zoom_Pan`实现可无限伸缩且可平移的网页效果。([具体实现步骤见此](https://blog.csdn.net/SL_World/article/details/89106463))
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190601122342295.gif)
###### 4.5.5 AAAI会议论文主题聚类(使用LDA主题模型)
其中`top5`主题分别是：

 - **机器学习的理论和应用** 
 - **自然语言处理** 
 - **深度神经网络** 
 - **知识表现与垂直搜索** 
 - **博弈论与经济范式**

![在这里插入图片描述](https://img-blog.csdnimg.cn/20190601122512158.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1NMX1dvcmxk,size_16,color_FFFFFF,t_70)
###### 4.5.6 AAAI会议论文概览及下载页面
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190601122921945.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1NMX1dvcmxk,size_16,color_FFFFFF,t_70)
点击标题链接后可进入到论文详情页面，可看到论文标题、摘要以及作者和所属机构，同时对于已登录用户可提供PDF论文下载服务。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190601123057347.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1NMX1dvcmxk,size_16,color_FFFFFF,t_70)
###### 4.5.7 AAAI会议论文作者统计
本系统对前五年的作者、前三年以及2018年的做了统计(其中细化为**所有作者**和**第一作者**两部分)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190601123507993.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1NMX1dvcmxk,size_16,color_FFFFFF,t_70)
###### 4.5.8 AAAI会议论文机构统计
本系统同时对前五年、前三年和2018年机构做了统计，细化规则同上，此处不再赘述。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190601123818285.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1NMX1dvcmxk,size_16,color_FFFFFF,t_70)
#### 4.6 系统管理后台
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190601114732878.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1NMX1dvcmxk,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190601114819624.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1NMX1dvcmxk,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190601114908756.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1NMX1dvcmxk,size_16,color_FFFFFF,t_70)
## 五、完整代码及相关文件说明
完整代码见我的GitHub：[DataMingingPaper](https://github.com/SparksFly8/DataMingingPaper)

 1. 机构国家分布、论文接受率、论文概览、论文详情页面、词云图、作者和机构统计页面**后端代码**见：`DataMingingPaper/apps/statistic/views.py`；其**路由设置**见`DataMingingPaper/apps/statistic/urls.py`
 2. 连接远程HBase以及相关HBase表操作代码见：`DataMingingPaper/apps/statistic/connect_hbase.py`
 3. 用户登录、注册、忘记密码找回、账号激活、个人中心信息修改及头像上传和404页面配置页面**后端代码**见：`DataMingingPaper/apps/users/views.py`
 4. 用户个人信息ORM代码见：`DataMingingPaper/apps/users/models.py`
 5. `xadmin`后台管理系统代码见：`DataMingingPaper/apps/users/adminx.py`
 6. 邮件发送代码见：`DataMingingPaper/apps/utils/email_send.py`
 7. 异步爬虫代码见：`DataMingingPaper/spider/metadata_Coroutine_Spider.py`
 8. 共现矩阵构建算法见：`DataMingingPaper/others/Co-occurrence_Matrix.py`
 9. LDA主题模型算法见：`DataMingingPaper/others/LDAkeywords.py`
 10. 词云图代码见：`DataMingingPaper/others/wordcloud.py`
 11. 各个HTML页面见：`DataMingingPaper/templates/` 



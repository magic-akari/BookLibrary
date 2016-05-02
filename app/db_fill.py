# -*- coding: utf-8 -*-

from app import app, db
from app.models import User, Book, Log, Role

app_ctx = app.app_context()
app_ctx.push()
db.create_all()
Role.insert_roles()

admin = User(name=u'root', email='root@gmail.com', password='password', major='administrator',
             headline=u"临时管理员一枚", about_me=u"毕业于管理系,爱好读书,因此兼职图书馆管理员.")
user1 = User(name=u'阿卡林', email='akarin@Gmail.com', password='123456', major='Computer Science', headline=u"普通的学生")
user2 = User(name=u'test', email='test@test.com', password='123456')
user3 = User(name=u'小明', email='xiaoming@163.com', password='123456')
user4 = User(name=u'李华', email='lihua@yahoo.com', password='123456')

book1 = Book(title=u"Flask Web 开发", subtitle=u"基于Python的Web应用开发框架", author=u"Miguel Grinberg", isbn='9787115373991',
             tags_string=u"计算机,程序设计,Web开发", image='http://img3.douban.com/lpic/s27906700.jpg',
             summary=u"""
# 本书不仅适合初级Web开发人员学习阅读，更是Python程序员用来学习高级Web开发技术的优秀参考书。

* 学习Flask应用的基本结构，编写示例应用；
* 使用必备的组件，包括模板、数据库、Web表单和电子邮件支持；
* 使用包和模块构建可伸缩的大型应用；
* 实现用户认证、角色和个人资料；
* 在博客网站中重用模板、分页显示列表以及使用富文本；
* 使用基于Flask的REST式API，在智能手机、平板电脑和其他第三方客户端上实现可用功能；
* 学习运行单元测试以及提升性能；
* 将Web应用部署到生产服务器。
""")
book2 = Book(title=u"STL源码剖析", subtitle=u"庖丁解牛 恢恢乎游刃有余", author=u"侯捷", isbn='9787560926995',
             tags_string=u"计算机,程序设计,C++", image='http://img3.doubanio.com/lpic/s1092076.jpg',
             summary=u"""* 学习编程的人都知道，阅读、剖析名家代码乃是提高水平的捷径。源码之前，了无秘密。大师们的缜密思维、经验结晶、技术思路、独到风格，都原原本本体现在源码之中。
* 这本书所呈现的源码，使读者看到vector的实现、list的实现、heap的实现、deque的实现、Red Black tree的实现、hash table的实现、set/map的实现；看到各种算法（排序、查找、排列组合、数据移动与复制技术）的实现；甚至还能够看到底层的memory pool和高阶抽象的traits机制的实现。""")
book3 = Book(title=u"编译原理（原书第2版）", subtitle=u"原理、技术与工具",
             author="Alfred V. Aho / Monica S.Lam / Ravi Sethi / Jeffrey D. Ullman ", isbn="9787111251217",
             tags_string=u"计算机,编译原理", image='http://img3.douban.com/lpic/s3392161.jpg',
             summary=u"""* 本书全面、深入地探讨了编译器设计方面的重要主题，包括词法分析、语法分析、语法制导定义和语法制导翻译、运行时刻环境、目标代码生成、代码优化技术、并行性检测以及过程间分析技术，并在相关章节中给出大量的实例。与上一版相比，本书进行了全面的修订，涵盖了编译器开发方面的最新进展。每章中都提供了大量的系统及参考文献。
* 本书是编译原理课程方面的经典教材，内容丰富，适合作为高等院校计算机及相关专业本科生及研究生的编译原理课程的教材，也是广大技术人员的极佳参考读物。""")
book4 = Book(title=u"深入理解计算机系统", author="Randal E.Bryant / David O'Hallaron", isbn="9787111321330",
             tags_string=u"计算机,计算机系统", image='http://img3.douban.com/lpic/s4510534.jpg',
             summary=u"""* 本书从程序员的视角详细阐述计算机系统的本质概念，并展示这些概念如何实实在在地影响应用程序的正确性、性能和实用性。全书共12章，主要内容包括信息的表示和处理、程序的机器级表示、处理器体系结构、优化程序性能、存储器层次结构、链接、异常控制流、虚拟存储器、系统级I/O、网络编程、并发编程等。书中提供大量的例子和练习，并给出部分答案，有助于读者加深对正文所述概念和知识的理解。
* 本书的最大优点是为程序员描述计算机系统的实现细节，帮助其在大脑中构造一个层次型的计算机系统，从最底层的数据在内存中的表示到流水线指令的构成，到虚拟存储器，到编译系统，到动态加载库，到最后的用户态应用。通过掌握程序是如何映射到系统上，以及程序是如何执行的，读者能够更好地理解程序的行为为什么是这样的，以及效率低下是如何造成的。
* 本书适合那些想要写出更快、更可靠程序的程序员阅读，也适合作为高等院校计算机及相关专业本科生、研究生的教材。""")
book5 = Book(title=u"果壳中的C#", subtitle=u"C#5.0权威指南", author=u"阿坝哈瑞 (Joseph Albahari) / 阿坝哈瑞 (Ben Albahari)",
             isbn="9787517010845", tags_string=u"计算机,程序设计,C#", image='http://img3.douban.com/lpic/s28152290.jpg',
             summary=u"""* 《果壳中的c#——c#5.0权威指南》是一本c＃5.0的权威技术指南，也是第一本中文版c＃5.0的学习资料。本书通过26章的内容，系统、全面、细致地讲解了c#5.0从基础知识到各种高级特性的命令、语法和用法。本书的讲解深入浅出，同时为每一个知识点都专门设计了贴切、简单、易懂的学习案例，从而可以帮助读者准确地理解知识点的含义并快速地学以致用。本书与之前的c#4.0版本相比，还新增了丰富的并发、异步、动态编程、代码精练、安全、com交互等高级特性相关的内容。
* 《果壳中的c#——c#5.0权威指南》还融汇了作者多年在软件开发及c#方面的研究及其实践经验，非常适合作为c#技术的一本通自学教程，亦是一本中高级c#技术人员不可多得的必备工具书。""")
book6 = Book(title=u"算法导论（原书第2版）",
             author="Thomas H.Cormen / Charles E.Leiserson / Ronald L.Rivest / Clifford Stein",
             isbn="9787111187776", tags_string=u"计算机,算法", image='http://img3.doubanio.com/lpic/s1959967.jpg',
             summary=u"这本书深入浅出，全面地介绍了计算机算法。对每一个算法的分析既易于理解又十分有趣，并保持了数学严谨性。本书的设计目标全面，适用于多种用途。涵盖的内容有：算法在计算中的作用，概率分析和随机算法的介绍。书中专门讨论了线性规划，介绍了动态规划的两个应用，随机化和线性规划技术的近似算法等，还有有关递归求解、快速排序中用到的划分方法与期望线性时间顺序统计算法，以及对贪心算法元素的讨论。此书还介绍了对强连通子图算法正确性的证明，对哈密顿回路和子集求和问题的NP完全性的证明等内容。全书提供了900多个练习题和思考题以及叙述较为详细的实例研究。")
logs = [Log(user1, book2), Log(user1, book3), Log(user1, book4), Log(user1, book6),
        Log(user2, book1), Log(user2, book3), Log(user2, book5),
        Log(user3, book2), Log(user3, book5)]

db.session.add_all([admin, user1, user2, user3, user4, book1, book2, book3, book4, book5, book6] + logs)
db.session.commit()

app_ctx.pop()

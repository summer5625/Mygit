项目名：选课系统

使用说明：
       python版本：python3.7
       开发环境：win10x64
       bin目录下提供三中角色的登录接口：管理员登录（manager_program.py），老师登录（teacher_program.py），学生登录（student_program.py）
      1、管理员视图：默认账户：admin  密码：admin，提供一下功能：
	(1)、学校创建
	(2)、课程创建
	(3)、班级创建
	(4)、添加老师
	(5)、更新课程：更新课程基本信息和课程上架，下架
	(6)、重置状态：重置老师和学生账户的密码和用户锁定状态
      2、老师视图：登录账号只支持老师工号登录，老师工号在管理员创建老师时生成，密码默认为：123.（提供测试账号：20190010001,20190010002,20190020001）提供功能如下：
	(1)、个人信息修改
	(2)、密码修改
	(3)、班级信息查看，包括班级学员查看
	(4)、上课打卡
	(5)、打分
      3、学生视图：登录账号只支持学生学号登录，提供测试账号（2019001001001,2019001002001）密码都是123，提供功能如下：
	(1)、账号注册
	(2)、选课
	(3)、充值
	(4)、个人信息查询
	(5)、个人信息修改
	(6)、密码修改
	(7)、分数查看
	(8)、充值记录查询

项目存在问题：
	1、学生在注册时必须选择班级才能注册成功，因为学号是由入学年份+学校代码+班级代码+序号组成
	2、删除course select system\db\classes\classes.pkl，course select system\db\teacher\teacher.pkl，course select system\db\school\school.pkl
	     course select system\db\course\course.pkl，course select system\db\teacher\teacher.pkl，course select system\db\student\student.pkl文件则程序无法运行
	3、该项目未提供账号删除功能
	4、一个老师只能带一门课程
	
	

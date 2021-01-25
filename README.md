# hippo_api

1、目录框架

```
├── hippo_api/      # 后端项目目录
       ├── logs/          # 项目运行时/开发时日志目录
       ├── manage.py
       ├── hippo_api/      # 项目主应用，开发时的代码保存
       │    ├── apps/      # 开发者的代码保存目录，以模块[子应用]为目录保存（包）
       │    ├── libs/      # 第三方类库的保存目录[第三方组件、模块]（包）
       │    ├── settings/  #（包）
       │         ├── dev.py   # 项目开发时的本地配置
       │         ├── prod.py  # 项目上线时的运行配置
       │         ├── test.py  # 测试人员使用的配置(咱们不需要)
       │    ├── urls.py    # 总路由（包）
       │    ├── utils/     # 多个模块[子应用]的公共函数类库[自己开发的组件]
       └── scripts/       # 保存项目运营时的脚本文件
```

2、功能点

- 目录优化，开发测试环境隔离
- 自定义日志与切割，定向控制大小输出
- 异常处理、自定义程序异常处理
- 后端跨域，django使用中间件跨域
- 管理后台admin系统，继承默认的 auth_user 表


3、待更新

- xadmin

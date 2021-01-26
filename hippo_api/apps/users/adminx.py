import xadmin
from xadmin import views


class BaseSetting(object):
    """xadmin的基本配置"""
    enable_themes = True    # 开启主题切换功能
    use_bootswatch = True   # 引导控制盘(其实就是我们的左侧菜单栏)


xadmin.site.register(views.BaseAdminView, BaseSetting)   # 固定搭配


class GlobalSettings(object):
    """xadmin的全局配置"""
    site_title = "Hippo后台"  # 设置站点标题
    site_footer = "牛逼的后台，双击 star"  # 设置站点的页脚
    menu_style = "accordion"  # 设置菜单折叠


xadmin.site.register(views.CommAdminView, GlobalSettings)



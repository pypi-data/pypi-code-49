def help():
    """
    显示帮助信息
    """

    return ("pysmms {arg}\n\n"
            "   profile          查看用户资料（需要配置 Authorization）\n"
            "   ip_history       基于 IP 的临时上传历史记录\n"
            "   history          获取用户上传记录（需要配置 Authorization）\n"
            "   /path/to/picture 上传图片（需要配置 Authorization）\n\n"
            "上传图片不需要配置 Authorization，但不保证图片的使用时效。\n"
            "配置 Authorization 需要在用户根目录创建 .pysmms 文件，文件写入以下内容：\n\n"
            "    [sm.ms]\n"
            "    auth=['wKSlYH******z8eb8qSr']\n\n"
            "注意：auth 以列表存放，支持多个 auth 随机上传。")

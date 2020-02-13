#!/usr/local/bin/python3
# -*- coding: utf8 -*-
#
# @author: natloc
# @date: 2019/10/11
# @time: 11:57
# @doc:
# Copyright © 2019 natloc. All rights reserved.
#

import nat.cmd
import nat.string



# 获取当前差异内容
# return string
def status_retStr():
    ret = nat.cmd.executeRead("git status")

    if nat.cmd.isLastCmdSuccess():
        return ret.read()
    else:
        return ""

# 是否已提交完所有变更
# return: bool
def status_isClean():
    return status_retStr().find("nothing to commit, working tree clean") >= 0

# 是否有内容变更需要提交
# return: bool
def status_isCommitable():
    return status_retStr().find("Changes to be committed:") >= 0

# 是否有内容需要 git add 添加
# return: bool
def status_isAddable():
    return status_retStr().find("Changes not staged for commit:") >= 0


# 下载代码
# return: bool
def clone(url):
    url = nat.string.trim(url)
    if "" != url:
        return nat.cmd.execute("git clone %s" %(url))
    else:
        return False

# 刷新
# return: bool
def fetch():
    return nat.cmd.execute("git fetch")

# 更新代码
# return: bool
def pull(branchName = "master", repoName = "origin", enableEdit = True):
    branchName = nat.string.trim(branchName)
    repoName = nat.string.trim(repoName)

    if "" == branchName or "" == repoName:
        return False
    else:
        editMode = ""
        if not enableEdit:
            editMode = "--no-edit"
        return nat.cmd.execute("git pull %s %s %s" %(repoName, branchName, editMode))


# 添加所有修改
# return: bool
def add():
    return nat.cmd.execute("git add .")



# 提交
# return: bool
def commit(messageStr):
    nat.cmd.execute(u"git commit -m \"%s\"" %(messageStr))

# 添加并提交
# return: bool
def addAndCommit(messageStr):
    return add() and commit(messageStr)


# 推送代码
# return: bool
def push(branchName = "master", repoName = "origin", withTags = False):
    branchName = nat.string.trim(branchName)
    repoName = nat.string.trim(repoName)

    if "" == branchName or "" == repoName:
        return False
    else:
        if withTags:
            withTagsStr = "--tags"
        else:
            withTagsStr = ""

        return nat.cmd.execute("git push %s %s %s" %(repoName, branchName, withTagsStr))





# 获取所有分支列表
# return: [string]
def branch_list():
    ret = nat.cmd.executeRead("git branch")

    branchList = []
    if nat.cmd.isLastCmdSuccess():
        for line in ret.readlines():
            branch = line.lstrip("*").strip()
            if "" != branch:
                branchList.append(branch)


    return branchList

# 获取当前分支名
# return: string
def branch_current():
    ret = nat.cmd.executeRead("git branch")

    if nat.cmd.isLastCmdSuccess():
        for line in ret.readlines():
            if 0 == line.find("* "):
                return line.lstrip("*").strip()

    return ""

# 判断当前是否主分支
# return: bool
def branch_isCurMaster():
    return "master" == branch_current()

# 判断是否有指定的分支
# return: bool
def branch_hasBranch(branchNameStr):
    for branch in branch_list():
        if branch == branchNameStr:
            return True

    return False

# 切换分支；如果目标分支不存在则返回 false
# return bool
def branch_switch(branchNameStr):
    if branch_hasBranch(branchNameStr):

        if branch_current() == branchNameStr:
            return True
        else:
            nat.cmd.execute(u"git checkout %s" %(branchNameStr))
            return branch_current() == branchNameStr

    else:
        return False

# 切换分支；如果目标分支不存在则自动创建
# # return bool
def branch_switchSafety(branchNameStr):
    if branch_switch(branchNameStr):
        return True

    branchNameStr = nat.string.trim(branchNameStr)
    return "" != branchNameStr and nat.cmd.execute(u"git checkout -b %s" %(branchNameStr))



# 添加 tag 名
# return: bool
def tag_add(tagNameStr):
    tagNameStr = nat.string.trim(tagNameStr)
    return False if "" == tagNameStr else nat.cmd.execute("git tag %s" %(tagNameStr))

# 移除 tag 名
# return: bool
def tag_remove(tagNameStr):
    tagNameStr = nat.string.trim(tagNameStr)
    return False if "" == tagNameStr else nat.cmd.execute("git tag -d %s" %(tagNameStr))

# 获取所有 tag
# return [TagName :: string, ...]
def tag_list():
    tagsStr = nat.cmd.executeRead("git tag").read()
    tagsArr = tagsStr.split("\n")

    tagList = []
    for tag in tagsArr:
        tag = tag.strip()
        if "" != tag:
            tagList.append(tag)

    return tagList

# 判断是否已有 tag
# return bool
def tag_has(tagNameStr):
    tagNameStr = nat.string.trim(tagNameStr)
    return tagNameStr in tag_list()








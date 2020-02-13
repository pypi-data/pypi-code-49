#!/usr/local/bin/python3
# -*- coding: utf8 -*-
#
# @author: natloc
# @date: 2019/10/12
# @time: 18:16
# @doc:
# Copyright © 2019 natloc. All rights reserved.
#

import nat.string
import nat.path
import nat.plist
import nat.file
import nat.cmd
import nat.log


# 基础打包类：支持 打包 + 导出
class _Archive(object):

    __XC_PROJECT_SUFFIX = "xcodeproj"
    __XC_WORKSPACE_SUFFIX = "xcworkspace"

    __ARCHIVE_SUFFIX = "xcarchive"
    __MANIFEST_PLIST_FILENAME = "manifest.plist"
    __EXPORT_OPTIONS_PLIST_FILENAME = "ExportOptions.plist"

    __DEFAULT_EXPORTED_ARCHIVE_DIR_BASENAME = "exportedArchive"
    __DEFAULT_EXPORTED_IPA_DIR_BASENAME = "ipa"

    __DEFAULT_UPDATE_MD_BASENAME = "update"

    _ARCHIVE_ERR_PRIFIX = u"iOS 打包 * "



    # 项目路径
    __projectDirPath = ""
    # 项目名
    _projectName = ""

    # xccodeproj 目录
    __xcCodeProjDirPath = ""
    # xcworkspace 目录
    __xcWorkSpaceDirPath = ""



    def __init__(self, projectDirPath):
        # 项目路径、项目名
        projectPath = nat.path.getAbsPath(nat.string.trim(projectDirPath))
        if not nat.path.isDir(projectPath):
            self._exitLog(u"%s初始化失败：项目目录不存在，%s" %(projectPath))

        projectName = nat.path.getBasename(projectDirPath)
        if "" == projectName:
            self._exitLog(u"初始化失败：项目目录名为空，%s" %(projectName))

        self.__projectDirPath = projectPath
        self._projectName = projectName


        # 项目配置
        xcProjDirPath = nat.path.join(self.__projectDirPath, "%s.%s" %(self._projectName, self.__XC_PROJECT_SUFFIX))
        if not nat.path.isDir(xcProjDirPath):
            self._exitLog(u"初始化失败：.xccodeproj 不存在：%s" %(projectDirPath))

        self.__xcCodeProjDirPath = xcProjDirPath

        xcWorkspaceDirPath = nat.path.join(self.__projectDirPath, "%s.%s" %(self._projectName, self.__XC_WORKSPACE_SUFFIX))
        if nat.path.isDir(xcWorkspaceDirPath):
            self.__xcWorkSpaceDirPath = xcWorkspaceDirPath

        if "" == self.__getAvailTeamID():
            self._exitLog(u"初始化失败：必须设置 teamID")


        # update.md
        if self._isForceEnableUpdateMd():
            updateMdPath = self._getAvailUpdateMdPath()
            if not nat.path.isFile(updateMdPath):
                nat.file.createEmptyFile(updateMdPath)

            content = nat.string.trim(self._getUpdateContent())
            if "" == content:
                self._onErrorUpdateMdEmpty()
                self._exitLog(u"初始化失败：必须填写更新内容到 %s" %(nat.path.getFilename(updateMdPath)))

            if not self._isUpdateMdContentValid():
                self._exitLog(u"初始化失败：%s 的内容格式不正确" %(nat.path.getFilename(updateMdPath)))




    # --- 功能函数

    # 执行项目清理工作
    # return: bool
    def doClean(self):
        exportedArchiveDirPath = self._getAvailExportedArchiveDirPath()
        nat.path.rmDirRecursive(exportedArchiveDirPath)

        exportedIpaDirPath = self._getAvailExportedIpaDirPath()
        nat.path.rmDirRecursive(exportedIpaDirPath)

        (typeStr, dirPath) = self.__getXc()
        cmdStr = "xcodebuild clean -%s %s -scheme %s -configuration %s" %(typeStr, dirPath, self.__getAvailScheme(), self._getIsReleaseModeStr())

        return nat.cmd.execute(cmdStr)

    # 编译 IPA 并生成 *.xcarchive 文件
    # return: bool
    def doGenArchive(self):
        (typeStr, dirPath) = self.__getXc()

        exportedArchivePath = self.__getAvailExportedArchivePath()
        cmdStr = "xcodebuild archive -%s %s -scheme %s -configuration %s -archivePath %s" %(typeStr, dirPath, self.__getAvailScheme(), self._getIsReleaseModeStr(), exportedArchivePath)

        return nat.cmd.execute(cmdStr)

    # 由 archive 导出 AdHoc 类型的 IPA
    # return: bool
    def doExportIpaForAdHoc(self):
        return self.__doExportIPA(True)

    # 由 archive 导出 AppStore 类型的 IPA
    # return: bool
    def doExportIpaForAppStore(self):
        return self.__doExportIPA(False)

    # 由 archive 导出 IPA
    # param: isAdHoc :: bool   # true-AdHoc；false-AppStore
    # return: bool
    def __doExportIPA(self, isAdHoc):
        exportedArchivePath = self.__getAvailExportedArchivePath()
        if not nat.path.isDir(exportedArchivePath):
            self._exitLog(u"导出 IPA 失败：archive 不存在：%s" %(exportedArchivePath))

        # 创建配置选项文件
        exportedIpaDirPath = self._getAvailExportedIpaDirPath()
        exportOptsPlistPath = nat.path.join(self._getAvailExportedArchiveDirPath(), self.__EXPORT_OPTIONS_PLIST_FILENAME)
        if isAdHoc:
            self.__createExportOptsPlistFileForAdHoc(exportOptsPlistPath)
        else:
            self.__createExportOptsPlistFileForAppStore(exportOptsPlistPath)

        autoSigningAndGenProfileStr = ""
        if self.__isEnableAutoSigningAndGenProfile():
            autoSigningAndGenProfileStr = "-allowProvisioningUpdates"

        cmdStr = "xcodebuild -exportArchive %s -archivePath %s -exportPath %s -exportOptionsPlist %s" %(autoSigningAndGenProfileStr, exportedArchivePath, exportedIpaDirPath, exportOptsPlistPath)

        return nat.cmd.execute(cmdStr)

    # 上传 IPA 到 AppStore
    # return: bool
    def doUploadToAppStore(self):
        cmd = "xcrun"
        if not nat.cmd.hasCmd(cmd):
            self._exitLog(u"xcrun 命令未安装")

        ipaFile = self.__getAvailExportedIpaPath()
        if not nat.path.isFile(ipaFile):
            self._exitLog(u"ipa 文件不存在")

        p8Path = self.__getAvailUploadAppstoreApiP8Path()
        if not nat.path.isFile(p8Path):
            self._exitLog(u"p8 文件不存在")

        apiKey = nat.string.trim(self._getUploadAppstoreApiKey())
        apiIssuer = nat.string.trim(self._getUploadAppstoreApiIssuer())
        if "" == apiIssuer:
            self._exitLog(u"api issuer 不能为空")


        cmdStr = "xcrun altool --%s-app -t ios -f %s --apiKey %s --apiIssuer %s"

        # 验证
        cmdValidateStr = cmdStr %("validate", ipaFile, apiKey, apiIssuer)
        if not nat.cmd.execute(cmdValidateStr):
            self._exitLog(u"验证上传失败")

        # 上传
        cmdValidateStr = cmdStr %("upload", ipaFile, apiKey, apiIssuer)
        if not nat.cmd.execute(cmdValidateStr):
            self._exitLog(u"上传到 appstore 失败")

        return True


    # 获取可用的 export 导出目录
    # return: string
    def _getAvailExportedDirPath(self):
        dirPath = nat.path.getAbsPath( nat.string.trim(self._getExportedArchiveDirPath()) )
        if not nat.path.isDir(dirPath) and "" != dirPath:
            nat.path.mkDirRecursive(dirPath)

        # 创建后再次检查
        if not nat.path.isDir(dirPath):
            dirPath = self.__projectDirPath

        return dirPath



    # 获取有效的打包后生成的 *.xcarchive 的目录
    # return: string
    def _getAvailExportedArchiveDirPath(self):
        dirPath = self._getAvailExportedDirPath()

        dirBasename = nat.string.trim(self._getExportedArchiveDirBasename())
        if "" == dirBasename:
            dirBasename = self.__DEFAULT_EXPORTED_ARCHIVE_DIR_BASENAME

        # archive 目录
        archiveDirPath = nat.path.join(dirPath, dirBasename)
        if nat.path.mkDirRecursive(archiveDirPath):
            return archiveDirPath
        else:
            self._exitLog(u"创建 *.xcarchive 所在的目录失败：%s" %(archiveDirPath))

    # 获取有效的打包后生成的 *.xcarchive 的路径
    # return: string
    def __getAvailExportedArchivePath(self):
        dirPath = self._getAvailExportedArchiveDirPath()

        basename = nat.string.trim(self._getExportedArchiveBasename())
        if "" == basename:
            basename = self._projectName

        return nat.path.join(dirPath, "%s.%s" %(basename, self.__ARCHIVE_SUFFIX))



    # 获取有效的 *.xcarchive 导出的 ipa 的目录
    # return: string
    def _getAvailExportedIpaDirPath(self):
        dirPath = nat.path.getAbsPath( nat.string.trim(self._getExportedIpaDirPath()) )
        if not nat.path.isDir(dirPath) and "" != dirPath:
            nat.path.mkDirRecursive(dirPath)

        # 创建后再次检查
        if not nat.path.isDir(dirPath):
            dirPath = self._getAvailExportedArchiveDirPath()

        dirBasename = self._getAvailExportedIpaDirBasename()

        # ipa 导出目录
        exportedIpaDirPath = nat.path.join(dirPath, dirBasename)
        if nat.path.mkDir(exportedIpaDirPath):
            return exportedIpaDirPath
        else:
            self._exitLog(u"创建 ipa 的导出目录失败：%s" %(exportedIpaDirPath))

    def _getAvailExportedIpaDirBasename(self):
        dirBasename = nat.string.trim(self._getExportedIpaDirBasename())
        if "" == dirBasename:
            dirBasename = self.__DEFAULT_EXPORTED_IPA_DIR_BASENAME

        return dirBasename

    def __getAvailExportedIpaPath(self):
        ipaDirPath = self._getAvailExportedIpaDirPath()
        return nat.path.join(ipaDirPath, "%s.ipa" %(self._projectName))

    # 获取导出 IPA 目录下的 manifest.plist 文件路径
    # return: string
    def _getAvailExportedIpaManifestPlistPath(self):
        return nat.path.join(self._getAvailExportedIpaDirPath(), self.__MANIFEST_PLIST_FILENAME)



    # 获取 *.p8 文件名
    # return: string
    def __getAvailUploadAppstoreApiP8Filename(self):
        apiKey = nat.string.trim(self._getUploadAppstoreApiKey())
        if "" == apiKey:
            return ""
        else:
            return "AuthKey_%s.p8" %(apiKey)

    # 获取 *.p8 文件路径
    # return: string
    def __getAvailUploadAppstoreApiP8Path(self):
        dir = self._getUploadAppstoreApiP8Dir()
        if not nat.path.isDir(dir):
            dir = nat.path.join( nat.path.getUserHomePath(), ".private_keys" )

        filename = self.__getAvailUploadAppstoreApiP8Filename()
        if "" == filename:
            return ""
        else:
            return nat.path.join(dir, filename)



    # 输出 log 日志并退出
    def _exitLog(self, content):
        nat.log.exit(u"%s%s" %(self._ARCHIVE_ERR_PRIFIX, content))

    # 获取有效的 工程配置目录
    # return: (typeStr, dirPath)
    def __getXc(self):
        if "" != self.__xcWorkSpaceDirPath:
            return ("workspace", self.__xcWorkSpaceDirPath)
        else:
            return ("project", self.__xcCodeProjDirPath)



    # 删除生成的 *.xcarchive 文件
    def removeExportedArchive(self):
        nat.path.rmDirRecursive(self.__getAvailExportedArchivePath())

    # 删除生成的 *.ipa 文件
    def removeExportedIap(self):
        nat.path.rmFile(self.__getAvailExportedIpaPath())



    # 创建导出 IPA 的选项配置文件：AdHoc
    def __createExportOptsPlistFileForAdHoc(self, exportOptsPlistPath):
        if not nat.path.isValidFilePath(exportOptsPlistPath):
            self._exitLog(u"创建 archive 的选项配置文件失败，路径不合法：%s" %(exportOptsPlistPath))

        elif not nat.plist.createEmptyFile(exportOptsPlistPath):
            self._exitLog(u"创建 archive 的选项配置文件失败：%s" %(exportOptsPlistPath))

        else:
            nat.plist.addStr(exportOptsPlistPath, "teamID", self._getTeamID())

            nat.plist.addStr(exportOptsPlistPath, "method", "ad-hoc")
            nat.plist.addStr(exportOptsPlistPath, "thinning", "<none>")
            nat.plist.addBool(exportOptsPlistPath, "stripSwiftSymbols", True)
            nat.plist.addBool(exportOptsPlistPath, "compileBitcode", True)

            self.__manageExportOptsPlistFileSigning(exportOptsPlistPath)

            dictKey = "manifest"
            downloadUrlPrefix = nat.path.join(self.__getDownloadIpaUrlDomainPath(), self._projectName)
            nat.plist.addDict(exportOptsPlistPath, dictKey)
            nat.plist.addStr(exportOptsPlistPath, "appURL", "%s.ipa" %(downloadUrlPrefix), dictKey)
            nat.plist.addStr(exportOptsPlistPath, "displayImageURL", "%s.57.png" %(downloadUrlPrefix), dictKey)
            nat.plist.addStr(exportOptsPlistPath, "fullSizeImageURL", "%s.512.png" %(downloadUrlPrefix), dictKey)


    # 创建导出 IPA 的选项配置文件：AppStore
    def __createExportOptsPlistFileForAppStore(self, exportOptsPlistPath):
        if not nat.path.isValidFilePath(exportOptsPlistPath):
            self._exitLog(u"创建 archive 的选项配置文件失败，路径不合法：%s" %(exportOptsPlistPath))

        elif not nat.plist.createEmptyFile(exportOptsPlistPath):
            self._exitLog(u"创建 archive 的选项配置文件失败：%s" %(exportOptsPlistPath))

        else:
            nat.plist.addStr(exportOptsPlistPath, "teamID", self._getTeamID())
            nat.plist.addStr(exportOptsPlistPath, "method", "app-store")
            nat.plist.addBool(exportOptsPlistPath, "stripSwiftSymbols", True)
            nat.plist.addBool(exportOptsPlistPath, "uploadSymbols", True)
            nat.plist.addBool(exportOptsPlistPath, "uploadBitcode", True)

            self.__manageExportOptsPlistFileSigning(exportOptsPlistPath)

    # 管理配置文件的签名信息
    def __manageExportOptsPlistFileSigning(self, exportOptsPlistPath):
        bundleIdProvisionList = self.__getAvailProvisioningProfiles()
        bundleIdProvisionLen = len(bundleIdProvisionList)

        nat.plist.addStr(exportOptsPlistPath, "destination", "export")

        # 签名方式
        if 0 == bundleIdProvisionLen:
            signingStyle = "automatic"
        else:
            signingStyle = "manual"

        nat.plist.addStr(exportOptsPlistPath, "signingStyle", signingStyle)

        # profile
        if bundleIdProvisionLen > 0:
            dictKey = "provisioningProfiles"
            nat.plist.addDict(exportOptsPlistPath, dictKey)
            for (bundleID, provisioningProfileName) in bundleIdProvisionList:
                nat.plist.addStr(exportOptsPlistPath, bundleID, provisioningProfileName, dictKey)

        # certificate
        certificateName = self.__getAvailCertificateName()
        if "" != certificateName:
            nat.plist.addStr(exportOptsPlistPath, "signingCertificate", certificateName)


    # 获取 ipa 的下载域名前缀地址，不包含 suffix 部分
    def __getDownloadIpaUrlDomainPath(self):
        domain = nat.string.trim(self._getDownloadIpaUrlDomain())
        urlPath = nat.string.trim(self._getDownloadIpaUrlPath())

        if not domain.startswith("https://") and not domain.startswith("http://"):
            self._exitLog(u"ipa 的下载地址必须以 https 或 http 开头：%s" %(domain))

        if domain.endswith("/"):
            domain = domain[:-1]

        if "" != urlPath and "/" != urlPath[0]:
            urlPath = u"/%s" %(urlPath)

        return domain + urlPath

    # return: string
    def __getAvailTeamID(self):
        return nat.string.trim( self._getTeamID() )

    # return: string
    def __getAvailScheme(self):
        scheme = nat.string.trim( self._getScheme() )
        if "" == scheme:
            return self._projectName
        else:
            return scheme

    # return: string
    def _getIsReleaseModeStr(self):
        if self._getIsReleaseMode():
            return "Release"
        else:
            return "Debug"

    # 获取 update.md 文件的路径
    # return: string
    def _getAvailUpdateMdPath(self):
        basename = nat.string.trim(self._getUpdateMdBasename())
        if "" == basename:
            basename = self.__DEFAULT_UPDATE_MD_BASENAME

        return nat.path.join(self.__projectDirPath, "%s.md" %(basename))

    # 获取更新的内容
    # return: string
    def _getUpdateContent(self):
        return ""

    # 可选：需子类实现
    # 设置指定的 profile；为空则使用
    # return: [(BundleID: string, ProfileBaseName: string), ...]   #
    def __getAvailProvisioningProfiles(self):
        availList = []
        for (bundleId, provisioningName) in self._getProvisioningProfiles():
            bundleId = nat.string.trim(bundleId)
            provisioningName = nat.string.trim(provisioningName)

            if "" != bundleId and "" != provisioningName:
                availList.append((bundleId, provisioningName))

        return availList


    # 获取有效的 证书 名
    # return: string
    def __getAvailCertificateName(self):
        return nat.string.trim(self._getSigningCertificate())

    # 是否允许自动签名；当 provisioning 为空时自动允许
    # return: bool
    def __isEnableAutoSigningAndGenProfile(self):
        return self._isEnableAutoSigningAndGenProfile() or [] == self.__getAvailProvisioningProfiles()


    # --- 必选：需子类实现


    # 必选：需子类实现
    # 获取下载 ipa 的域名，必须以 https:// 或 http:// 开头
    # return: string
    def _getDownloadIpaUrlDomain(self):
        return ""

    # 必选：需子类实现
    # 获取下载 ipa 的路径，以 / 开头
    # return: string
    def _getDownloadIpaUrlPath(self):
        return ""

    # 必选：需子类实现
    # 开发者 teamID，用于导出 IPA
    # return: string
    def _getTeamID(self):
        return ""



    # --- 可选：需子类实现

    # 可选：需子类实现
    # 获取打包后生成的 *.xcarchive 的目录；如果为空则默认使用 项目的根目录
    # 完整目录由：DirPath/ DirBasename/ 组成
    # return: stringå
    def _getExportedArchiveDirPath(self):
        return ""

    # 可选：需子类实现
    # 获取打包后生成的 *.xcarchive 的目录名；如果为空则默认使用 exportedArchive
    # 完整目录由：DirPath/ DirBasename/ 组成
    # return: string
    def _getExportedArchiveDirBasename(self):
        return ""

    # 可选：需子类实现
    # 获取打包后生成的 *.xcarchive 的 basename；如果为空则默认使用项目名
    # return: string
    def _getExportedArchiveBasename(self):
        return ""


    # 可选：需子类实现
    # 获取由 *.xcarchive 导出的 ipa 的目录；如果为空则默认使用 self._getAvailExportedArchiveDirPath()
    # 完整目录由：DirPath/ DirBasename/ 组成
    # return: string
    def _getExportedIpaDirPath(self):
        return ""

    # 可选：需子类实现
    # 获取由 *.xcarchive 导出的 ipa 的目录名；如果为空则默认使用 ipa
    # 完整目录由：DirPath/ DirBasename/ 组成
    # return: string
    def _getExportedIpaDirBasename(self):
        return ""


    # 可选：需子类实现
    # TARGET 的 scheme；如果为空则默认使用项目名
    # return: string
    def _getScheme(self):
        return ""

    # 可选：需子类实现
    # 模式
    # return: bool
    def _getIsReleaseMode(self):
        return False

    # 可选：需子类实现
    # 是否允许 Xcode 自动签名生成 provisioning
    def _isEnableAutoSigningAndGenProfile(self):
        return False

    # 可选：需子类实现
    # 是否强制开启 更新 *.md 文本内容 的功能；若开启则每次打包必须填写更新内容
    # return: bool
    def _isForceEnableUpdateMd(self):
        return False

    # 可选：需子类实现
    # 获取更新文件 *.md 的 basename；若为空则默认为 update
    # return: string
    def _getUpdateMdBasename(self):
        return ""

    # 可选：需子类实现
    # 检查 *.md 的文件内容格式是否正确
    # return: bool
    def _isUpdateMdContentValid(self):
        return True


    # 可选：需子类实现
    # 设置指定的 profile；为空则使用
    # return: [(BundleID: string, ProfileBaseName: string), ...]   #
    def _getProvisioningProfiles(self):
        return []

    # 可选：需子类实现
    # 设置指定的 证书；为空则使用
    # return: string
    def _getSigningCertificate(self):
        return ""


    # 当 update.md 文件为空时的回调
    def _onErrorUpdateMdEmpty(self):
        pass


    # 可选：需子类实现
    # 获取用于上传到 appstore 的 API KEY
    # return: string
    def _getUploadAppstoreApiKey(self):
        return ""

    # 可选：需子类实现
    # 获取用于上传到 appstore 的 API ISSUER
    # return: string
    def _getUploadAppstoreApiIssuer(self):
        return ""

    # 可选：需子类实现
    # 获取用于上传到 appstore 的 AuthKey_ApiKey.p8 文件的存放目录；未设置则使用 ~/.private_keys/
    # return: string
    def _getUploadAppstoreApiP8Dir(self):
        return ""












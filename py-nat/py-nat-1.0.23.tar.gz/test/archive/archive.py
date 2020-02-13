#!/usr/bin/python3
# -*- coding: utf8 -*-


import argparse
import sys
import os
import time
import nat.coding
import nat.global_
import nat.datetime

nat.coding.setDefaultUTF8()


# ----- 开始时间

def __timestamp():
	return int(nat.datetime.getTi())

__scriptStartTi = nat.datetime.getTi()


# ----- 根据项目修改的常量


__APP_NAME = nat.global_.getStr("APP_NAME")
__APP_LOGO_FILE = nat.global_.getStr("APP_LOGO_FILE")
__PLATFORM = nat.global_.getStr("PLATFORM")
__PROJECT_GIT_URL = nat.global_.getStr("PROJECT_GIT_URL")
_TEAM_ID = nat.global_.getStr("TEAM_ID")
_BUNDLE_ID = nat.global_.getStr("BUNDLE_ID")

_ITC_API_KEY = nat.global_.getStr("ITC_API_KEY")
_ITC_ISSUER_ID = nat.global_.getStr("ITC_ISSUER_ID")

_CERTIFICATE_INFO_ADHOC = nat.global_.get("CERTIFICATE_INFO_ADHOC")   # 财商：正式
_EXTRA_ADHOC_BUNDLEID_PROVISION_LIST = nat.global_.get("EXTRA_ADHOC_BUNDLEID_PROVISION_LIST")
_CERTIFICATE_INFO_APPSTORE = nat.global_.get("CERTIFICATE_INFO_APPSTORE")   # 财商：正式
_EXTRA_APPSTORE_BUNDLEID_PROVISION_LIST = nat.global_.get("EXTRA_APPSTORE_BUNDLEID_PROVISION_LIST")

__QIYE_WECHAT_WEBHOOK = nat.global_.getStr("QIYE_WECHAT_WEBHOOK")

__QRCODE_BG_PNG_PATH = nat.global_.getStr("QRCODE_BG_PNG_PATH")
__QRCODE_BG_STANDBY_PNG_PATH = nat.global_.getStr("QRCODE_BG_STANDBY_PNG_PATH")

__GIT_BRANCH_MODE = nat.global_.getStr("GIT_BRANCH_MODE")
__POD_UPDATE_FQ_RESOURCE = nat.global_.getBool("POD_UPDATE_FQ_RESOURCE")

__APK_SCRIPT_PATH = nat.global_.getStr("APK_SCRIPT_PATH")


# ----- 不常修改的常量
__PROJECT_DIR_PREFIX = "/Users/xb/Documents/"

_ACCOUNT_USER = "luxiaolong"
_ACCOUNT_PASSWD = "654321qwerQ"

__SERVER_HOST_IP = "10.20.22.224"
_DOWNLOAD_IPA_URL_DOMAIN = "http://%s" %(__SERVER_HOST_IP)
_MINI_HTTPS_DIR = "/Library/WebServer/Documents/http"

__DEFAULT_GITEE = "https://gitee.com/natloc/xb.git"
__DEFAULT_GITEE_RAW = "https://gitee.com/natloc/xb/raw/master"

_CODE_FILENAME = ".code"



import datetime

import nat.path
import nat.file
import nat.cmd
import nat.log
import nat.git
import nat.plist
import nat.version
import nat.image
import nat.string

import thd.wechat.group_robot
import thd.qrcode.nat_qrcode
import thd.ios.ipa

import utils


from bs4 import BeautifulSoup
import qrcode
from PIL import Image




# ----- 解析命令行
_parser = argparse.ArgumentParser()


_group = _parser.add_mutually_exclusive_group(required=False)
_group.add_argument("-p", "--projectDirectory", help=u"项目目录", type=str)

_parser.add_argument("-v", "--version", help=u"迭代版本号，如：1.13", type=str, required=True)
_parser.add_argument("--vsn", help=u"版本号；如：1.0.0", type=str, required=False)
_parser.add_argument("--silence", help=u"不发消息到企业微信群", action="store_true")

_groupMode = _parser.add_mutually_exclusive_group(required=False)
_groupMode.add_argument("--release", help=u"开启 Release 模式", action="store_true")
_groupMode.add_argument("--staging", help=u"开启 Staging 模式", action="store_true")
_groupMode.add_argument("--debug", help=u"开启 Debug 模式", action="store_true")
_groupMode.add_argument("--appstore", help=u"上传到 appstore", action="store_true")
_groupMode.add_argument("--mode", help=u"模式；如：debug | staging | release 等", type=str) # 优先级更高

_parser.add_argument("--releaseNote", help=u"更新日志", type=str)

# android 特有选项
_parser.add_argument("--args", help=u"android 参数列表；以空格为分隔符", type=str)
_parser.add_argument("--commitInfo", help=u"android 提交信息", type=str)


_args = _parser.parse_args()


_version = nat.string.trim(_args.version)
_versionName = nat.string.trim(_args.vsn)
_projectDir = nat.path.getAbsPath(nat.string.trim(_args.projectDirectory))

_isSilence = _args.silence

_androidArgs = _args.args
_releaseNote = _args.releaseNote
if None == _releaseNote:
	_releaseNote = u""


_commitInfo = _args.commitInfo
if None == _commitInfo:
	commitInfo = u""


# ----- 模式
__argMode = nat.string.trim(_args.mode).lower() if nat.string.isStr(_args.mode) else ""
__modeSwitch = {
	"debug": "Debug",
	"debug_qa": "Debug_QA",
	"debug_all": "Debug_All",

	"staging": "Staging",
	"debug_staging": "Debug_Staging",

	"release": "Release",

	"appstore": "appstore",
}
_mode = __modeSwitch.get(__argMode, "")

if "" == _mode:
	if _args.appstore:
		_mode = "appstore"
	elif _args.staging:
		_mode = "Staging"
	elif _args.release:
		_mode = "Release"
	else:
		_mode = "Debug"

_isModeAppStore = "appstore" == _mode
_isModeRelease = "release" == _mode.lower()
_isModeStaging = "staging" == _mode.lower() or "debug_staging" == _mode.lower()


_projectName = os.path.basename(__PROJECT_GIT_URL).split(".")[0]
_platform = __PLATFORM
_projectDir = "%s/%s/%s/v%s" %(__PROJECT_DIR_PREFIX, _platform, _projectName, _version)   # 如：/Users/xb/Documents/ios/fq/v1.13   # 之后将变成 /Users/xb/Documents/ios/fq/v1.13/fq
_isIOS = "ios" == __PLATFORM
__projectInfoPlistPath = "%s/%s/%s/Info.plist" %(_projectDir, _projectName, _projectName)


if _isIOS:
	if _isModeAppStore:
		_certificateName = _CERTIFICATE_INFO_APPSTORE[0]
		_provisioningName = _CERTIFICATE_INFO_APPSTORE[1]
	else:
		_certificateName = _CERTIFICATE_INFO_ADHOC[0]
		_provisioningName = _CERTIFICATE_INFO_ADHOC[1]


# ----- 内部函数
def __exit(content):
	nat.log.exit(u"%s ===" %(content))

def __warn(content):
	nat.log.warn(u"%s ===" %(content))



# 解析更新内容行为 md 字符串
def _parseUpdateLines(contentLineArr):
	content = u""

	for contentLine in contentLineArr:
		contentLine = contentLine.strip()

		if "" == contentLine:
			continue

		# info 类别：任务
		elif contentLine.startswith("+"):
			contentLine = contentLine[1:].strip()
			try:
				jiraCode = int(contentLine)
				jiraIssueTitle = utils.reqJiraTitle(jiraCode)
				content += u"- **<font color=\"info\">[任务]</font>** [%s](http://jira.xiaobangtouzi.com/browse/FQ-%i)\n" %(jiraIssueTitle, jiraCode)
			except:
				contentLine = contentLine[1:].strip()
				content += u"- **<font color=\"info\">[任务]</font>** %s\n" %(contentLine)

		# warning 类别：bug
		elif contentLine.startswith("-"):
			contentLine = contentLine[1:].strip()
			try:
				jiraCode = int(contentLine)
				jiraIssueTitle = utils.reqJiraTitle(jiraCode)
				content += u"- **<font color=\"warning\">[bug]</font>** [%s](http://jira.xiaobangtouzi.com/browse/FQ-%i)\n" %(jiraIssueTitle, jiraCode)
			except:
				nat.log.exit(u"- 类别必须填写 jira 的单号数字，当前内容错误：%s" %(contentLine))

		# comment 类别：
		elif contentLine.startswith("*"):
			contentLine = contentLine[1:].strip()
			content += u"- **<font color=\"comment\">[备注]</font>** %s\n" %(contentLine)

		# 引用 类别：
		elif contentLine.startswith(">"):
			content += u"%s\n" %(contentLine)

		else:
			content += u"- %s\n" %(contentLine)

	return content


# ----- 检测参数
if "" == _version:
	__exit(u"请输入迭代号；如：1.13 迭代")
elif _isIOS and _isModeAppStore and not nat.version.isValid(_versionName):
	__exit(u"请通过 --vsn VersionStr 输入正确的版本号；如：--vsn 1.0.0")
# elif not nat.path.isDir(_projectDir):
# 	__exit(u"项目目录不存在")
elif not nat.path.isDir(_MINI_HTTPS_DIR):
	__exit(u"mini 服务器的 https 目录不存在：%s" %(_MINI_HTTPS_DIR))


# ----- iOS 准备
if _isIOS:
	# ----- 创建分支
	if not nat.path.isDir(_projectDir) and not nat.path.mkDirRecursive(_projectDir):
		__exit(u"创建分支目录失败：%s" %(_projectDir))

	nat.path.changeCwd(_projectDir)
	_projectDir = nat.path.join(_projectDir, _projectName)
	if not nat.path.isDir(_projectDir) and not nat.git.clone(__PROJECT_GIT_URL):
		__exit(u"克隆项目到本地失败")

	# ----- 更新当前分支到最新代码
	nat.path.changeCwd(_projectDir)

	if "develop" == __GIT_BRANCH_MODE:
		targetBranchName = "Develop"
	elif "developer" == __GIT_BRANCH_MODE:
		targetBranchName = __GIT_BRANCH_MODE
	else:
		targetBranchName = nat.string.trim("qa-%s" %(_version))

	if nat.git.branch_isCurMaster():
		nat.git.fetch()
		if not nat.cmd.execute("git checkout -b %s origin/%s" %(targetBranchName, targetBranchName)):
			__exit(u"切换到目标分支 %s 失败，请先手动新增该分支到远程仓库" %(targetBranchName))

	elif targetBranchName == nat.git.branch_current():
		pass

	else:
		__exit(u"当前分支与目标分支不同，无法检出；当前分支：%s，目标分支：%s" %(nat.git.branch_current(), targetBranchName))

	# 切换新分支
	nat.git.pull(targetBranchName, enableEdit = False)
	if _isIOS:
		nat.git.push(targetBranchName)



# ----- 小帮 iOS 打包类
class XbIosArchive(thd.ios.ipa._Archive):

	def _getDownloadIpaUrlDomain(self):
		return _DOWNLOAD_IPA_URL_DOMAIN

	# 如：/fq/ios/v1.13/02/ipa
	def _getDownloadIpaUrlPath(self):
		return "/%s/%s/v%s/%s/%s/%s" %(self._projectName, _platform, _version, _mode, self.getCode(), self._getAvailExportedIpaDirBasename())

	def _getTeamID(self):
		return _TEAM_ID

	def getCode(self):
		codePath = self.getCodePath()
		if not nat.path.isFile(codePath):
			codeDirPath = os.path.dirname(codePath)
			if not nat.path.mkDirRecursive(codeDirPath) or not nat.file.createEmptyFile(codePath, "1"):
				nat.log.exit(u"创建 %s 文件失败" %(codePath))

		codeInt = int(nat.string.trim(nat.file.read(codePath)))
		return "%02d" %(codeInt)

	def getCodePath(self):
		exportDirPath = self._getAvailExportedDirPath()
		exportBasename = "export-%s/%s" %(_version, self._getIsReleaseModeStr().lower())
		exportDir = nat.path.join(exportDirPath, exportBasename)

		return nat.path.join(exportDir, _CODE_FILENAME)

	def _getExportedArchiveDirBasename(self):
		return "export-%s/%s/%s" %(_version, self._getIsReleaseModeStr().lower(), self.getCode())

	def _getProvisioningProfiles(self):
		extraList = []

		if not _isModeAppStore and None != _EXTRA_ADHOC_BUNDLEID_PROVISION_LIST:
			extraList = _EXTRA_ADHOC_BUNDLEID_PROVISION_LIST
		elif _isModeAppStore and None != _EXTRA_APPSTORE_BUNDLEID_PROVISION_LIST:
			extraList = _EXTRA_APPSTORE_BUNDLEID_PROVISION_LIST

		if "" != _provisioningName:
			extraList.append((_BUNDLE_ID, _provisioningName))

		return extraList

	def _isEnableAutoSigningAndGenProfile(self):
		return True

	def _getSigningCertificate(self):
		return _certificateName

	def __mkReleaseTag(self):
		return _mode


	def _getIsReleaseMode(self):
		return _isModeRelease

	def __getIsStagingMode(self):
		return _isModeStaging

	def _getIsAppStoreMode(self):
		return _isModeAppStore

	def _getIsReleaseModeStr(self):
		return _mode


	def _isForceEnableUpdateMd(self):
		return _isIOS and not _isModeAppStore

	def _isUpdateMdContentValid(self):
		content = self.getUpdateMdContent()
		return "" != content

	def _getUpdateContent(self):
		return self.getUpdateMdContent()


	def getUpdateMdContent(self):
		updateMdPath = self._getAvailUpdateMdPath()

		content = ""
		if nat.path.isFile(updateMdPath):
			updateFileFp = open(updateMdPath, "r")
			content += _parseUpdateLines(updateFileFp.readlines())
			content += u"\n"
			updateFileFp.close()

		content += _parseUpdateLines(_releaseNote.split("\n"))
		if "" == content:
			return ""
		else:
			prefix = u"### 【提测-%s】\n#### 【iOS-%s迭代-%s】\n" %(self.__mkReleaseTag(), _version, self.getCode())
			return prefix + content

	def _onErrorUpdateMdEmpty(self):
		cmdStr = "open -a Sublime\ Text %s" %(self._getAvailUpdateMdPath())
		nat.cmd.execute(cmdStr)

	def _getUploadAppstoreApiKey(self):
		return _ITC_API_KEY

	def _getUploadAppstoreApiIssuer(self):
		return _ITC_ISSUER_ID



# ----- 小帮 android 打包类
class XbAndroidArchive:

	__projectDirPath = ""
	_projectName = ""

	_datetime = ""   # 年月日时分；如：201805051259

	_argApkPath = ""
	_argVersionName = ""
	_argBuildType = ""
	_argPartnerNo = ""
	_argCommitName = ""
	_argCommitId = ""
	_argCommitBranch = ""

	def __init__(self, projectDirPath):
		# 项目路径、项目名
		projectPath = nat.path.getAbsPath(nat.string.trim(projectDirPath))
		if not nat.path.isDir(projectPath) and not nat.path.mkDirRecursive(projectPath):
			nat.log.exit(u"初始化失败：项目目录不存在，项目名：%s，目录：%s" %(_projectName, projectPath))

		projectName = nat.path.getBasename(projectDirPath)
		if "" == projectName:
			nat.log.exit(u"初始化失败：项目名为空，%s" %(_projectName))

		self.__projectDirPath = projectPath
		_projectDir = projectPath
		self._projectName = projectName

		# 解析参数
		argsArr = _androidArgs.split(" ")
		if len(argsArr) >= 4:
			self._argApkPath = argsArr[0]
			self._argVersionName = argsArr[1]
			self._argBuildType = argsArr[2]
			self._argPartnerNo = argsArr[3]

		# 解析提交信息
		argsArr = _commitInfo.split(" ")
		if len(argsArr) >= 3:
			self._argCommitName = argsArr[0]
			self._argCommitId = argsArr[1]
			self._argCommitBranch = argsArr[2]

		# 检测参数
		if not nat.path.isDir(self._argApkPath):
			nat.log.exit(u"初始化失败：http 目录不存在，%s" %(_projectName))
		elif not self._argApkPath.startswith(_MINI_HTTPS_DIR):
			nat.log.exit(u"初始化失败：apk 路径不是 Http 目录，%s" %(_projectName))

		# 时间
		self._datetime = time.strftime("%Y%m%d%H%M", time.localtime())



	def getCode(self):
		codePath = self.getCodePath()
		if not nat.path.isFile(codePath):
			codeDirPath = os.path.dirname(codePath)
			if not nat.path.mkDirRecursive(codeDirPath) or not nat.file.createEmptyFile(codePath, "1"):
				nat.log.exit(u"创建 %s 文件失败" %(codePath))

		codeInt = int(nat.string.trim(nat.file.read(codePath)))
		return "%02d" %(codeInt)

	def getCodePath(self):
		exportDirPath = self._getAvailExportedDirPath()
		exportBasename = "export-%s/%s" %(_version, self._getIsReleaseModeStr().lower())
		exportDir = nat.path.join(exportDirPath, exportBasename)

		return nat.path.join(exportDir, _CODE_FILENAME)


	def _getIsReleaseMode(self):
		return _isModeRelease

	def _getIsStagingMode(self):
		return _isModeStaging

	def _getIsReleaseModeStr(self):
		return _mode

	def _mkReleaseTag(self):
		return _mode


	def _getAvailExportedDirPath(self):
		return _projectDir


	# 生成 apk 的 basename
	def _mkApkBasename(self):
		return "xiaobangguihua_%s_%s_%s_%s" %(_version, self._getIsReleaseModeStr().lower(), self._argPartnerNo, self._datetime)

	def _mkApkFilename(self):
		return "%s.apk" %(self._mkApkBasename())

	def _mkApkHttpPath(self):
		return nat.path.join(self._argApkPath, "%s/%s" %(self._datetime, self._mkApkFilename()))

	# 生成下载链接
	def _mkApkDownloadUrl(self):
		httpPath = self._argApkPath[len(_MINI_HTTPS_DIR):]
		httpPath = nat.path.join(httpPath, "%s/%s" %(self._datetime, self._mkApkFilename()))
		return "%s%s" %(_DOWNLOAD_IPA_URL_DOMAIN, httpPath)


	# 生成迭代号；如：1.3
	def _mkDiedai(self):
		valueArr = _version.split(".")
		if len(valueArr) >= 2:
			return "%s.%s" %(valueArr[0], valueArr[1])
		else:
			valueArr = self._argVersionName.split(".")
			if len(valueArr) >= 2:
				return "%s.%s" %(valueArr[0], valueArr[1])
			else:
				return self._argVersionName


	# 发布日志
	def getUpdateMdContent(self):
		content = u"### 【提测-%s】\n#### 【android-%s迭代-%s】\n" %(self._mkReleaseTag(), self._mkDiedai(), _code)
		content += _parseUpdateLines(_releaseNote.split("\\n"))

		return content



# ----- 实例化对象
if _isIOS:
	archive = XbIosArchive(_projectDir)
else:
	archive = XbAndroidArchive(_projectDir)

_code = archive.getCode()
__vsnCode = "v%s/%s" %(_version, _code)   # 如：v1.13/03
__vsnModeCode = "v%s/%s/%s" %(_version, _mode, _code)   # 如：v1.13/debug/03
__projectPlatformVsn = "%s/%s/v%s" %(archive._projectName, _platform, _version)   # 如：fq/ios/v1.13
__projectPlatformVsnMode = "%s/%s" %(__projectPlatformVsn, _mode)   # 如：fq/ios/v1.13/debug
__projectPlatformVsnModeCode = "%s/%s/%s" %(__projectPlatformVsn, _mode, _code)   # 如：fq/ios/v1.13/debug/03
__versionCode = "%s%s" %(nat.version.toCodeStr(_versionName), _code)   # 如：01010104
__miniDirPath = "%s/%s" %(_MINI_HTTPS_DIR, __projectPlatformVsnModeCode)   # 如：/...web.../fq/ios/v1.13/release/03/
__manifestDownloadUrl = "%s/%s.plist" %(__DEFAULT_GITEE_RAW, __projectPlatformVsnModeCode)



# ----- iOS 打包
if _isIOS:
	# 进行 pod install
	nat.cmd.execute("pod install")
	nat.cmd.execute("pod install")
	if __POD_UPDATE_FQ_RESOURCE:
		nat.cmd.execute("pod update fq-resource")


	# 如果是上架 AppStore
	if _isModeAppStore:
		if not nat.path.isFile(__projectInfoPlistPath):
			__exit(u"项目的 Info.plist 文件不存在")

		nat.plist.setStr(__projectInfoPlistPath, "CFBundleShortVersionString", _versionName)
		nat.plist.setStr(__projectInfoPlistPath, "CFBundleVersion", "%s" %(__versionCode))

		if None != _EXTRA_APPSTORE_BUNDLEID_PROVISION_LIST:
			for (bundleId, _) in _EXTRA_APPSTORE_BUNDLEID_PROVISION_LIST:
				targetName = bundleId.split(".")[-1]
				extraProjectInfoPlistPath = "%s/%s/Info.plist" %(_projectDir, targetName)
				if nat.path.isFile(extraProjectInfoPlistPath):
					nat.plist.setStr(extraProjectInfoPlistPath, "CFBundleShortVersionString", _versionName)
					nat.plist.setStr(extraProjectInfoPlistPath, "CFBundleVersion", "%s" %(__versionCode))

		nat.git.addAndCommit(u"【开始上传】%s" %(_versionName))

	else:
		# 读取版本更新内容
		updateMdPath = archive._getAvailUpdateMdPath()
		updateMdContent = archive.getUpdateMdContent()

		# 添加 tag
		if not nat.git.tag_has(__vsnModeCode):
			nat.git.tag_add(__vsnModeCode)
		nat.git.addAndCommit(u"【开始提测】%s" %(__vsnModeCode))

		# 清空 update.md
		nat.cmd.execute("echo \"\" > %s" %(updateMdPath))
		nat.git.addAndCommit(u"【完成提测】")


	# ----- 打包操作
	__warn(u"开始清理项目")
	if not archive.doClean():
		__exit(u"清理项目失败")

	__warn(u"开始生成 archive")
	if not archive.doGenArchive():
		__exit(u"生成 archive 失败")


	# ----- 上传到 appstore
	if _isModeAppStore:
		__warn(u"开始导出 IPA")
		if not archive.doExportIpaForAppStore():
			__exit(u"导出 IPA 失败")

		__warn(u"开始上传到 appstore")
		if not archive.doUploadToAppStore():
			__exit(u"上传到 appstore 失败")

	# ----- AdHoc 打包
	else:
		__warn(u"开始导出 IPA")
		if not archive.doExportIpaForAdHoc():
			__exit(u"导出 IPA 失败")


		# ----- 推送 manifest 到 gitee
		__warn(u"开始提交 manifest.plist 到远程仓库")
		archiveExportDirPath = archive._getAvailExportedArchiveDirPath()
		nat.path.changeCwd(archiveExportDirPath)
		nat.git.clone(__DEFAULT_GITEE)

		# 跳转到 gitee 目录
		giteeBasename = os.path.splitext(os.path.basename(__DEFAULT_GITEE))[0]   # xb
		giteeDirPath = os.path.join(archiveExportDirPath, giteeBasename)
		nat.path.changeCwd(giteeDirPath)

		# 创建迭代目录
		manifestDirPath = "%s/%s" %(giteeDirPath, __projectPlatformVsnMode)
		nat.path.mkDirRecursive(manifestDirPath)

		# 拷贝 manifest.plist 文件
		manifestPlistNewPath = nat.path.join(manifestDirPath, "%s.plist" %(_code))
		manifestPlistPath = archive._getAvailExportedIpaManifestPlistPath()
		nat.plist.remove(manifestPlistPath, ":items:0:assets:2")   # 移除 full-size-image
		nat.plist.remove(manifestPlistPath, ":items:0:assets:1")   # 移除 display-image
		nat.cmd.execute("cp %s %s" %(manifestPlistPath, manifestPlistNewPath))

		# 加入版本控制
		nat.git.add()
		if not nat.git.status_isClean():
			nat.git.commit(u"[Auto Commit]")

		nat.git.push()
		__warn(u"已推送 manifest.plist")



		# ----- 同步数据到 mini 的 https 地址
		__warn(u"开始同步资料到 mini")
		nat.path.rmDirRecursive(__miniDirPath)
		nat.path.mkDirRecursive(__miniDirPath)

		# 同步 ipa
		ipaDirPath = archive._getAvailExportedIpaDirPath()
		if not nat.path.cpDir(ipaDirPath, __miniDirPath):
			__exit(u"同步资料到 mini 失败")

		# 同步 更新文件
		updateMdFilePath = nat.path.join(__miniDirPath, "update.md")
		if not nat.file.write(__miniDirPath, "update.md", updateMdContent):
			__exit(u"推送 更新文件 到 mini 失败")


# ----- android 打包
else:
	cmdStr = "%s %s %s" %(__APK_SCRIPT_PATH, _androidArgs, archive._datetime)
	if not nat.cmd.execute(cmdStr):
		__exit(u"执行 android 打包脚本失败：执行命令失败：%s" %(cmdStr))

	# 检测打包结果
	apkHttpPath = archive._mkApkHttpPath()
	if not nat.path.isFile(apkHttpPath):
		__exit(u"执行 android 打包脚本失败：没有生成 apk 文件：%s" %(apkHttpPath))


# ----- 通知企业微信群
if not _isSilence:
	__warn(u"开始通知企业微信群")

	# iOS
	if _isIOS:
		if _isModeAppStore:
			# md
			msgMd = thd.wechat.group_robot.MarkdownMessage(__QIYE_WECHAT_WEBHOOK)
			updateMdContent = u"### 【准备提审-AppStore】\n#### 【iOS-%s迭代-%s】\n" %(_version, archive.getCode())
			msgMd.append(updateMdContent)

			# at 所有人
			msgText = thd.wechat.group_robot.TextMessage(__QIYE_WECHAT_WEBHOOK)
			msgText.setContent(u"版本：%s\n版本编号：%s" %(_versionName, __versionCode))
			msgText.setMentionedAll()

			# 发送
			msgMd.send()
			msgText.send()

		else:
			# md
			msgMd = thd.wechat.group_robot.MarkdownMessage(__QIYE_WECHAT_WEBHOOK)
			msgMd.append(updateMdContent)

			# at 所有人
			standbyUrl = "http://%s/download/?n=%s&p=%s&v=%s&m=%s&c=%s" %(__SERVER_HOST_IP, _projectName, _platform, _version, _mode, _code)
			msgText = thd.wechat.group_robot.TextMessage(__QIYE_WECHAT_WEBHOOK)
			msgText.setContent(u"请扫码下载：\n或使用备用链接：%s" %(standbyUrl))
			msgText.setMentionedAll()

			# 二维码：原始链接
			qrGenerator = thd.qrcode.nat_qrcode.Generator()
			qrGenerator.setDestDirPath(archive._getAvailExportedArchiveDirPath())
			qrGenerator.setDestBasename(archive._projectName)
			qrGenerator.setUrl(__manifestDownloadUrl, True)
			# qrGenerator.setBgImgPath(__QRCODE_BG_PNG_PATH)
			if not qrGenerator.generate():
				__exit(u"生成下载二维码失败")

			qrPath = qrGenerator.getQrPath()
			img = nat.image.NatImage(qrPath)
			img.setWidth(150, True)

			# 中间添加logo
			if nat.path.isFile(__APP_LOGO_FILE):
				logoImg = nat.image.NatImage(__APP_LOGO_FILE)
				logoImg.setRGBA().setWidth(50, True)

				img.setRGBA()
				img.pasteImg(logoImg, 50, 50)

			img.save()

			msgImg = thd.wechat.group_robot.ImageMessage(__QIYE_WECHAT_WEBHOOK)
			msgImg.setImg(qrPath)

			# 二维码：备用链接
			# qrGeneratorStandby = thd.qrcode.nat_qrcode.Generator()
			# qrGeneratorStandby.setDestDirPath(archive._getAvailExportedArchiveDirPath())
			# qrGeneratorStandby.setDestBasename("%s_standby" %(archive._projectName))
			# qrGeneratorStandby.setUrl(standbyUrl)
			# qrGeneratorStandby.setBgImgPath(__QRCODE_BG_STANDBY_PNG_PATH)
			# if not qrGeneratorStandby.generate():
			# 	__exit(u"生成备用二维码失败")
			#
			# qrPathStandby = qrGeneratorStandby.getQrPath()
			# imgStandby = nat.image.NatImage(qrPathStandby)
			# imgStandby.setWidth(150, True)
			# imgStandby.save()
			#
			# msgImgStandby = thd.wechat.group_robot.ImageMessage(__QIYE_WECHAT_WEBHOOK)
			# msgImgStandby.setImg(qrPathStandby)

			# 同步二维码图片到 mini
			nat.cmd.execute("cp %s %s/" %(qrPath, __miniDirPath))
			# nat.cmd.execute("cp %s %s/" %(qrPathStandby, __miniDirPath))

			# 发送消息
			msgMd.send()
			msgText.send()
			msgImg.send()
			# msgImgStandby.send()

	# android
	else:
		# md
		msgMd = thd.wechat.group_robot.MarkdownMessage(__QIYE_WECHAT_WEBHOOK)
		msgMd.append(archive.getUpdateMdContent())
		msgMd.append("\n\n")
		msgMd.append(msgMd.mkLink(u"点击安装 APK (%s)" %(archive._mkApkFilename()), archive._mkApkDownloadUrl()))

		# text
		msgText = thd.wechat.group_robot.TextMessage(__QIYE_WECHAT_WEBHOOK)
		msgText.setMentionedAll()

		# 发送消息
		msgMd.send()
		msgText.send()



# 推送到 qa 分支
if _isIOS:
	nat.path.changeCwd(_projectDir)
	nat.git.pull(targetBranchName, enableEdit = False)
	if not nat.git.push(targetBranchName, withTags = True):
		__exit(u"推送分支 %s 失败" %(targetBranchName))


# ----- 推送到自动化建设 - app 包管理
__warn(u"开始推送到集成平台")
if _isIOS:
	nat.path.changeCwd(_projectDir)
	gitLog = nat.cmd.executeRead("git log -1")
	commit_id = gitLog.readline().split(" ")[1].strip()
	submitter = gitLog.readline().split(" ")[1].strip()
	quality_qa_download_url = "itms-services://?action=download-manifest&url=%s" %(__manifestDownloadUrl)
else:
	commit_id = archive._argCommitId
	submitter = archive._argCommitName
	targetBranchName = archive._argCommitBranch
	quality_qa_download_url = archive._mkApkDownloadUrl()

utils.syncQualityQA(__APP_NAME, _version, _code, targetBranchName, _platform, commit_id, _mode, submitter, quality_qa_download_url)


# ----- 开始进行清理工作
__warn(u"开始清理工作")
if _isIOS:
	# 删除 *.xcarchive 和 提审 appstore 产生的 ipa
	archive.removeExportedArchive()
	archive.removeExportedIap()



# ----- 递增迭代 code 号
_code = int(_code) + 1
nat.cmd.execute("echo %d > %s" %(_code, archive.getCodePath()))



# ----- 完成打包
utils.printArchiveDuration(__scriptStartTi)


















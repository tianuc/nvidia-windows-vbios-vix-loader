# NVIDIA Windows VBIOS Vix Loader 中文维护版

上游：[Panchovix/nvidia-windows-vbios-vix-loader](https://github.com/Panchovix/nvidia-windows-vbios-vix-loader)。中文维护：[tianuc/nvidia-windows-vbios-vix-loader](https://github.com/tianuc/nvidia-windows-vbios-vix-loader)。

当前对应的上游版本与中文修订见 [upstream-version.json](upstream-version.json)。版本号沿用 `v上游版本-zh.中文修订`，例如 `v0.3.1-zh.1`。本项目是社区中文维护版，与 NVIDIA 没有隶属关系。原作者版权及 GPL-3.0-or-later 许可证均保留。

## 下载和打开

从本仓库的 [Releases](https://github.com/tianuc/nvidia-windows-vbios-vix-loader/releases) 下载 `vbios-loader-zh-…-windows-x64.zip`，解压后打开 `vbios-loader-zh.exe`，无需安装 Python。发布页的 `SHA256SUMS-ZH` 可用于核对下载文件。请保留压缩包内的许可证及第三方声明。

主界面默认简体中文，可切换 English / Español，支持浅色、深色和跟随系统。主界面、常用错误、文件检查、加载确认、移除确认和验证结果均提供中文；少数驱动或系统底层错误可能保留原始英文详情。

## 它能做什么

将与显卡匹配的 VBIOS 文件保存到 NVIDIA 驱动使用的注册表覆盖项，在显卡或 Windows 重新启动后由驱动加载。**不向显卡闪存写入内容。** 工具本身不编辑 VBIOS，也不会自动超频、提高功耗或电压。修改过的 VBIOS 仍可能损坏硬件。

需要 Windows 10/11 x64、支持的 NVIDIA 显卡，以及 616.56 或更新的相应驱动。加载和移除需要管理员权限；查看状态及验证只读。详细硬件范围和限制见原版 [README.md](README.md)。

## 按钮说明

- **刷新**：重新检测显卡、驱动及保存的覆盖。
- **选择 VBIOS 文件**：仅检查文件与显卡是否匹配，此时不会写入显卡配置。
- **加载覆盖**：先显示具体显卡、文件 SHA256 和注册表修改清单，确认后才写入。
- **移除覆盖**：删除覆盖并恢复本工具保存的固件设置；其他工具原先写入的覆盖不会被恢复。
- **验证实际生效状态**：通过 NvAPI 两次读取驱动正在使用的 VBIOS，比较实际运行内容与保存的覆盖；不会写入配置。

中文版默认不勾选“操作后立即重启显卡”，与上游 README 对显示显卡的建议一致。如果此显卡正在连接显示器，请保持此选项关闭，在保存工作后重启 Windows。直接重启显示显卡可能出现无信号。

## 黑屏时恢复

若直接重启显卡后无信号，先重启 Windows。若启动后仍无画面，可进入 Windows 安全模式，打开工具，取消“操作后立即重启显卡”，点击“移除覆盖”，再正常重启。完整恢复步骤和注册表回退说明见原版 README 的 “If the GPU does not start”。

## 维护与上游同步

`main` 保留上游分支；`codex/zh-cn` 是中文维护分支，也是本 Fork 的默认分支。`upstream-version.json` 记录对应上游标签、完整提交和中文修订号。

在 Actions 中手动运行 **同步上游版本**：输入目标上游标签（留空时读取最新正式版）。流程会合并到新的同步分支、更新版本记录并运行测试，然后创建面向中文分支的更新 PR。合并冲突或新界面词条缺少翻译时流程会失败，需要维护者处理；不会自动合并或加载任何 VBIOS。

在中文分支推送提交，或手动运行 **构建中文版**，即可生成 Windows 构建产物。发布时推送与版本记录一致的标签，例如 `v0.3.1-zh.1`，测试和打包通过后自动建立带 EXE、ZIP 和 SHA256 的 Release。

## 本地构建

```powershell
python -m pip install pyinstaller==6.22.3
$env:PYTHONPATH = "src"
python -m unittest discover -s tests -v
python tools/build_chinese.py
```

建议使用 Windows x64 官方 CPython 3.12。发布包包含 Python、Tcl/Tk 和 PyInstaller 启动器，需要连同打包生成的许可证一起分发。源代码及构建脚本始终随仓库和发布标签提供。

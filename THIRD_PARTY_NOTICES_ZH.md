# 中文构建的第三方声明

本文件适用于由 `tools/build_chinese.py` 生成的 `vbios-loader-zh.exe`。原版 `THIRD_PARTY_NOTICES.md` 保留为上游文档，其中关于 Nuitka 的原版构建说明不适用于这个 PyInstaller 中文构建。

- 原项目：Copyright (C) 2026 panchovix，GNU GPL v3 或更新版本，全文见 `LICENSE`。
- 中文界面及中文构建维护：Copyright (C) 2026 tianuc，GNU GPL v3 或更新版本。
- CPython 运行时及标准库：Python Software Foundation 许可证，以及其所包含代码的声明，见 `third_party/CPython-LICENSE.txt`。
- Tcl/Tk 界面库及脚本：随 CPython 安装分发的 Tcl/Tk 许可；其文本包含在 CPython 的 Windows 许可证文件及打包找到的 `*-license.terms` 中。
- PyInstaller 启动器：GPL 许可证及允许分发生成程序的特殊例外，见 `third_party/PyInstaller-COPYING.txt`。PyInstaller 是构建工具，不是本项目的原作者。

实际 Python、Tcl/Tk 与打包工具版本见发布包的 `BUILD-INFO.txt`。项目源代码与对应发布标签位于 https://github.com/tianuc/nvidia-windows-vbios-vix-loader 。

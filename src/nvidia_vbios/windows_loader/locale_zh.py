"""Simplified Chinese UI for the community-maintained fork (GPL-3.0-or-later)."""
import re

STRINGS_ZH = {
    'title': 'NVIDIA VBIOS 加载器 · 中文社区版',
    'not_admin': '当前没有管理员权限：可以查看状态和验证，加载及移除覆盖已禁用。需要修改时，请以管理员身份重新打开。',
    'gpus': 'NVIDIA 显卡',
    'col_index': '序号', 'col_name': '显卡名称', 'col_pci': 'PCI ID', 'col_location': '位置',
    'col_driver': '驱动版本', 'col_override': 'VBIOS 覆盖状态',
    'refresh': '刷新', 'file': 'VBIOS 文件', 'file_button': '选择 VBIOS 文件…',
    'file_types': 'VBIOS 文件', 'all_files': '所有文件',
    'restart': '操作后立即重启显卡', 'load': '加载覆盖', 'remove': '移除覆盖', 'verify': '验证实际生效状态',
    'messages': '操作记录', 'working': '正在处理…重启显卡可能需要 45 秒。',
    'verifying': '正在读取驱动实际使用的 VBIOS…',
    'override_none': '无覆盖', 'override_loaded': '已加载：{size} 字节，SHA256 {sha}…',
    'override_other': '其他工具写入的覆盖：{size} 字节',
    'override_bad': 'vbios 注册表值类型异常（{type}）',
    'override_records': 'romOverride 记录（mVolt+）：{count} 条',
    'override_backup': '仅保留了 EnableGpuFirmware 备份', 'override_error': '无法读取显卡驱动注册表项',
    'driver_unknown': '未知', 'driver_too_old': '{version}（过旧，需要 {minimum} 或更新版本）',
    'no_gpu': '未找到 NVIDIA 显卡。', 'choose_gpu': '请选择显卡。',
    'choose_file': '请选择与此显卡匹配的 VBIOS 文件。',
    'cannot_read': '无法读取 {path}：{error}',
    'valid': '适用于显卡 {index}：{family}，将保存 {size} 字节，SHA256 {sha256}。',
    'refused': '文件未通过检查：{reason}',
    'confirm_load_title': '确认加载 VBIOS 覆盖',
    'confirm_load': '将此 VBIOS 加载到显卡 {index}（{name}，PCI {location}）？\n\n'
                    '文件：{path}\n保存内容：{size} 字节的映像链（{family}），SHA256 {sha256}\n\n'
                    '将修改显卡驱动项中的以下注册表值：\n{steps}',
    'confirm_remove_title': '确认移除 VBIOS 覆盖',
    'confirm_remove': '移除显卡 {index}（{name}，PCI {location}）的覆盖？\n\n将修改以下注册表值：\n{steps}',
    'other_tool': '此显卡已有其他工具（如 mVolt+）写入的覆盖；它将被替换，之后移除本工具的覆盖不会恢复旧覆盖。',
    'will_restart': '随后会重启显卡，显示器可能暂时黑屏；如果没有恢复信号，请重启 Windows，覆盖仍会保留。',
    'no_restart': '不会立即重启显卡；请在方便时重启 Windows，使更改生效。',
    'risk': '修改过的 VBIOS 可能损坏硬件。如果显卡无法启动，请按说明进入安全模式并移除覆盖。',
    'loaded': '显卡 {index}：已保存 VBIOS 覆盖，{size} 字节，SHA256 {sha256}。',
    'removed': '显卡 {index}：已移除覆盖。', 'restarted': '显卡已重启。',
    'not_restarted': '尚未重启显卡。请重启 Windows，使更改生效。',
    'restart_failed': '注册表值已写入，但显卡重启失败（{detail}）。请重启 Windows，使更改生效。',
    'pnputil_code': 'pnputil 退出码 {code}', 'pnputil_timeout': 'pnputil 未完成',
    'verify_override-active': '显卡 {index}：驱动正在使用加载的覆盖，逐字节验证一致。',
    'verify_override-active-prefix': '显卡 {index}：实际运行 VBIOS 的前 {compared} 字节与覆盖一致；其余部分无法读回。',
    'verify_override-not-active': '显卡 {index}：驱动尚未使用保存的覆盖。刚加载时需要重启显卡或 Windows；否则可能是驱动拒绝了覆盖，仍使用原 VBIOS。',
    'verify_no-override': '显卡 {index}：未保存覆盖，驱动应使用显卡原 VBIOS。如果刚移除覆盖，请先重启显卡或 Windows。',
    'verify_unstable': '显卡 {index}：两次读取的 VBIOS 内容不同，请重试。',
    'verify_prefix': '仅比较了前 {compared} 字节：NvAPI 最多读取这么多，而保存的覆盖有 {size} 字节。',
    'verify_difference': '首个不同字节位于偏移 {offset}。',
    'verify_records': '另有 romOverride 记录（mVolt+），驱动也可能将它们应用到显卡 VBIOS。',
    'verify_running': '实际运行 VBIOS：{size} 字节，SHA256 {sha256}。',
    'verify_stored': '已保存的覆盖：{size} 字节，SHA256 {sha256}。',
    'note': '提示：{message}', 'error': '错误：{message}', 'unexpected': '未预期的错误：{message}',
    'status_failed': '无法列出显卡：{message}',
    'hint_remove': '请在窗口中点击“刷新”，再点击“移除覆盖”，然后重启 Windows。',
    'hint_remove_first': '请先在窗口中点击“移除覆盖”。',
    'hint_refresh': '请点击“刷新”，重新选择显卡。',
    'language': '语言', 'theme': '主题', 'theme_auto': '跟随系统', 'theme_light': '浅色', 'theme_dark': '深色',
}


def translate_reason(text):
    """Translate UI diagnostics without changing backend decisions or error types."""
    replacements = {
        'administrator rights are required; run this from an elevated PowerShell': '需要管理员权限，请以管理员身份运行本程序',
        'no NVIDIA GPU matches that selection; run status to list them': '未找到匹配的 NVIDIA 显卡，请刷新显卡列表',
        'only NVIDIA GPUs are supported': '仅支持 NVIDIA 显卡',
        'No override is stored for this GPU.': '此显卡未保存任何覆盖。',
        'the registry values read back differ from what was written; run unload': '写入后的注册表读回结果不一致，请移除覆盖',
        'the registry values read back differ from what was expected': '注册表读回结果与预期不同',
        'the registry may be partly changed: run status, then unload,': '注册表可能已部分修改：请刷新状态并移除覆盖，',
        'holds an unexpected value; run unload first': '保存了异常值，请先移除覆盖',
        'holds an unexpected value; not changing it': '保存了异常值，已停止修改',
        ' (no image marked last)': '（没有标为结束的映像）',
        ' (the file may be a two-bank flash dump; normalize it to one image chain)': '（文件可能含两组映像，请先规范化为单条映像链）',
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    patterns = (
        (r'payload refused for GPU (\d+) \(([^)]+)\): ', r'显卡 \1（\2）拒绝此文件：'),
        (r'payload is (\d+) bytes; the loader accepts 512 B to 4 MiB', r'文件大小为 \1 字节；加载器接受 512 字节至 4 MiB'),
        (r'payload has (\d+) legacy images; the driver needs exactly one', r'文件含 \1 个传统映像；驱动要求恰好一个'),
        (r'legacy image at (0x[0-9a-f]+) has a nonzero checksum', r'偏移 \1 处传统映像的校验和错误'),
        (r'legacy image at (0x[0-9a-f]+) has an invalid length', r'偏移 \1 处传统映像的长度无效'),
        (r'legacy image at (0x[0-9a-f]+) is for PCI ID (.*)', r'偏移 \1 处传统映像对应其他 PCI ID：\2'),
        (r'the image chain is truncated at (0x[0-9a-f]+)', r'映像链在偏移 \1 处截断'),
        (r'unexpected ROM signature (0x[0-9a-f]+) at (0x[0-9a-f]+)', r'偏移 \2 处 ROM 签名异常：\1'),
        (r'missing PCI data structure for the image at (0x[0-9a-f]+)', r'偏移 \1 处映像缺少 PCI 数据结构'),
        (r'the image at (0x[0-9a-f]+) has an invalid length', r'偏移 \1 处映像长度无效'),
        (r'NVIDIA driver ([\d.]+) is too old; (.*)', r'NVIDIA 驱动 \1 版本过旧；\2'),
    )
    for pattern, replacement in patterns:
        text = re.sub(pattern, replacement, text)
    return text

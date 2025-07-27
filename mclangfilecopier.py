import os
import sys
import json
import zipfile
import shutil
import re
from pathlib import Path

def extract_lang_from_jar(jar_path):
    """从模组JAR文件中提取语言文件"""
    mod_id = None
    lang_files = {}
    
    with zipfile.ZipFile(jar_path, 'r') as jar:
        # 扫描JAR内文件路径匹配模式：assets/<modid>/lang/<langcode>.json
        lang_pattern = re.compile(r'assets/([^/]+)/lang/(en_us|zh_cn)\.json')
        
        for file in jar.namelist():
            match = lang_pattern.match(file)
            if match:
                mod_id = match.group(1)
                lang_type = match.group(2)
                # 提取到内存
                with jar.open(file) as f:
                    try:
                        lang_files[lang_type] = json.load(f)
                    except json.JSONDecodeError:
                        print(f"警告: {file} JSON格式错误，跳过此文件")
    
    if not lang_files:
        print(f"错误: 未在JAR中找到语言文件: {jar_path}")
        return None, None, None
    
    return mod_id, lang_files.get('en_us'), lang_files.get('zh_cn')

def merge_lang_files(en_data, zh_data):
    """合并英文和中文语言文件"""
    if en_data is None:
        print("错误: 英文语言数据为空")
        return None
    
    merged = {}
    missing_translations = []
    
    for key, value in en_data.items():
        # 保留现有翻译或回退到英文
        merged[key] = zh_data.get(key, value)
        if key not in zh_data:
            missing_translations.append(key)
    
    if missing_translations:
        print(f"警告: {len(missing_translations)}个条目缺少翻译")
    
    return merged

def process_jar(jar_path):
    """处理单个JAR文件"""
    print(f"\n处理文件: {os.path.basename(jar_path)}")
    
    # 提取语言文件
    mod_id, en_data, zh_data = extract_lang_from_jar(jar_path)
    if not mod_id:
        return False
    
    print(f"找到模组ID: {mod_id}")
    print(f"英文条目数: {len(en_data) if en_data else 0}")
    print(f"中文条目数: {len(zh_data) if zh_data else 0}")
    
    # 合并语言文件
    merged_data = merge_lang_files(en_data, zh_data)
    if not merged_data:
        return False
    
    # 保存路径处理
    output_dir = Path(jar_path).parent / "output"
    output_dir.mkdir(exist_ok=True)
    output_path = output_dir / f"{mod_id}_new_zh_cn.json"
    
    # 写入文件（带UTF-8 BOM）
    with open(output_path, 'w', encoding='utf-8-sig') as f:
        json.dump(merged_data, f, ensure_ascii=False, indent=2)
    
    print(f"生成新语言文件: {output_path}")
    print(f"总条目数: {len(merged_data)}")
    return True

def main():
    print("=" * 50)
    print("Minecraft 模组语言文件处理器")
    print("=" * 50)
    
    if len(sys.argv) < 2:
        print("\n请将模组JAR文件拖放到此脚本上")
        print("支持批量处理：可同时拖放多个JAR文件")
        input("\n按Enter键退出...")
        return
    
    success_count = 0
    for i, jar_path in enumerate(sys.argv[1:], 1):
        if not jar_path.lower().endswith('.jar'):
            print(f"\n跳过非JAR文件: {jar_path}")
            continue
        
        if process_jar(jar_path):
            success_count += 1
    
    print("\n" + "=" * 50)
    print(f"处理完成！成功处理 {success_count}/{len(sys.argv[1:])} 个文件")
    print("生成的文件保存在各JAR同目录的output文件夹内")
    print("=" * 50)
    input("\n按Enter键退出...")

if __name__ == "__main__":
    main()

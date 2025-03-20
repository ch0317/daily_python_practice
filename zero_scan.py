import sys
import os

def is_all_zero(filepath):
    try:
        with open(filepath, 'rb') as f:
            while True:
                chunk = f.read(4096)
                if not chunk:
                    break
                if any(byte != 0 for byte in chunk):
                    return False
        return True
    except FileNotFoundError:
        print(f"文件不存在: {filepath}")
        return False
    except Exception as e:
        print(f"检查文件时发生错误: {e}")
        return False

def main():
    if len(sys.argv) != 2:
        print("用法: python check_zero.py <文件路径>")
        sys.exit(1)

    filepath = sys.argv[1]

    if not os.path.isfile(filepath):
        print(f"错误：{filepath} 不是有效文件")
        sys.exit(1)

    if is_all_zero(filepath):
        print(f"✅ 文件 {filepath} 全是 0")
    else:
        print(f"❌ 文件 {filepath} 存在非0数据")

if __name__ == "__main__":
    main()

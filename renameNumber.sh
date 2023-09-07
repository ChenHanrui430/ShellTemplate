#!/bin/bash

# 创建一个子目录
mkdir new_images

# 设置计数器
count=1

# 遍历当前目录下的所有文件
for file in *.*; do
    # 判断文件是否为图片文件
    if [[ $file == *.png || $file == *.jpg || $file == *.jpeg ]]; then
        # 获取文件的扩展名
        extension="${file#*.}"
        # 生成新的文件名
        new_filename="${count}.${extension}"
        # 将新文件移动到子目录
        cp "$file" "new_images/${new_filename}"
        # 增加计数器
        count=$((count+1))
    fi
done

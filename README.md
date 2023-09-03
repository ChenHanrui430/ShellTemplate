# ShellTemplate
常用shell脚本

# 使用教程

## 1. ffmpegCoverCRF.sh
功能：以CRF参数为17自动遍历并清洗指定目录下所有视频文件（CRF参数主要作用为调节视频质量，一般16-18可在几乎不降低画质的情况下减小视频文件体积）

例子
``` shell
bash ffmpegCoverCRF.sh './videos'
```

## 2. ffmpegConvertMp4.bat
功能: 自动遍历脚本所在文件夹所有视频文件，并且在当前文件夹自动新建一个名为output的文件夹，将所有视频转化为mp4格式并放入output文件夹中
备注: 适用于Windows系统



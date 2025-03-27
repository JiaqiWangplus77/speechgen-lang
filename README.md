当然可以，以下是你项目的完整 README.md 文件，符合 GitHub 标准格式，包括：
	•	✅ 英文 + 中文
	•	✅ 完整代码块（无语法错误）
	•	✅ 清晰的项目结构
	•	✅ 可直接粘贴使用！

⸻

✅ README.md（完整双语标准 Markdown）

# SpeechGen-Lang

**SpeechGen-Lang** is a lightweight Python tool that converts custom language learning content into high-quality MP3 audio using AWS Polly. It's designed for learners who want to practice listening with personalized stories and slow, understandable speech.

## Features

- 🗣️ Neural voice synthesis with AWS Polly
- 🐢 Customizable speech rate and pause strength (after dots and commas)
- 📁 Reads input from text files, saves MP3 with timestamped filenames
- 🧩 Modular structure, ready for UI or LLM integration

## Installation

```bash
pip install -r requirements.txt
```
## Usage

### English

1. Place your input text (UTF-8 encoded) in the `input/` directory, for example:

   ```
   input/sample_story.txt
   ```

2. Run the main program:

   ```bash
   python src/main.py
   ```

3. The generated MP3 file will appear in the `output/` directory.  
   Its filename will follow the format:

   ```
   output/de_YYYYMMDD_HHMMSS.mp3
   ```
# SpeechGen-Lang（中文说明）

**SpeechGen-Lang** 是一个轻量级 Python 工具，使用 AWS Polly 将自定义语言学习文本转为高质量 MP3 音频。它适合希望通过个性化内容提升听力的学习者。

## 功能特点

- 🗣️ 使用 AWS Polly 神经网络语音，朗读自然流畅
- 🐢 支持自定义语速、句号和逗号停顿
- 📁 输入来自 `.txt` 文件，输出音频自动按时间戳命名
- 🧩 模块化设计，便于接入界面或大语言模型

## 安装依赖

```bash
pip install -r requirements.txt
```

## 使用方法

1. 将你的输入文本（需为 UTF-8 编码）放入 `input/` 文件夹，例如：

   ```
   input/sample_story.txt
   ```

2. 运行主程序：

   ```bash
   python src/main.py
   ```

3. 生成的 MP3 文件将保存在 `output/` 文件夹中。  
   文件名格式如下：

   ```
   output/de_YYYYMMDD_HHMMSS.mp3
   ```

## 项目结构

```text
speechgen-lang/
├── input/                  # 输入文本文件
├── output/                 # 输出音频文件
├── src/
│   ├── main.py             # 简洁的主入口
│   ├── generate_audio.py   # 核心语音合成逻辑
│   ├── config.py           # 默认语音、语速、停顿配置
│   ├── text_preprocessor.py # 处理 SSML 和插入停顿
├── README.md
└── requirements.txt
```

## 授权协议

MIT License（可自由修改并用于学习和个人项目）
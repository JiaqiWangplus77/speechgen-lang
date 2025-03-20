import boto3
import os
import re

# 1️⃣ 创建 Polly 客户端
polly = boto3.client("polly", region_name="eu-central-1")

# 2️⃣ SSML 预留字符转换
def escape_ssml(text):
    replacements = {
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        '"': "&quot;",
        "'": "&apos;"
    }
    for char, replacement in replacements.items():
        text = text.replace(char, replacement)
    return text

# 3️⃣ 在句号后添加自然停顿
def add_pauses(text):
    return re.sub(r"\.\s", ".<break strength='x-strong'/> ", text)  # 句号后增加段落级停顿

# 4️⃣ 从文件中读取文本
def read_text_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

# 5️⃣ 读取输入文本并处理 SSML 预留字符和停顿
input_text = read_text_from_file("input.txt")
escaped_text = escape_ssml(input_text)
escaped_text_with_pauses = add_pauses(escaped_text)

# 6️⃣ 朗读的文本，使用 SSML 进行语速控制和停顿
ssml_text = f"""
<speak>
    <prosody rate="slow">{escaped_text_with_pauses}</prosody>
</speak>"""

# 7️⃣ 请求 Polly 生成语音
response = polly.synthesize_speech(
    Text=ssml_text,
    OutputFormat="mp3",
    VoiceId="Vicki",  # Vicki 是 AWS Polly 的高质量 Neural 女声
    Engine="neural",  # 使用神经网络语音
    TextType="ssml"  # 启用 SSML
)

# 8️⃣ 确保输出目录存在
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "german_slow.mp3")

# 9️⃣ 保存音频文件
with open(output_path, "wb") as file:
    file.write(response["AudioStream"].read())

print(f"✅ 语音文件已生成: {output_path}")

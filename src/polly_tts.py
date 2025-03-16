import os
from src.config import get_polly_client

# 确保 output 目录存在
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def synthesize_speech(text, output_file="output.mp3"):
    """生成 AWS Polly 语音"""
    polly = get_polly_client()
    response = polly.synthesize_speech(Text=text, OutputFormat="mp3", VoiceId="Vicki")

    # 存入 output 目录
    output_path = os.path.join(OUTPUT_DIR, output_file)

    with open(output_path, "wb") as file:
        file.write(response["AudioStream"].read())

    print(f"✅ 语音文件已生成: {output_path}")
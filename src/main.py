import os
from generate_audio import synthesize_speech_to_mp3

if __name__ == "__main__":
    # 输入路径（你可以替换成命令行参数或UI选择）
    input_path = "../input/sample_story.txt"
    synthesize_speech_to_mp3(input_path=input_path)

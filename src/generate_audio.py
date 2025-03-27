import os
def synthesize_speech_to_mp3(
    input_path: str,
    voice_id: str = "Vicki",
    engine: str = "neural",
    rate: str = "x-slow",
    pause_after_dot: str = "x-strong",
    pause_after_comma: str = "strong",
    output_dir: str = "../output",
    language_code: str = "de"
):
    import boto3
    from text_preprocessor import escape_ssml, insert_pauses
    from datetime import datetime

    with open(input_path, "r", encoding="utf-8") as f:
        text = f.read()

    safe_text = escape_ssml(text)
    paused_text = insert_pauses(safe_text, dot=pause_after_dot, comma=pause_after_comma)
    ssml = f"""<speak><prosody rate="{rate}">{paused_text}</prosody></speak>"""

    polly = boto3.client("polly", region_name="eu-central-1")
    response = polly.synthesize_speech(
        Text=ssml,
        OutputFormat="mp3",
        VoiceId=voice_id,
        Engine=engine,
        TextType="ssml"
    )

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{language_code}_{timestamp}.mp3"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, filename)

    with open(output_path, "wb") as f:
        f.write(response["AudioStream"].read())

    print(f"✅ 成功生成语音：{output_path}")
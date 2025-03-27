# 可选语音设置（可扩展）
SUPPORTED_VOICES = {
    "de": [
        {"name": "Vicki", "gender": "Female", "engine": "neural"},
        {"name": "Hans", "gender": "Male", "engine": "neural"},
        {"name": "Marlene", "gender": "Female", "engine": "standard"}
    ],
    "en": [
        {"name": "Joanna", "gender": "Female", "engine": "neural"},
        {"name": "Matthew", "gender": "Male", "engine": "neural"}
    ]
}

# 可选语速（SSML 支持的值）
SUPPORTED_RATES = ["x-slow", "slow", "medium", "fast", "x-fast"]

# 停顿强度选项（SSML 支持的值）
SUPPORTED_PAUSES = ["none", "x-weak", "weak", "medium", "strong", "x-strong"]

# 默认设置
DEFAULT_SETTINGS = {
    "voice_id": "Vicki",
    "engine": "neural",
    "rate": "x-slow",
    "pause_after_dot": "x-strong",
    "pause_after_comma": "strong",
    "region": "eu-central-1"
}

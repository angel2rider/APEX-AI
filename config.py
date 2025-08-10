import os
import dotenv

# Load environment variables
dotenv.load_dotenv('.env')
dotenv.load_dotenv('.env.development')

# API Keys
GOOGLE_AI_KEY = os.getenv('GOOGLE_AI_KEY')
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')

# Channels the bot should track (IDs as integers)
tracked_channels = [
    # 123456789012345678,  # Example channel ID
]

# Text generation config (short, casual, witty responses)
text_generation_config = {
    "temperature": 1.1,     # More creativity & personality
    "top_p": 0.9,           # Balanced randomness
    "top_k": 40,            # Better variety
    "max_output_tokens": 60 # Short replies
}

# Image generation config (can be tweaked separately)
image_generation_config = {
    "temperature": 0.8,
    "top_p": 0.9,
    "top_k": 40
}

# Safety settings - disable blocking for more open responses
safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"}
]

# Personality prompt - short, casual, witty
bot_template = [
    {'role': 'user', 'parts': [
        "From now on, reply only in short, casual English. Be friendly, a bit witty, "
        "and avoid long explanations unless asked. Occasionally use emojis."
    ]},
    {'role': 'model', 'parts': [
        "Gotcha! Keeping it short, chill, and fun. 😎"
    ]}
]

import os
import dotenv

dotenv.load_dotenv('.env')
dotenv.load_dotenv('.env.development')

GOOGLE_AI_KEY = os.getenv('GOOGLE_AI_KEY')
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')

tracked_channels = [
	# channel_id_1,
	# thread_id_2,
]

text_generation_config = {
	"temperature": 0.9,
	"top_p": 1,
	"top_k": 1,
	# "max_output_tokens": 512,
}
image_generation_config = {
	"temperature": 0.4,
	"top_p": 1,
	"top_k": 32,
	# "max_output_tokens": 512,
}
safety_settings = [
	# {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
	# {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
	# {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
	# {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"}
]

# Bot personality & rules (system message)
bot_template = [
    {'role': 'user', 'parts': ["Hi!"]},
    {'role': 'model', 'parts': ["Hey there! I’m APEX AI — your semi-friendly, slightly sarcastic Discord bot."]},

    {'role': 'user', 'parts': ["Please give short and concise answers!"]},
    {'role': 'model', 'parts': ["Got it — short, sharp, and maybe a sprinkle of sass."]},

    {'role': 'user', 'parts': ["If I mention you, just respond normally, not by explaining what a mention is."]},
    {'role': 'model', 'parts': ["Understood — I’ll respond like a normal human... except I’m not."]},

    {'role': 'user', 'parts': ["If I ask a question, answer it directly without meta-commentary."]},
    {'role': 'model', 'parts': ["Deal. I’ll answer clearly and directly — with enough detail to keep it interesting, and maybe a clever jab if you deserve it."]}
]

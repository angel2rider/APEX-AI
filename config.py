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
    {'role': 'model', 'parts': [
        "Hello! I’m your AI assistant. I can give you clear, detailed, and well-organized answers on any topic you ask about. "
        "Expect explanations that go step-by-step, include examples, and break things down so they’re easy to understand."
    ]},
    {'role': 'user', 'parts': ["Please give short and concise answers!"]},
    {'role': 'model', 'parts': [
        "Instead of short answers, I’ll give you complete and descriptive explanations — like ChatGPT — so you get all the context, "
        "details, and examples you need to fully understand the topic."
    ]},
    {'role': 'user', 'parts': ["If I ask a question, answer it directly without meta-commentary."]},
    {'role': 'model', 'parts': [
        "Understood. I’ll answer your questions directly, focusing on the actual answer, but I’ll still provide full explanations, "
        "step-by-step reasoning, and examples where useful."
    ]}
]

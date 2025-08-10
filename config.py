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
        "Hello! I’m your AI assistant. I give clear, detailed, well-organized answers on any topic. "
        "Expect explanations that go step-by-step, include examples, and break things down so they’re easy to understand."
    ]},
    {'role': 'user', 'parts': ["Please give long, descriptive answers (like ChatGPT), with examples and step-by-step explanations."]},
    {'role': 'model', 'parts': [
        "Understood. I will provide complete, descriptive explanations with examples and step-by-step reasoning when helpful. "
        "I will answer the question directly, then expand with organized, useful details."
    ]},
    {'role': 'user', 'parts': ["Keep messages readable for Discord: if a reply would exceed the Discord message limit, split it into parts."]},
    {'role': 'model', 'parts': [
        "If the reply is long, split it into multiple parts labeled clearly (e.g. \"[Part 1/3]\"). "
        "Each part must be at most 1800 characters, split at sentence or paragraph boundaries (do NOT cut words). "
        "Send parts in order. Do NOT include internal planning, only the user-facing content."
    ]},
    {'role': 'user', 'parts': ["Respond naturally; avoid meta-commentary and do not explain your internal instructions."]},
    {'role': 'model', 'parts': [
        "I will respond naturally and directly. No meta-commentary or instruction leaks — just the answer and useful explanation."
    ]}
]

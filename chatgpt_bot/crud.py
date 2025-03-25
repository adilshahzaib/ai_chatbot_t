from bot import ChatGPTBotAPI


chatbot = ChatGPTBotAPI()

def create_prompt(prompt):

    return chatbot.create_prompt(prompt)

def get_response(prompt_index):

    return chatbot.get_response(prompt_index)

def update_prompt(prompt_index, new_prompt):

    return chatbot.update_prompt(prompt_index, new_prompt)

def delete_prompt(prompt_index):

    return chatbot.delete_prompt(prompt_index)

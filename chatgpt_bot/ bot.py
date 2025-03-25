from openai import OpenAI
from config import OPENAI_API_KEY

class ChatGPTBotAPI:
    def __init__(self):

        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.prompts = []

    def create_prompt(self, prompt):

        self.prompts.append(prompt)
        return len(self.prompts) - 1

    def get_response(self, prompt_index):
        """Return the ChatGPT response for a stored prompt."""
        if 0 <= prompt_index < len(self.prompts):
            prompt = self.prompts[prompt_index]

            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}]
            )

            return response.choices[0].message.content
        return None

    def update_prompt(self, prompt_index, new_prompt):

        if 0 <= prompt_index < len(self.prompts):
            self.prompts[prompt_index] = new_prompt
            return True
        return False

    def delete_prompt(self, prompt_index):

        if 0 <= prompt_index < len(self.prompts):
            del self.prompts[prompt_index]
            return True
        return False

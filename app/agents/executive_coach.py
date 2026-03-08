import ollama


class ExecutiveCoachAgent:

    def __init__(self, model="phi3:mini"):
        self.model = model
        self.system_prompt = self.load_prompt()

    def load_prompt(self):
        with open("app/prompts/coach_prompt.txt", "r") as f:
            return f.read()

    # NORMAL RESPONSE
    def run(self, user_input):

        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": user_input}
        ]

        response = ollama.chat(
            model=self.model,
            messages=messages
        )

        return response["message"]["content"]


    # STREAMING RESPONSE
    def run_stream(self, user_input):

        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": user_input}
        ]

        stream = ollama.chat(
            model=self.model,
            messages=messages,
            stream=True
        )

        for chunk in stream:
            yield chunk["message"]["content"]
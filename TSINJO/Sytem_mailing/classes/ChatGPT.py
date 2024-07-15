import openai
openai.api_key = "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"
class ChatGPT:
    def __init__(self) -> None:
        pass

    def requete(self,requete):

        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "hasina20.jeremia@gmail.com", "content": requete}
        ]
        )
        print(completion.choices[0].message)

    def req(self):
        response = openai.Completion.create(
            engine="text-davinci-002",  # Choisissez le moteur de génération approprié (par exemple, "text-davinci-002" pour le moteur GPT-3.5-turbo)
            prompt="Quel est le sens de la vie ?",  # Votre requête ou prompt
            max_tokens=100  # Le nombre maximum de tokens à générer dans la réponse
        )
        generated_text = response['choices'][0]['text']
        print(generated_text)
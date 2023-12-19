import openai

class Content():
    def __init__(self, api_key):
        self.key = api_key
        self.response_txt = None
        self.response_img = None
        self.broken_text = None

    def content_txt_davinci(self, sentence:str, model:str='text-davinci-003', temperature:int=1, max_tokens:int=1000):
        """ Essa função é para solicitar uma resposta ao prompt passado. Essa função utiliza uma versão mais ANTIGA do chatGPT. """
        openai.api_key = self.key
        response = openai.Completion.create(model=model, prompt=sentence, temperature=temperature, max_tokens=max_tokens)
        self.response_txt = response["choices"][0]["text"]
        return self.response_txt
    
    def content_txt_gpt(self, sentence:str, model:str='gpt-3.5-turbo-0301'):
        """ Essa função é para solicitar uma resposta ao prompt passado. Essa função utiliza uma versão mais ATUAL do chatGPT. """
        openai.api_key = self.key
        response = openai.ChatCompletion.create(model=model, messages=[{"role": "user", "content": sentence}])
        self.response_txt = response.choices[0].message['content']
        return self.response_txt
    
    def content_img(self, sentence):
        """ Essa função gera a imagem solicitada no prompt. """
        openai.api_key = self.key
        response = openai.Image.create(prompt=sentence, n=1, size="1024x1024")
        image_url = response['data'][0]['url']
        self.response_img = image_url
        return self.response_img
    
    def wrap_text(self, sentence, line_length=49):
        """ Essa função deixa o texto formatado para o tamanho ideal da imagem gerada. """
        lines = []
        current_line = ""
        words = sentence.split()
        for word in words:
            if(len(current_line+word) <= line_length):
                current_line += f" {word}"
            else:
                lines.append(current_line)
                current_line = word
        lines.append(current_line)
        self.broken_text = '\n'.join(lines)
        return self.broken_text
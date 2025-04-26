from ollama import Client
import re 
""""client = Client("http://ollama.default.svc.cluster.local:11434")"""

"""client = Client("http://ollama.default.svc.cluster.local:11434")"""

"""client = Client("http://host.docker.internal:11434")"""

"""client = Client("http://127.0.0.1:11434")"""
"""client = Client("http://ollama.default.svc.cluster.local:11434")"""


def generate_code(prompt):
    full_prompt = f"""Sen bir Python kod üreticisisin. Açıklamalı ve sade Python kodu üret.
Prompt: {prompt}"""
    response = client.chat(
        model='mistral',
        messages=[
            {"role": "system", "content": "Python kod üret"},
            {"role": "user", "content": full_prompt}
        ]
    )
    return response['message']['content']

def extract_code_and_title(text):
    code_match = re.search(r"```python\n(.*?)```", text, re.DOTALL)
    code = code_match.group(1) if code_match else text
    title = code.split('\n')[0].replace('#', '').strip() if code.startswith('#') else "Python Kod Parçası"
    return code, title

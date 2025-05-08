# Please install OpenAI SDK first: `pip3 install openai`

from openai import OpenAI
import yaml
client = OpenAI(api_key="sk-c7a1296e41424c319125bad01855fb06", base_url="https://api.deepseek.com")

def request(prompt):
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": prompt},
        ],
        stream=False
    )

    print(response.choices[0].message.content)


query = "众所周知，我们中国拥有着五千年璀璨历史。"


#load yaml

def load_prompt_from_yaml(yaml_path: str, query: str) -> str:
    with open(yaml_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    prompt_template = data['prompt']
    return prompt_template.format(query=query)

# 示例调用
prompt = load_prompt_from_yaml('prompt.yaml', query)

res = request(prompt)
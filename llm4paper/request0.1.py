# Please install OpenAI SDK first: `pip3 install openai`
from openai import OpenAI
import yaml
import os
import textract  # 核心依赖：处理多种格式
import pdfplumber  # 更优的PDF处理
from docx import Document  # 处理docx文件
from typing import Union
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
def extract_text(file_path: str) -> Union[str, None]:
    """
    统一提取PDF/Word文档文本
    支持格式：.pdf, .doc, .docx
    返回：提取的文本字符串 或 None（失败时）
    """
    # 验证文件是否存在
    if not os.path.isfile(file_path):
        print(f"文件不存在: {file_path}")
        return None

    # 获取文件扩展名
    ext = os.path.splitext(file_path)[1].lower()

    try:
        # PDF文件处理
        if ext == '.pdf':
            with pdfplumber.open(file_path) as pdf:
                text = '\n'.join([page.extract_text() for page in pdf.pages])
                return text

        # 新版Word文档（docx）
        elif ext == '.docx':
            doc = Document(file_path)
            return '\n'.join([para.text for para in doc.paragraphs])

        # 旧版Word文档（doc）和其他格式
        else:
            # 使用textract作为兜底方案
            raw_data = textract.process(file_path)
            # 尝试常见中文编码
            try:
                return raw_data.decode('utf-8')
            except UnicodeDecodeError:
                return raw_data.decode('gbk', errors='ignore')

    except Exception as e:
        print(f"提取失败 ({file_path}): {str(e)}")
        return None

# ===================== 使用示例 =====================
if __name__ == "__main__":
    # 测试文件路径（替换为实际路径）
    test_files = [
        r"C:\Users\sweet dream\Desktop\LLM\1-3章.pdf"
    ]

    for file in test_files:
        print(f"\n处理文件: {os.path.basename(file)}")
        content = extract_text(file)
        if content:
            print(f"提取到 {len(content)} 个字符")
            print("内容预览:", content[:200] + "...")

query = content


#load yaml

def load_prompt_from_yaml(yaml_path: str, query: str) -> str:
    with open(yaml_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    prompt_template = data['prompt']
    return prompt_template.format(query=query)

# 示例调用
prompt = load_prompt_from_yaml('prompt.yaml', query)

res = request(prompt)
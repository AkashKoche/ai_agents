from langchain.llms import Ollama

llm = Ollama(model=llama3.2:3b)

def classify(log):
    prompt = f"""
Classify thi log message into incident tags
Return JSON with tag and severity.

Log: [log]
"""

    return llm(prompt)

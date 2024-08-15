import os
from openai import AzureOpenAI
from langchain_core.messages import HumanMessage
from langchain_openai import AzureChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

os.environ["AZURE_OPENAI_API_KEY"] = "50de015aec69492ea83ecbc2c5d773c1"
os.environ["AZURE_OPENAI_ENDPOINT"] = "https://chatgptcanadaeastnew.openai.azure.com/"
os.environ["AZURE_OPENAI_API_VERSION"] = "2024-02-01"
os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"] = "gpt-4o-0513"

'''
client = AzureOpenAI(
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
  api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
  api_version="2024-02-01"
)

response = client.chat.completions.create(
    model="gpt-4o-0513", # model = "deployment_name".
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
        {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},
        {"role": "user", "content": "Do other Azure AI services support this too?"}
    ]
)

print(response.choices[0].message.content)
'''

model = AzureChatOpenAI(
    openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_deployment=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"],
    temperature=0, 
    streaming=True
)

prompt = ChatPromptTemplate.from_template("tell me a short joke about {topic}")
output_parser = StrOutputParser()

chain = prompt | model | output_parser

res = chain.invoke({"topic": "ice cream"})
print(res)

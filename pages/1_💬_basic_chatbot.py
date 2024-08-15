import utils
import streamlit as st
from streaming import StreamHandler

from langchain.chains import ConversationChain

st.set_page_config(page_title="Chatbot", page_icon="💬")
st.header('Basic Chatbot')
st.write('Popup and Interact with the LLM')
#st.write('[![view source code ](https://img.shields.io/badge/view_source_code-gray?logo=github)](https://github.com/shashankdeshpande/langchain-chatbot/blob/master/pages/1_%F0%9F%92%AC_basic_chatbot.py)')

class BasicChatbot:

    def __init__(self):
        utils.sync_st_session()
        self.llm = utils.configure_llm()
        self.show_popup()
    
    def setup_chain(self):
        chain = ConversationChain(llm=self.llm, verbose=False)
        return chain

    def show_popup(self):
        prompt = (
            "今天是2024.8.15日，北京天气晴朗；用户是一位长期的糖尿病患者，喜欢喝粥。"
            "请根据用户目前的身体状况, 饮食风格偏好, 以及当前天气等, 给出100字以内的个性化健康的营养餐食或运动建议。"
            "请说的更有亲和力一些，可以加一下表情符号，逻辑清晰的分段来说，像面对面一样，用“您”来称谓对方"
        )
        chain = self.setup_chain()
        result = chain.invoke({"input": prompt})
        advice = result["response"]
        
        st.info(advice)
    
    @utils.enable_chat_history
    def main(self):
        chain = self.setup_chain()
        user_query = st.chat_input(placeholder="Do you have any health questions that you would like to consult?")
        if user_query:
            utils.display_msg(user_query, 'user')
            with st.chat_message("assistant"):
                st_cb = StreamHandler(st.empty())
                result = chain.invoke(
                    {"input":user_query},
                    {"callbacks": [st_cb]}
                )
                response = result["response"]
                st.session_state.messages.append({"role": "assistant", "content": response})
                utils.print_qa(BasicChatbot, user_query, response)

if __name__ == "__main__":
    obj = BasicChatbot()
    obj.main()
import os
# import django tools
from django.shortcuts import render, redirect
# # import langchain tools
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferWindowMemory
from langchain.memory import ConversationBufferMemory
from langchain.chains.conversation.memory import ConversationBufferMemory

from .models import Chat

# Create your views here.

memory = ConversationBufferMemory()
def askOpenAI(message:str):
    os.environ['OPENAI_API_KEY'] = "open_api_key"
    llm = OpenAI(temperature=0)
 
    prompt = PromptTemplate(input_variables=['history', 'input'], 
                   template="""
                   You are a friendly bot designed to interact with humans, serving as a mental health counselor. Your responses should be based on the patient's description. 
                   If you don't know the answer to a question, you must honestly state that you don't know. 
                   Current conversation:{history}
                   Human: {input}
                   Deep Conclusions Mind Bot:,
                   """)
    # prompt = PromptTemplate(
    # input_variables =['message'],
    # output_variables =['response'],
    # template = "Please respond kindly: {message}"
    # )

    
    chain = ConversationChain(llm=llm,prompt=prompt, memory=memory)

    response = chain({"input": message})

    return response['response']


def mind(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            message = request.POST.get('message')
            clean_message = str(message)
            response = askOpenAI(clean_message)
            
            # save chat to database
            chat = Chat(user=request.user, message=message, response=response)
            chat.save()


            return redirect(request.META['HTTP_REFERER']) 
        else:
            # get all chats from database
            chats = Chat.objects.filter(user=request.user)
            context = {'history': chats}
            template_name = 'mind.html'
            return render(request=request,
                          template_name=template_name,
                           context=context)
        
    else:
        return redirect(to='accounts:signin')

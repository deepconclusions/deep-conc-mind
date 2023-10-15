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

from .models import Chat

# Create your views here.

def askOpenAI(message:str):
    os.environ['OPENAI_API_KEY'] = "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"
    llm = OpenAI()
    memory = ConversationBufferMemory() 

    # CoversationChain
    # chat = ConversationChain(llm=llm)
    # response = chat.run(message)

    prompt = PromptTemplate(
    input_variables =['message'],
    template = "Please respond kindly: {message}"
    )
    
    chain = LLMChain(llm=llm, prompt=prompt, memory=memory)
    response = chain.run(message)

    return response


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

import os
# import django tools
from django.shortcuts import render, redirect
# # import langchain tools
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferWindowMemory
# from langchain.memory import ConversationBufferMemory
# from langchain.chains.conversation.memory import ConversationBufferMemory
# import django decorators
from django.contrib.auth.decorators import login_required
from .models import Chat
from .models import Secret

# Create your views here.


#memory = ConversationBufferMemory()
memory_dict = {}
def askOpenAI(message:str, memory):
    os.environ['OPENAI_API_KEY'] = Secret.objects.get(name='openai_key').secret
    llm = OpenAI(temperature=0)
 
    prompt = PromptTemplate(input_variables=['history', 'input'], 
                   template="""
                   The following is a friendly conversation between a human and a Deep Conclucions Mind bot. 
                   The bot is a mental health counsellor and the answer should be based on description of the patient.
                   If the bot does not know the answer to a question, 
                   it truthfully says it does not know.\n\nCurrent conversation:\n{history}\nHuman: {input}\nDeep Conclucions Mind bot:'),
                    """)
    # prompt = PromptTemplate(
    # input_variables =['message'],
    # output_variables =['response'],
    # template = "Please respond kindly: {message}"
    # )

    
    chain = ConversationChain(llm=llm,prompt=prompt, memory=memory)

    response = chain({"input": message})

    return response['response']

@login_required(login_url='accounts:signin')
def mind(request):
    user_id = str(request.user.id)
    if user_id not in memory_dict:
        memory_dict[user_id] = ConversationBufferWindowMemory()

    if request.method == 'POST':
        message = request.POST.get('message')
        clean_message = str(message)
        response = askOpenAI(clean_message, memory_dict[user_id])
        chat = Chat(user=request.user, human=message, mind_bot=response)
        chat.save()
        return redirect(request.META['HTTP_REFERER'])
    else:
        chats = Chat.objects.filter(user=request.user)
        context = {'history': chats}
        template_name = 'mind/mind.html'
        return render(request=request, template_name=template_name, context=context)


def deleteChat(request):
    Chat.objects.filter(user=request.user).delete()
    return redirect(request.META['HTTP_REFERER']) 
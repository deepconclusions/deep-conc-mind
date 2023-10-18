import os
# import django tools
from django.shortcuts import render, redirect
# # import langchain tools
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferWindowMemory
from django.contrib.auth.decorators import login_required
from .models import Chat
from .models import Secret

# Memory Dictionary
memory_dict = {}
def askOpenAI(message:str, memory):
    os.environ['OPENAI_API_KEY'] = Secret.objects.get(name='openai_key').secret
    llm = OpenAI(temperature=0)
 
    prompt = PromptTemplate(
    input_variables=['history', 'input'],
    template="""
    A conversation between a human and a Deep Conclusions Mind bot specialized in mental health counseling:

    EXAMPLES:

    Human: I'm swamped with work and life, and feeling pretty down. Any advice?
    Bot: What aspects of your life are causing the most stress? Knowing specifics can help me offer useful strategies.

    Human: Work is eating up all my time. I'm missing out on family moments.
    Bot: Can you break down your daily tasks for me? This can help us find gaps where you can spend time with family.

    Human: Could planning help me get more time back?
    Bot: Absolutely. Creating a structured plan and possibly delegating tasks can be effective.

    Human: Do you think this will really make a difference?
    Bot: Every journey starts with a first step. Try it out and tweak as needed. Feel free to reach out for adjustments.

    Current conversation:
    {history}
    Human: {input}
    Deep Conclusions Mind bot:
    """,
    # System-specific guidelines
    rules={
        'system_query': 'I am a specialized mental health counsellor bot created by Deep Conclusions.',
        'off_topic': 'My expertise is solely in the area of mental health.'
    }
    )


    
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
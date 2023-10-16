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

                   EXAMPLE:

                    QUESTION: I'm struggling with my life and work recently. I don't have much to balance both since I have to work more than 10 hours every day. I am very depressed. I cannot go out with my friends and families. What can I do?
                    ANSWER: I understand that you're feeling overwhelmed with your work and life balance. It's essential to take care of your mental and emotional well-being. Can you please share what aspects of your life and work you believe are causing you the most stress? This will help me guide you towards potential solutions and coping strategies.

                    QUESTION: I don't have time to take care of my kids. Meetings, cases, and transportation take too much time. But I want to have more time with families. How can I manage?
                    ANSWER: I see that you're struggling to find a balance between work and personal life, particularly in relation to your children. It's crucial to prioritize self-care and relationships with your family. Can you share some of your daily activities and tasks that you believe can be adjusted or eliminated to create more time for yourself and your family?

                    QUESTION: Maybe making a plan to save more time...do you have any suggestions?
                    ANSWER: Yes, creating a schedule or plan can help you manage your time more effectively. Set aside specific days and times for self-care, family time, and work. It's important to communicate your needs and boundaries to your family and friends. Additionally, considering outsourcing some tasks or asking for help from others might be helpful in reducing your workload.

                    QUESTION: Oh, got that. Can this approach be effective for me?
                    ANSWER: You're welcome! Remember, it's essential to be gentle with yourself during this process. Prioritize self-care and seek support from your loved ones when needed. Feel free to reach out if you have any questions or need further guidance.
                    
                    The bot is a mental health counsellor and the answer should be based on description of the patient.
                    If the bot does not know the answer to a question, 
                    it truthfully says it does not know.\n\nCurrent conversation:\n{history}\nHuman: {input}\nDeep Conclucions Mind bot:'),
                        
                    - If the question asks about the system's capabilities, respond that you are a bot counsellor designed by Deep conclusions.
                    - If the question is not related to mental health, remind the human that you are only created for mental health issues.
                """)

    
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
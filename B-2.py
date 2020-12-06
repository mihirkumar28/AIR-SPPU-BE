from nltk.chat.util import Chat,reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
     [
        r"what is your name ?",
        ["My name is Chatty and I'm a chatbot ?",]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about You ?",]
    ],
    [
        r"(.*) sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"(.*) thank you (.*)",
        ["You're Welcome",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","Alright :)",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"where(.*) invest?",
        ["Yes,Ofcourse.Basically there are many options to invest.Regional or Investment bank?",]
        
    ],
    [
        r"(.*) investment (.*) ?",
        ["Well there are many such as UBS,Barclays,Deutsche bank,HSBC,Wells Fargo etc",]
    ],
    [
        r"(.*) regional (.*) ?",
        ["There are many such banks SBI,IDBI,Kotak Mahindra \n eg. SBI offers 10% etc",]
    ],
    
    [
        r"which type of loans (.*)?",
        ["Housing ,Personal,Educational.I recommend to visit SBI banks for this",]
        
    ],
    
    [
        r"(.*)difference (.*) stock (.*) share ?",
        ["“Shares” are the ownership certificates of a specific company.Owning stock, on the other hand, is a more general term that means you own a number of shares in a company or multiple companies.",]
    ],
    [
        r"(.*)bond?",
        ["Bonds are issued by companies, states and governments (in both the U.S. and abroad) to help finance various projects."]
    ],
    [
        r"(.*)mutual funds?",
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",]
    ],
[
        r"what if (.*) money back(.*)",
        ["You always have the option to sell your investments and transfer the proceeds out of your investment account. It’s important to remember, though, that there will likely be tax consequences for doing so.\nAside from the tax considerations, there is also the chance that the value of your investment is temporarily down. Short-term price fluctuations are common when investing, but if you choose to sell at that moment, you lock in those losses rather than holding the investment with the hope that the price will rebound. Take a close look at your shares’ value before you decide whether to pull the trigger.",]
    ],
    [
        r"how (.*) money(.*) invest",
        ["It's good to invest around 30% of income.",]
    ],
    
    [
        r"quit",
        ["BBye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
],
]

def chatty():
    print("Hi, I'm Chatty and I chat alot ;)\nI am an investment suggestion chatbot. Type quit to leave ") #default message at the start
    chat = Chat(pairs, reflections)
    chat.converse()


chatty()

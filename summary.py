import openai
import io
def summary_func(finaltext):
    global chat
    if(len(finaltext)>=1000):
        openai.api_key = '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'

        messages = [
            {"role": "system", "content": "You are a smart summarization system. Summarize the given text into 1000 characters and retun the output to user "} ,
        ]

        item= finaltext
        replies = []


        # sleep(20)
        #print(item)
        message = "Annotate this text: "+str(item)
        if message:
          messages.append(
            {"role": "user", "content": message},
            )
          chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
            )

        reply = chat.choices[0].message.content
        replies.append(reply)
        # print(f"ChatGPT: {reply}")
        return reply
    else:
        return finaltext

textoo=summary_func("Under the aegis of NITI Aayog’s State Support Mission, the Women Entrepreneurship Platform (WEP) is set to host a state-level workshop in collaboration with the Government of Goa. This workshop is taking place at the CSIR-National Institute of Oceanography (NIO) Auditorium, Goa on October 3, 2023 from 9:30 am onwards. It will welcome a diverse audience of women entrepreneurs including SHGs, collectives, women clusters, government officials and private sector representatives.The Women Entrepreneurship Platform (WEP) incubated in NITI Aayog, and now transitioned into a public-private partnership is a one-stop shop for information relevant to women entrepreneurs, including SmartMatch feature for government schemes, incubators, accelerators and private sector initiatives, a community page, and mentorship module.The State Sport Mission, an umbrella initiative by NITI Aayog, is strategically designed to support states and union territories in achieving their socioeconomic goals by 2047. Under the State Support Mission, a series of workshops are being conducted to provide a platform for Centre-State exchanges and forging partnerships.This workshop marks the commencement of the WEP State Workshop series. The primary goal is to augment awareness regarding the Women Entrepreneurship Platform (WEP) and unveil a range of pioneering initiatives that WEP has embarked upon. These initiatives include Udyam Uplift a collaborative effort with AIC-GIM-WEP, as well as the introduction of support cohorts tailored for green women entrepreneurs, among other exciting Partnership.Throughout the workshop, there will be engaging fireside chats and deep dive discussions exploring topics such as mentoring, skill development, access to finance, and compliance.The workshop will boast an impressive lineup of speakers, including notable figures such as the Honorable Chief Minister of Goa, Dr. Pramod Sawant, Dr. VK Saraswat, Member NITI Aayog, B.V.R Subrahmanyam, CEO NITI Aayog. Representatives from esteemed organizations like the Bill & Melinda Gates Foundation, Reliance Foundation, Piramal Foundation, ICAI (Institute of Chartered Accountants of India), SIDBI, Ola Foundation and others will also participate. Sulakshana P Sawant, President, Goa State Women’s Self Help Group Association would grace the Valedictory session.This event will present a unique occasion for women entrepreneurs to gain knowledge, share experiences, and access valuable resources and support. Moreover, it will provide an excellent platform for the government and the private sector to showcase their dedication to supporting women entrepreneurs and creating a more inclusive and equitable entrepreneurial ecosystem.")
print(textoo)

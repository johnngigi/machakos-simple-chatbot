# Define a dictionary with predefined responses
responses = {
    "hi": "Hello! Welcome to Machakos University customer service. How can I assist you today?",
    "how are you": "I'm an AI assistant, and I'm here to help you with any inquiries or concerns related to Machakos University.",
    "bye": "Thank you for contacting Machakos University customer service. Have a great day!",
    "help": "Sure, I can help you with a wide range of topics related to Machakos University, such as admission process, programs offered, tuition fees, campus facilities, and more. What specific information are you looking for?",
    "admission": "For admission-related inquiries, you can find information on our website at <a href='http://www.mksu.ac.ke' target='_blank'>www.mksu.ac.ke/admissions</a>. You can also email our admissions office at admissions@machakosuniversity.ac.ke or call us at +254 123 456 789.",
    "programs": "Machakos University offers a variety of undergraduate and graduate programs in fields such as business, engineering, arts and sciences, education, and more. You can find a complete list of our programs on our website at <a href='http://www.mksu.ac.ke' target='_blank'>www.mksu.ac.ke/academics/programs</a>.",
    "fees": "For Fee detail visit www.ksu.ac.ke",
    "location": "www.ksu.ac.ke",
    "hostel": "For hostel detail visit www.ksu.ac.ke",
    "document": "To know more about document required visit www.ksu.ac.ke",
    "floors": "has total 2 floors ",
    "syllabus": "Timetable provide direct to the students OR To know about syllabus visit www.ksu.ac.ke",
    "library": "There is one huge and spacious library.timings are 8am to 6pm and for more visit <a href='http://www.mksu.ac.ke' target='_blank'>www.mksu.ac.ke</a>",
    "infrastructure": "Our University has Excellent Infrastructure. Campus is clean. Good IT Labs With Good Speed of Internet connection",
    "canteen": "Our university has canteen with variety of food available",
    "menu": "we serve Ugali, rice, Chapati, Tea, Coffee, Soda and many more on menu",
    "placement": "To know about placement visit www.mksu.ac.ke",
    "ithod": "All engineering departments have different HOD'S ",
    "CIT": "All engineering departments have only one HOD but particularly for CIT (DR.Omuya)",
    "extchod": "Different school wise hod are different.So be more clear with your school or department",
    "University  Chancellor": " Prof.Agallo is  University  Chancellor and if you need any help then call your branch hod first.That is more appropriate",
    "sem": "Here is the Academic Calendar www.mksu.ac.ke",
    "admission": "Application can also be submitted online through the Unversity's www.mksu.ac.ke",
    "scholarship": "Many government scholarships are supported by our university. For details and updates visit www.ksu.ac.ke",
    "facilities": "Our university's Engineering department provides fully AC Lab with internet connection, smart classroom, Auditorium, library,canteen",
    "university intake": "For IT, Computer and extc 60 per branch and seat may be differ for different department.",
    "uniform": "No particular dress code",
    "committee": "For the various committe in university contact this number: 0712345678",
    "random": "I am not program for this, please ask appropriate query",
    "swear": "please use appropriate language",
    "vacation": "Academic calender is given to you by your class-soordinators after you join your respective classes",
    "sports": "Our university encourages all-round development of students and hence provides sports facilities in the campus. For more details visitwww.ksu.ac.ke",
    "salutaion": "I am glad I helped you",
    "task": "I can answer to low-intermediate questions regarding university",
    "ragging": "We are Proud to tell you that our university provides ragging free environment, and we have strict rules against ragging",
    "hod": "HODs differ for each branch, please be more specific like: (HOD it)",
    "what is the name of your developers": "Comp science 2.2 students",
    "what is the name of your creators": "Comp science 2.2 students",
    "what is the name of the developers": "Comp science 2.2 students",
    "what is the name of the creators": "Comp science 2.2 students",
    "who created you": "Comp science 2.2 students",
    "your developers": "Comp science 2.2 students",
    "your creators": "Comp science 2.2 students",
    "who are your developers": "Comp science 2.2 students",
    "developers": "Comp science 2.2 students",
    "you are made by": "Comp science 2.2 students",
    "you are made by whom": "Comp science 2.2 students",
    "who created you": "Comp science 2.2 students",
    "who create you": "Comp science 2.2 students",
    "creators": "Comp science 2.2 students",
    "who made you": "Comp science 2.2 students",
    "who designed you": "Comp science 2.2 students",
    "name": "You can call me Mind Reader.",
    "your name": "You can call me Mind Reader.",
    "do you have a name": "You can call me Mind Reader.",
    "what are you called": "You can call me Mind Reader.",
    "what is your name": "You can call me Mind Reader.",
    "what should I call you": "You can call me Mind Reader.",
    "whats your name?": "You can call me Mind Reader.",
    "what are you": "I am a Chatbot.",
    "who are you": "I am a Chatbot.",
    "who is this": "I am a Chatbot.",
    "what am i chatting to": "I am a Chatbot.",
    "who am i taking to": "I am a Chatbot.",
    "more info": "You can contact at: 0712345678",
    "contact info": "You can contact at: 0712345678",
    "how to contact university": "You can contact at: 0712345678",
    "university telephone number": "You can contact at: 0712345678",
    "university number": "You can contact at: 0712345678",
    "What is your contact no": "You can contact at: 0712345678",
    "Contact number?": "You can contact at: 0712345678",
    "how to call you": "You can contact at: 0712345678",
    "phone no?": "You can contact at: 0712345678",
    "how can i contact you": "You can contact at: 0712345678",
    "Can i get your phone number": "You can contact at: 0712345678",
    "how can i call you": "You can contact at: 0712345678",
    "phone number": "You can contact at: 0712345678",
    "phone no": "You can contact at: 0712345678",
    "call": "You can contact at: 0712345678",
    "list of courses": "Our university offers Information Technology, computer Engineering, Mechanical engineering,Chemical engineering, Civil engineering and extc Engineering.",
    "list of courses offered": "Our university offers Information Technology, computer Engineering, Mechanical engineering,Chemical engineering, Civil engineering and extc Engineering.",
    "list of courses offered in": "Our university offers Information Technology, computer Engineering, Mechanical engineering,Chemical engineering, Civil engineering and extc Engineering.",
    "what are the courses offered in your university?": "Our university offers Information Technology, computer Engineering, Mechanical engineering,Chemical engineering, Civil engineering and extc Engineering.",
    "courses?": "Our university offers Information Technology, computer Engineering, Mechanical engineering,Chemical engineering, Civil engineering and extc Engineering.",
    "courses offered": "Our university offers Information Technology, computer Engineering, Mechanical engineering,Chemical engineering, Civil engineering and extc Engineering.",
    "courses offered in (your univrsity(UNI) name)": "Our university offers Information Technology, computer Engineering, Mechanical engineering,Chemical engineering, Civil engineering and extc Engineering.",
    "courses you offer": "Our university offers Information Technology, computer Engineering, Mechanical engineering,Chemical engineering, Civil engineering and extc Engineering.",
    "branches?": "Our university offers Information Technology, computer Engineering, Mechanical engineering,Chemical engineering, Civil engineering and extc Engineering.",
    "courses available at UNI?": "Our university offers Information Technology, computer Engineering, Mechanical engineering,Chemical engineering, Civil engineering and extc Engineering.",
    "branches available at your university?": "Our university offers Information Technology, computer Engineering, Mechanical engineering,Chemical engineering, Civil engineering and extc Engineering.",
    "what are the courses in UNI?": "Our university offers Information Technology, computer Engineering, Mechanical engineering,Chemical engineering, Civil engineering and extc Engineering.",
    "what are branches in UNI?": "Our university offers Information Technology, computer Engineering, Mechanical engineering,Chemical engineering, Civil engineering and extc Engineering.",
    "what are courses in UNI?": "Our university offers Information Technology, computer Engineering, Mechanical engineering,Chemical engineering, Civil engineering and extc Engineering.",
    "branches available in UNI?": "Our university offers Information Technology, computer Engineering, Mechanical engineering,Chemical engineering, Civil engineering and extc Engineering.",
    "can you tell me the courses available in UNI?": "Our university offers Information Technology, computer Engineering, Mechanical engineering,Chemical engineering, Civil engineering and extc Engineering.",
    "can you tell me the branches available in UNI?": "Our university offers Information Technology, computer Engineering, Mechanical engineering,Chemical engineering, Civil engineering and extc Engineering.",
    "computer engineering?": "Our university offers Information Technology, computer Engineering, Mechanical engineering,Chemical engineering, Civil engineering and extc Engineering.",
    "computer": "Our university offers Information Technology, computer Engineering, Mechanical engineering,Chemical engineering, Civil engineering and extc Engineering.",
    "Computer engineering?": "Our university offers Information Technology, computer Engineering, Mechanical engineering,Chemical engineering, Civil engineering and extc Engineering.",
    "it": "Our university offers Information Technology, computer Engineering, Mechanical engineering,Chemical engineering, Civil engineering and extc Engineering.",
    "IT": "Our university offers Information Technology, computer Engineering, Mechanical engineering,Chemical engineering, Civil engineering and extc Engineering.",
    "Information Technology": "Our university offers Information Technology, computer Engineering, Mechanical engineering,Chemical engineering, Civil engineering and extc Engineering.",
    "AI/Ml": "Our university offers Information Technology, computer Engineering, Mechanical engineering,Chemical engineering, Civil engineering and extc Engineering.",
    "Mechanical engineering": "Our university offers Information Technology, computer Engineering, Mechanical engineering,Chemical engineering, Civil engineering and extc Engineering.",
    "Chemical engineering": "Our university offers Information Technology, computer Engineering, Mechanical engineering,Chemical engineering, Civil engineering and extc Engineering.",
    "Civil engineering": "Our university offers Information Technology, computer Engineering, Mechanical engineering,Chemical engineering, Civil engineering and extc Engineering."
}

# Function to get the bot response
def get_bot_response(user_input):
    # Convert the input to lowercase for case-insensitive matching
    user_input = user_input.lower()
    
    # Return the matching response if it exists, otherwise return a default response
    return responses.get(user_input, "I'm afraid I don't have enough information to answer your query. Could you please rephrase your question or provide more details?")

# Main chat loop
while True:
    user_input = input("You: ")
    
    # Check if the user wants to quit
    if user_input.lower() == "quit":
        print("Bot: Thank you for contacting Machakos University customer service. Have a great day!")
        break
    
    # Get the bot response
    response = get_bot_response(user_input)
    
    # Print the bot response
    print(f"Bot: {response}")
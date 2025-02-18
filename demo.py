import pygame, sys
from sys import exit
from button import Button, imgButton
import pygame.freetype
import textwrap


eightiesNames = ["Ivan Adames", "Tamara Davis", "Tammy Hardin-Crowe", "Lisa Pompa", "Sandy Helmkamp", "Mathew John", "Sara Wright", "Di'Nia Williams-Campbell"]
eightiesGrad = ["1988", "1988", "1988", "1988", "1989", "1989", "1989", "1989"]
eightiesOcc = ["Has traveled around the world but now settled in Chicago working at the botanical garden as a Chief Developement officer.", "Now a 6th grade english teacher for north prarie junior high.", "Now a dental office manager.", "Now a Patient Service Representative for a Community Health Center in their Dental Clinic.", "Now a teacher at ZB for Driver's Ed and PE.", "Graduated med school and became a foot/ankle surgeon.", "Now retired after working 30 years as an Athletic Trainer at Libertyville High school.", "Working professionally in music and also corporate."]
eightiesQuote = ["Life is a team sport.", "You can do anything you set your mind to.", "Don't rush growing up.", "Work Hard, Never Give Up, and Ask for help when needed. Enjoy your high school years and build lasting friendships.", "Don't waste opportunities and time. Work hard!", "Dream big and work hard.", "Make memories and get involved.", "Cultivate what your passion is."]
eightiesImg = []

ninetiesNames = ["William Johansen", "Tara Espinosa", "Becki Matteson", "Shauna Martin", "Nicole Poulson"]
ninetiesGrad = ["1991", "1993", "1998", "1998", "1999"]
ninetiesOcc = ["Recently retired from the US Marine Corps.", "Has a career as a registered nurse and is working to get a Post Master Certificate as a Family Nurse Practitioner.", "Now a physical therapist, financial counselor, and secretary of the Winthrop Harbor School Board after graduating from Carroll College.", "Currently an assistant fire chief for winthrop harbor.", "Now the administrative assistant for Dr. Brown at ZB after being a chef for 20 years."]
ninetiesQuote = ["Finish high school.", "Follow your dreams.", "You get more out of life if you put more effort into it.", "Follow your dreams even if you think they're impossible.", "Work on making yourself better every day."]
ninetiesImg = []

zerosNames = ["Sarah Haske", "Axel Owen", "Kristina Zobrist", "Ashley Wold"]
zerosGrad = ["2004", "2005", "2007", "2008"]
zerosOcc = ["Math Teacher at ZB.", "Travels the country working for political candidates big and small.", "Now a realtor for one of the top companies in Illinois.", "Volunteers in Dunesland Restoration at Illinois Beach State Park."]
zerosQuote = ["Follow your dreams no matter how long it takes.", "Don't be scared to be different.", "Enjoy high school - join clubs!", "Volunteer in your community!"]
zerosImg = []

tensNames = ["Gloria Santana", "Gina Flammini Birmingham", "Renika Morris", "Benjamin Koepsel", "Kimberly Dominguez", "Makenzie Kooi", "Jade Gree", "Nicole Duda", "Haley Taylor", "Hannah Butz", "Maddie Meyer", "Joycelynn Valencia Garcia", "Hanna Doyle", "Nicholas Whitehead", "Kailey Sherling", "Rachel Colangelo", "Rikki Vela", "Marcese Geeter Gonzales", "Jordan Buckholtz", "Lexy Fretchette", "Diana Weber", "Anna Spiering", "Sarah Mazur", "Stephanie Resendez", "Naomi Kight", "Jonel Raven Morris", "Ariel Gonsowski", "Hailey Smith", "Paul Taylor", "Blake Woods", "Jeet Bhalala", "Tristan Cook", "Samantha Hendricks", "Elliana Reynolds", "Julia Jarmon", "Rhiannon Graham", "Kylie Wright"]
tensGrad = ["2010", "2011", "2011", "2011", "2011", "2012", "2012", "2012", "2013", "2013", "2013", "2014", "2014", "2014", "2014", "2015", "2015", "2015", "2015", "2016", "2016", "2016", "2016", "2016", "2016", "2016", "2017", "2017", "2017", "2017", "2017", "2018", "2018", "2018", "2018", "2019", "2019"]
tensOcc = ["Recently graduated with a masters in public health.", "Now a lawyer after graduating from UIC Law.", "Currently a police officer.", "Now a facilities manager throughout Lake County and Kenosha.", "Active Duty Army for 10 years, now working for Child Protective Services in Texas while pursuing her dream degree of Criminology.", "Now a special ed teacher in Waukegan.", "Now works as a Global Program Advisor for a study abroad company.", "Works for an insurance company and focuses on sales. Also working towards a business strategy certificate at Harvard.","Works as a special ed teacher in Lake Villa.","A full time tattoo artist, running Hannah Banana Tattoos!","Manage the Occupational Therapy department at a level 2 trauma center.", "Working towards a clinical license in social work.", "Now a substance abuse counselor.", "Now a professional MMA fighter and coach.", "Currently an XRay technician at Frodert Hospital Pleasant Prarie.", "Now has a bachelors in communications and works for a corporate company.", "Traveled the world and currently enlisted in the US Army.", "Currently enlisted in the US Army.", "Now an ER/ICU nurse after being an EMT.", "Now a conference specialist specified in health and technology.", "Now the associate editor for the magazine department of the American Library association, fighting against book bans.", "Now lives in California, studying physical therapy.","Works as a nurse in the emergency department.","Currently working towards a PhD in healthcare at UW-Madison.", "Now an occupational therapist in the ICU section of a hospital in Arizona.", "Working toward a PhD in biomedical engineering at the University of Florida.", "Now has a degree in biology and currently working towards nursing after graduating from Augustana College.", "Currently in the US Navy and training to become a helicopter pilot.", "Now a software engineer after graduating from Carrol University.", "University of Kentucky undergraduate with a bachelor's in Human Health Sciences & a Certificate of Undergraduate Research focused on pathogenesis of periodontal disease.", "Now in 3rd year of med school at Midwestern University-Chicago College of Osteopathic Medicine.", "Now a professional sculptor and make up artist.", "Now a behavior therapist and working towards becoming a board certified behavior analyst.", "Graduated from Brown University and is now a social studies teacher in Rhode Island.", "Working towards a masters in Film and Television.", "After graduating from Illinois State University, she now has an associate degree in art, a master's in science, and is working toward a career in social work.", "Now working towards a dual degree in biology and german studies at the University of Kentucky. Also works as a part time EMT."]
tensQuote = ["Don't let anything stop you from achieving your dreams.", "Maintain perspective while you're in high school - there's more to life ahead of you.", "Stay persistent, determined, and focused.", "Building a strong work ethic now will propel you farther than you know.", "Don't let anyone tell you you can't, no matter who you are you can achieve whatever you want.", "Enjoy high school as much as possible and be involved.", "Stay focused.", "Finish high school and then further develop you education.", "Take courses that will prepare you for what you want to do.", "Do your best! Take every opportunity that comes to you!", "Be involved to open doors to your future!", "Enjoy high school while it lasts and embrace change.", "Don't do drugs - reach out for help if you need it.", "Learn from EVERYONE.", "Don't let others define you.", "High school is a place where you are able to mature into adulthood and look back at your childhood.", "It's never too late to pick a school, do a trade, or join the military.", "Stick with a plan-have a back up.", "Don't give up on your dreams.", "Always be 100% authentic.", "Have fun!", "Don't give up on your dreams.", "Enjoy your time in life, it's short.", "Don't doubt yourself - you're more capable than you think.", "Don't be afraid to try something you wanna do.", "Take all the opportunities you can.", "Try everything! You never know where you'll end up.", "Take everything one day at a time.", "Do a bunch of extracurriculars - never work at Amazon or Six Flags.", "Explore career options now! Ask questions that peak your curiosity, and find out what makes you tick.", "Learn new things everyday to find what your passionate about, and find friends that will support you.", "Do something you're passionate about, no goal is too big to achieve.", "On the path to success is where the greatest adventures lie.", "Never forget where you came from.", "Don't stress too much about the future, it will work itself out.", "Get involved!", "Research jobs and attend job fairs to help you decide what job you want to pursue."]
tensImg = []

twentiesNames = ["Jacob Pulliam", "Aiyana Loonsfoot", "Emma Paulson", "Syncere Williams", "Noah Ondo", "Isabella Diliberti", "Kylie Pankiewicz", "Leonardo Massimo"]
twentiesGrad = ["2020", "2020", "2020", "2020", "2020", "2021", "2021", "2023"]
twentiesOcc = ["Works for an HVAC company in Iowa.", "Working as a hairstylist after finishing cosmology school.", "Now an undergrad at Coastal Carolina University.", "Currently a student teacher after graduating ISU with a degree in Secondary English Education.", "Founded and currently serve as the Athletic Director for the 501(c)(3) not-for-profit Maroons Baseball Club in Zion, IL.", "Working towards a doctorate for occupational therapy at Central Michigan University.", "Working towards a bachelors degree in psychology at the University of Arizona.", "Now a full time student at Illinois State University."]
twentiesQuote = ["Don't get hung up on the little things.", "Don't fall into the wrong crowd.", "Take as many AP classes as you can.", "Stay confident in the things you wanna do.", "Do not let other people dictate your drive for success and willingness to ask for help along the way.", "The world is much bigger than Zion - but don't forget your roots :)", "Be involved in clubs and sports - be more well rounded.", "Don't procrastinate, plan for your future as early as possible."]
twentiesImg = []











BG1 = pygame.image.load("bg1.png")
BG2 = pygame.image.load("bg2.png")
BG3 = pygame.image.load("bg3.png")
BG4 = pygame.image.load("bg4.png")
BG5 = pygame.image.load("bg5.png")
BG6 = pygame.image.load("bg6.png")
pygame.init()
win_height = 800
win_width = 800
window = pygame.display.set_mode((win_width, win_height))


def quit_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
def startgame():
    global BG1
    pygame.display.set_caption("Start")

    while True:
        window.blit(BG1, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        creditButton = Button(image=pygame.image.load("creditbutton.png"), pos=(400, 400), text_input="Credits", font=get_font(60), base_color="#000000", hovering_color="#6a282cff")
        startButton = Button(image=pygame.image.load("startButton.png"), pos=(120,400), text_input= "Start", font = get_font(60), base_color="#000000", hovering_color="#6a282cff")
        quitButton = Button(image=pygame.image.load("../beginButton/quitButton.png"), pos=(680, 400),
                            text_input="Quit", font=get_font(60), base_color="#000000", hovering_color="#6a282cff")


        for button in [startButton, quitButton, creditButton]:
            button.changeColor(START_MOUSE_POS)
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if startButton.checkForInput(START_MOUSE_POS):
                    music = pygame.mixer.music.load("song.mp3"
                                                    "")
                    pygame.mixer.music.play(-1)
                    welcome()

                if quitButton.checkForInput(START_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                if creditButton.checkForInput(START_MOUSE_POS):
                    credit()
        pygame.display.update()
def credit():
    global BG6
    pygame.display.set_caption("Credits")
    while True:
        window.blit(BG6, (0,0))
        START_MOUSE_POS = pygame.mouse.get_pos()
        backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                            text_input="Back", font=get_font(60), base_color="#000000", hovering_color="#6a282cff")
        for button in [backButton]:
            button.changeColor(START_MOUSE_POS)
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if backButton.checkForInput((START_MOUSE_POS)):
                    startgame()
        pygame.display.update()

def welcome():
    global BG2
    pygame.display.set_caption("Welcome!")

    while True:
        window.blit(BG2, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        beginButton = Button(image=pygame.image.load("beginButton.png"), pos=(680,620), text_input= "Begin", font = get_font(60), base_color="#000000", hovering_color = "#6a282cff")
        backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                            text_input="Back", font=get_font(60), base_color="#000000", hovering_color="#6a282cff")



        for button in [beginButton, backButton]:
            button.changeColor(START_MOUSE_POS)
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if beginButton.checkForInput(START_MOUSE_POS):
                    zeebees()
                if backButton.checkForInput((START_MOUSE_POS)):
                    startgame()
        pygame.display.update()

def zeebees():
    global BG3
    pygame.display.set_caption("Zeebees")

    while True:
        window.blit(BG3, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        eightBees = imgButton(image=pygame.image.load("bees80.png"), pos=(685, 560))
        nineBees = imgButton(image=pygame.image.load("bees90.png"), pos=(625, 340))
        zeroBees = imgButton(image=pygame.image.load("bees00.png"), pos=(380, 355))
        tenBees = imgButton(image=pygame.image.load("bees10.png"), pos=(70, 355))
        twentyBees = imgButton(image=pygame.image.load("bees20.png"), pos=(175, 150))
        backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                            text_input="Back", font=get_font(60), base_color="#000000", hovering_color="#6a282cff")

        for button in [eightBees, nineBees, zeroBees, tenBees, twentyBees]:
            button.update(window)
        for button in [backButton]:
            button.changeColor(START_MOUSE_POS)
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if eightBees.checkForInput(START_MOUSE_POS):
                    music = pygame.mixer.music.load("80song.mp3")
                    pygame.mixer.music.play(-1)
                    eight()
                if nineBees.checkForInput(START_MOUSE_POS):
                    music = pygame.mixer.music.load("90song.mp3")
                    pygame.mixer.music.play(-1)
                    nine()
                if zeroBees.checkForInput(START_MOUSE_POS):
                    music = pygame.mixer.music.load("00song.mp3")
                    pygame.mixer.music.play(-1)
                    zero()
                if tenBees.checkForInput(START_MOUSE_POS):
                    music = pygame.mixer.music.load("10song.mp3")
                    pygame.mixer.music.play(-1)
                    ten()
                if twentyBees.checkForInput(START_MOUSE_POS):
                    music = pygame.mixer.music.load("20song.mp3")
                    pygame.mixer.music.play(-1)
                    twenty()
                if backButton.checkForInput(START_MOUSE_POS):
                    welcome()

        pygame.display.update()

def eight():
    global BG4
    pygame.display.set_caption("Class of 80's")


    while True:
        window.blit(BG4, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        bee0 = imgButton(image=pygame.image.load("bees80.png"), pos=(100, 750))
        bee1 = imgButton(image=pygame.image.load("bees80.png"), pos=(550, 250))
        bee2 = imgButton(image=pygame.image.load("bees80.png"), pos=(600, 550))
        bee3 = imgButton(image=pygame.image.load("bees80.png"), pos=(350, 300))
        bee4 = imgButton(image=pygame.image.load("bees80.png"), pos=(300, 450))
        bee5 = imgButton(image=pygame.image.load("bees80.png"), pos=(200, 200))
        bee6 = imgButton(image=pygame.image.load("bees80.png"), pos=(100, 50))
        bee7 = imgButton(image=pygame.image.load("bees80.png"), pos=(700, 700))
        backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                            text_input="Back", font=get_font(60), base_color="#000000", hovering_color="#6a282cff")

        for button in [bee0, bee1, bee2, bee3, bee4, bee5, bee6, bee7]:
            button.update(window)
        for button in [backButton]:
            button.changeColor(START_MOUSE_POS)
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 1")
                    beea()
                if bee1.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 2")
                    beeb()
                if bee2.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 3")
                    beec()
                if bee3.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 4")
                    beed()
                if bee4.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 5")
                    beee()
                if bee5.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 6")
                    beef()
                if bee6.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 7")
                    beeg()
                if bee7.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 8")
                    beeh()
                if backButton.checkForInput(START_MOUSE_POS):
                    zeebees()

        pygame.display.update()

def nine():
    global BG4
    pygame.display.set_caption("Class of 90's")


    while True:
        window.blit(BG4, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        bee0 = imgButton(image=pygame.image.load("bees90.png"), pos=(400, 350))
        bee1 = imgButton(image=pygame.image.load("bees90.png"), pos=(650, 250))
        bee2 = imgButton(image=pygame.image.load("bees90.png"), pos=(650, 550))
        bee3 = imgButton(image=pygame.image.load("bees90.png"), pos=(250, 200))
        bee4 = imgButton(image=pygame.image.load("bees90.png"), pos=(350, 600))
        backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                            text_input="Back", font=get_font(60), base_color="#000000", hovering_color="#6a282cff")

        for button in [bee0, bee1, bee2, bee3, bee4]:
            button.update(window)
        for button in [backButton]:
            button.changeColor(START_MOUSE_POS)
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 9")
                    beei()
                if bee1.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 10")
                    beej()
                if bee2.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 11")
                    beek()
                if bee3.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 12")
                    beel()
                if bee4.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 13")
                    beem()
                if backButton.checkForInput(START_MOUSE_POS):
                    zeebees()

        pygame.display.update()


def zero():
    global BG4
    pygame.display.set_caption("Class of 00's")
    while True:
        window.blit(BG4, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        bee0 = imgButton(image=pygame.image.load("bees00.png"), pos=(350, 650))
        bee1 = imgButton(image=pygame.image.load("bees00.png"), pos=(500, 300))
        bee2 = imgButton(image=pygame.image.load("bees00.png"), pos=(600, 150))
        bee3 = imgButton(image=pygame.image.load("bees00.png"), pos=(50, 750))
        backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                            text_input="Back", font=get_font(60), base_color="#000000", hovering_color="#6a282cff")

        for button in [bee0, bee1, bee2, bee3]:
            button.update(window)
        for button in [backButton]:
            button.changeColor(START_MOUSE_POS)
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 14")
                    been()
                if bee1.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 15")
                    beeo()
                if bee2.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 16")
                    beep()
                if bee3.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 17")
                    beeq()
                if backButton.checkForInput(START_MOUSE_POS):
                    zeebees()

        pygame.display.update()



def ten():
    global BG4
    pygame.display.set_caption("Class of 10's")

    while True:
        window.blit(BG4, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        bee0 = imgButton(image=pygame.image.load("bees10.png"), pos=(50, 50))
        bee1 = imgButton(image=pygame.image.load("bees10.png"), pos=(200, 75))
        bee2 = imgButton(image=pygame.image.load("bees10.png"), pos=(350, 70))
        bee3 = imgButton(image=pygame.image.load("bees10.png"), pos=(500, 45))
        bee4 = imgButton(image=pygame.image.load("bees10.png"), pos=(650, 145))
        bee5 = imgButton(image=pygame.image.load("bees10.png"), pos=(100, 170))
        bee6 = imgButton(image=pygame.image.load("bees10.png"), pos=(230, 180))
        bee7 = imgButton(image=pygame.image.load("bees10.png"), pos=(420, 220))
        bee8 = imgButton(image=pygame.image.load("bees10.png"), pos=(550, 160))
        bee9 = imgButton(image=pygame.image.load("bees10.png"), pos=(700, 240))
        bee10 = imgButton(image=pygame.image.load("bees10.png"), pos=(50,380))
        bee11 = imgButton(image=pygame.image.load("bees10.png"), pos=(220, 320))
        bee12 = imgButton(image=pygame.image.load("bees10.png"), pos=(370, 360))
        bee13 = imgButton(image=pygame.image.load("bees10.png"), pos=(520, 300))
        bee14 = imgButton(image=pygame.image.load("bees10.png"), pos=(670, 400))
        bee15 = imgButton(image=pygame.image.load("bees10.png"), pos=(90, 470))
        bee16 = imgButton(image=pygame.image.load("bees10.png"), pos=(260, 450))
        bee17 = imgButton(image=pygame.image.load("bees10.png"), pos=(410, 500))
        bee18 = imgButton(image=pygame.image.load("bees10.png"), pos=(560, 430))
        bee19 = imgButton(image=pygame.image.load("bees10.png"), pos=(710, 510))
        bee20 = imgButton(image=pygame.image.load("bees10.png"), pos=(625, 300))
        bee21 = imgButton(image=pygame.image.load("bees10.png"), pos=(250, 580))
        bee22 = imgButton(image=pygame.image.load("bees10.png"), pos=(345, 600))
        bee23 = imgButton(image=pygame.image.load("bees10.png"), pos=(510, 525))
        bee24 = imgButton(image=pygame.image.load("bees10.png"), pos=(660, 650))
        bee25 = imgButton(image=pygame.image.load("bees10.png"), pos=(100, 740))
        bee26 = imgButton(image=pygame.image.load("bees10.png"), pos=(200, 750))
        bee27 = imgButton(image=pygame.image.load("bees10.png"), pos=(420, 740))
        bee28 = imgButton(image=pygame.image.load("bees10.png"), pos=(570, 645))
        bee29 = imgButton(image=pygame.image.load("bees10.png"), pos=(720, 750))
        bee30 = imgButton(image=pygame.image.load("bees10.png"), pos=(50, 270))
        bee31 = imgButton(image=pygame.image.load("bees10.png"), pos=(325, 250))
        bee32 = imgButton(image=pygame.image.load("bees10.png"), pos=(470, 400))
        bee33 = imgButton(image=pygame.image.load("bees10.png"), pos=(620, 50))
        bee34 = imgButton(image=pygame.image.load("bees10.png"), pos=(750, 100))
        bee35 = imgButton(image=pygame.image.load("bees10.png"), pos=(300, 700))
        bee36 = imgButton(image=pygame.image.load("bees10.png"), pos=(580, 750))

        backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                            text_input="Back", font=get_font(60), base_color="#000000", hovering_color="#6a282cff")

        for button in [bee0, bee1, bee2, bee3, bee4, bee5, bee6, bee7, bee8, bee9, bee10, bee11, bee12, bee13, bee14, bee15, bee16, bee17, bee18, bee19, bee20, bee21, bee22, bee23, bee24, bee25, bee26, bee27, bee28, bee29, bee30, bee31, bee32, bee33, bee34, bee35, bee36]:
            button.update(window)
        for button in [backButton]:
            button.changeColor(START_MOUSE_POS)
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 18")
                    beer()
                if bee1.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 19")
                    bees()
                if bee2.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 20")
                    beet()
                if bee3.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 21")
                    beeu()
                if bee4.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 22")
                    beev()
                if bee5.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 23")
                    beew()
                if bee6.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 24")
                    beex()
                if bee7.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 25")
                    beey()
                if bee8.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 26")
                    beez()
                if bee9.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 27")
                    beeaa()
                if bee10.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 28")
                    beeab()
                if bee11.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 29")
                    beeac()
                if bee12.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 30")
                    beead()
                if bee13.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 31")
                    beeae()
                if bee14.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 32")
                    beeaf()
                if bee15.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 33")
                    beeag()
                if bee16.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 34")
                    beeah()
                if bee17.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 35")
                    beeai()
                if bee18.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 36")
                    beeaj()
                if bee19.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 37")
                    beeak()
                if bee20.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 38")
                    beeal()
                if bee21.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 39")
                    beeam()
                if bee22.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 40")
                    beean()
                if bee23.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 41")
                    beeao()
                if bee24.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 42")
                    beeap()
                if bee25.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 43")
                    beeaq()
                if bee26.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 44")
                    beear()
                if bee27.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 45")
                    beeas()
                if bee28.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 46")
                    beeat()
                if bee29.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 47")
                    beeau()
                if bee30.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 48")
                    beeav()
                if bee31.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 49")
                    beeaw()
                if bee32.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 50")
                    beeax()
                if bee33.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 51")
                    beeay()
                if bee34.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 52")
                    beeaz()
                if bee35.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 53")
                    beeba()
                if bee36.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 54")
                    beebb()
                if backButton.checkForInput(START_MOUSE_POS):
                    zeebees()

        pygame.display.update()



def twenty():
    global BG4
    pygame.display.set_caption("Class of 20's")

    while True:
        window.blit(BG4, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        bee0 = imgButton(image=pygame.image.load("bees20.png"), pos=(125, 50))
        bee1 = imgButton(image=pygame.image.load("bees20.png"), pos=(250, 225))
        bee2 = imgButton(image=pygame.image.load("bees20.png"), pos=(300, 475))
        bee3 = imgButton(image=pygame.image.load("bees20.png"), pos=(425, 600))
        bee4 = imgButton(image=pygame.image.load("bees20.png"), pos=(500, 150))
        bee5 = imgButton(image=pygame.image.load("bees20.png"), pos=(650, 350))
        bee6 = imgButton(image=pygame.image.load("bees20.png"), pos=(7250, 550))
        bee7 = imgButton(image=pygame.image.load("bees20.png"), pos=(600, 550))
        backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                            text_input="Back", font=get_font(60), base_color="#000000", hovering_color="#6a282cff")

        for button in [bee0, bee1, bee2, bee3, bee4, bee5, bee6, bee7]:
            button.update(window)
        for button in [backButton]:
            button.changeColor(START_MOUSE_POS)
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 9")
                    beebc()
                if bee1.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 10")
                    beebd()
                if bee2.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 11")
                    beebe()
                if bee3.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 12")
                    beebf()
                if bee4.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 13")
                    beebg()
                if bee5.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 11")
                    beebh()
                if bee6.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 12")
                    beebi()
                if bee7.checkForInput(START_MOUSE_POS):
                    pygame.display.set_caption("Zee Bee 13")
                    beebj()
                if backButton.checkForInput(START_MOUSE_POS):
                    zeebees()

        pygame.display.update()




def beea():
    global BG5
    global eightiesNames
    global eightiesGrad
    global eightiesOcc
    global eightiesQuote
    global eightiesImg
    global window
    pygame.display.set_caption("Zee Bee 1")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees80.png"), pos=(400, 400),
                        text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#000000", hovering_color="#6a282cff")


    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + eightiesNames[0]
    comText2 = comText1 + gradText
    comText3 = comText2 + eightiesGrad[0]
    comText4 = comText3 + occText
    comText5 = comText4 + eightiesOcc[0]
    comText6 = comText5 + quoteText
    comText7 = comText6 + eightiesQuote[0]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    # Wrap the text with the correct width
    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False
                    eight()

        if show_text:
            image = pygame.image.load('zeebee1.png')
            window.blit(image, (250,250))
            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()

        pygame.display.update()



def beeb():
    global BG5
    global eightiesNames
    global eightiesGrad
    global eightiesOcc
    global eightiesQuote
    global eightiesImg
    global window
    pygame.display.set_caption("Zee Bee 2")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees80.png"), pos=(400, 400),
                        text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + eightiesNames[1]
    comText2 = comText1 + gradText
    comText3 = comText2 + eightiesGrad[1]
    comText4 = comText3 + occText
    comText5 = comText4 + eightiesOcc[1]
    comText6 = comText5 + quoteText
    comText7 = comText6 + eightiesQuote[1]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    # Wrap the text with the correct width
    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False
                    eight()

        if show_text:
            image = pygame.image.load('zeebee2.png')
            window.blit(image, (200,250))
            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()

        pygame.display.update()



def beec():
    global BG5
    global eightiesNames
    global eightiesGrad
    global eightiesOcc
    global eightiesQuote
    global eightiesImg
    global window
    pygame.display.set_caption("Zee Bee 3")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees80.png"), pos=(400, 400),
                        text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + eightiesNames[2]
    comText2 = comText1 + gradText
    comText3 = comText2 + eightiesGrad[2]
    comText4 = comText3 + occText
    comText5 = comText4 + eightiesOcc[2]
    comText6 = comText5 + quoteText
    comText7 = comText6 + eightiesQuote[2]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    # Wrap the text with the correct width
    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False
                    eight()

        if show_text:
            image = pygame.image.load('zeebee3.png')
            window.blit(image, (300,250))
            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()

        pygame.display.update()


def beed():
    global BG5
    global eightiesNames
    global eightiesGrad
    global eightiesOcc
    global eightiesQuote
    global eightiesImg
    global window
    pygame.display.set_caption("Zee Bee 4")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees80.png"), pos=(400, 400),
                        text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + eightiesNames[3]
    comText2 = comText1 + gradText
    comText3 = comText2 + eightiesGrad[3]
    comText4 = comText3 + occText
    comText5 = comText4 + eightiesOcc[3]
    comText6 = comText5 + quoteText
    comText7 = comText6 + eightiesQuote[3]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    # Wrap the text with the correct width
    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False
                    eight()

        if show_text:
            image = pygame.image.load('zeebee4.png')
            window.blit(image, (250,250))
            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()

        pygame.display.update()


def beee():
    global BG5
    global eightiesNames
    global eightiesGrad
    global eightiesOcc
    global eightiesQuote
    global eightiesImg
    global window
    pygame.display.set_caption("Zee Bee 5")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees80.png"), pos=(400, 400),
                        text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + eightiesNames[4]
    comText2 = comText1 + gradText
    comText3 = comText2 + eightiesGrad[4]
    comText4 = comText3 + occText
    comText5 = comText4 + eightiesOcc[4]
    comText6 = comText5 + quoteText
    comText7 = comText6 + eightiesQuote[4]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    # Wrap the text with the correct width
    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False
                    eight()

        if show_text:
            image = pygame.image.load('zeebee5.png')
            window.blit(image, (200,250))
            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()

        pygame.display.update()


def beef():
    global BG5
    global eightiesNames
    global eightiesGrad
    global eightiesOcc
    global eightiesQuote
    global eightiesImg
    global window
    pygame.display.set_caption("Zee Bee 6")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees80.png"), pos=(400, 400),
                        text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + eightiesNames[5]
    comText2 = comText1 + gradText
    comText3 = comText2 + eightiesGrad[5]
    comText4 = comText3 + occText
    comText5 = comText4 + eightiesOcc[5]
    comText6 = comText5 + quoteText
    comText7 = comText6 + eightiesQuote[5]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    # Wrap the text with the correct width
    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False
                    eight()

        if show_text:
            image = pygame.image.load('zeebee6.png')
            window.blit(image, (180,250))
            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()

        pygame.display.update()


def beeg():
    global BG5
    global eightiesNames
    global eightiesGrad
    global eightiesOcc
    global eightiesQuote
    global eightiesImg
    global window
    pygame.display.set_caption("Zee Bee 7")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees80.png"), pos=(400, 400),
                        text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + eightiesNames[6]
    comText2 = comText1 + gradText
    comText3 = comText2 + eightiesGrad[6]
    comText4 = comText3 + occText
    comText5 = comText4 + eightiesOcc[6]
    comText6 = comText5 + quoteText
    comText7 = comText6 + eightiesQuote[6]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    # Wrap the text with the correct width
    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False
                    eight()

        if show_text:

            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()

        pygame.display.update()


def beeh():
    global BG5
    global eightiesNames
    global eightiesGrad
    global eightiesOcc
    global eightiesQuote
    global eightiesImg
    global window
    pygame.display.set_caption("Zee Bee 8")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees80.png"), pos=(400, 400),
                        text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + eightiesNames[7]
    comText2 = comText1 + gradText
    comText3 = comText2 + eightiesGrad[7]
    comText4 = comText3 + occText
    comText5 = comText4 + eightiesOcc[7]
    comText6 = comText5 + quoteText
    comText7 = comText6 + eightiesQuote[7]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    # Wrap the text with the correct width
    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False
                    eight()

        if show_text:
            image = pygame.image.load('zeebee8.png')
            window.blit(image, (200,250))
            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()

        pygame.display.update()


def beei():
    global BG5
    global ninetiesNames
    global ninetiesGrad
    global ninetiesOcc
    global ninetiesQuote
    global ninetiesImg
    global window
    pygame.display.set_caption("Zee Bee 9")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees90.png"), pos=(400, 400),
                        text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + ninetiesNames[0]
    comText2 = comText1 + gradText
    comText3 = comText2 + ninetiesGrad[0]
    comText4 = comText3 + occText
    comText5 = comText4 + ninetiesOcc[0]
    comText6 = comText5 + quoteText
    comText7 = comText6 + ninetiesQuote[0]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()


        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    nine()
        if show_text:

            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()

def beej():
    global BG5
    global ninetiesNames
    global ninetiesGrad
    global ninetiesOcc
    global ninetiesQuote
    global ninetiesImg
    global window
    pygame.display.set_caption("Zee Bee 10")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees90.png"), pos=(400, 400),
                        text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + ninetiesNames[1]
    comText2 = comText1 + gradText
    comText3 = comText2 + ninetiesGrad[1]
    comText4 = comText3 + occText
    comText5 = comText4 + ninetiesOcc[1]
    comText6 = comText5 + quoteText
    comText7 = comText6 + ninetiesQuote[1]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()


        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    nine()
        if show_text:
            image = pygame.image.load('zeebee10.png')
            window.blit(image, (300,250))
            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()

def beek():
    global BG5
    global ninetiesNames
    global ninetiesGrad
    global ninetiesOcc
    global ninetiesQuote
    global ninetiesImg
    global window
    pygame.display.set_caption("Zee Bee 11")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees90.png"), pos=(400, 400),
                        text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + ninetiesNames[2]
    comText2 = comText1 + gradText
    comText3 = comText2 + ninetiesGrad[2]
    comText4 = comText3 + occText
    comText5 = comText4 + ninetiesOcc[2]
    comText6 = comText5 + quoteText
    comText7 = comText6 + ninetiesQuote[2]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()


        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    nine()
        if show_text:

            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()

def beel():
    global BG5
    global ninetiesNames
    global ninetiesGrad
    global ninetiesOcc
    global ninetiesQuote
    global ninetiesImg
    global window
    pygame.display.set_caption("Zee Bee 12")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees90.png"), pos=(400, 400),
                        text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + ninetiesNames[3]
    comText2 = comText1 + gradText
    comText3 = comText2 + ninetiesGrad[3]
    comText4 = comText3 + occText
    comText5 = comText4 + ninetiesOcc[3]
    comText6 = comText5 + quoteText
    comText7 = comText6 + ninetiesQuote[3]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()


        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    nine()
        if show_text:
            image = pygame.image.load('zeebee12.png')
            window.blit(image, (250,250))
            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()

def beem():
    global BG5
    global ninetiesNames
    global ninetiesGrad
    global ninetiesOcc
    global ninetiesQuote
    global ninetiesImg
    global window
    pygame.display.set_caption("Zee Bee 13")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees90.png"), pos=(400, 400),
                        text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + ninetiesNames[4]
    comText2 = comText1 + gradText
    comText3 = comText2 + ninetiesGrad[4]
    comText4 = comText3 + occText
    comText5 = comText4 + ninetiesOcc[4]
    comText6 = comText5 + quoteText
    comText7 = comText6 + ninetiesQuote[4]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()


        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    nine()
        if show_text:
            image = pygame.image.load('zeebee13.png')
            window.blit(image, (250,250))
            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()

def been():
    global BG5
    global zerosNames
    global zerosGrad
    global zerosOcc
    global zerosQuote
    global zerosImg
    global window
    pygame.display.set_caption("Zee Bee 14")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees00.png"), pos=(400, 400),
                  text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + zerosNames[0]
    comText2 = comText1 + gradText
    comText3 = comText2 + zerosGrad[0]
    comText4 = comText3 + occText
    comText5 = comText4 + zerosOcc[0]
    comText6 = comText5 + quoteText
    comText7 = comText6 + zerosQuote[0]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    zero()
        if show_text:
            image = pygame.image.load('zeebee14.png')
            window.blit(image, (250, 250))
            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()

def beeo():
    global BG5
    global zerosNames
    global zerosGrad
    global zerosOcc
    global zerosQuote
    global zerosImg
    global window
    pygame.display.set_caption("Zee Bee 15")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees00.png"), pos=(400, 400),
                  text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + zerosNames[1]
    comText2 = comText1 + gradText
    comText3 = comText2 + zerosGrad[1]
    comText4 = comText3 + occText
    comText5 = comText4 + zerosOcc[1]
    comText6 = comText5 + quoteText
    comText7 = comText6 + zerosQuote[1]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    zero()
        if show_text:
            image = pygame.image.load('zeebee15.png')
            window.blit(image, (150, 250))
            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()

def beep():
    global BG5
    global zerosNames
    global zerosGrad
    global zerosOcc
    global zerosQuote
    global zerosImg
    global window
    pygame.display.set_caption("Zee Bee 16")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees00.png"), pos=(400, 400),
                  text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + zerosNames[2]
    comText2 = comText1 + gradText
    comText3 = comText2 + zerosGrad[2]
    comText4 = comText3 + occText
    comText5 = comText4 + zerosOcc[2]
    comText6 = comText5 + quoteText
    comText7 = comText6 + zerosQuote[2]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    zero()
        if show_text:
            image = pygame.image.load('zeebee16.png')
            window.blit(image, (250, 250))
            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()

def beeq():
    global BG5
    global zerosNames
    global zerosGrad
    global zerosOcc
    global zerosQuote
    global zerosImg
    global window
    pygame.display.set_caption("Zee Bee 17")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees00.png"), pos=(400, 400),
                  text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + zerosNames[3]
    comText2 = comText1 + gradText
    comText3 = comText2 + zerosGrad[3]
    comText4 = comText3 + occText
    comText5 = comText4 + zerosOcc[3]
    comText6 = comText5 + quoteText
    comText7 = comText6 + zerosQuote[3]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    zero()
        if show_text:
            image = pygame.image.load('zeebee17.png')
            window.blit(image, (250, 250))
            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()

def beer():
    global BG5
    global tensNames
    global tensGrad
    global tensOcc
    global tensQuote
    global tensImg
    global window
    pygame.display.set_caption("Zee Bee 18")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees10.png"), pos=(400, 400),
                  text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + tensNames[0]
    comText2 = comText1 + gradText
    comText3 = comText2 + tensGrad[0]
    comText4 = comText3 + occText
    comText5 = comText4 + tensOcc[0]
    comText6 = comText5 + quoteText
    comText7 = comText6 + tensQuote[0]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    ten()
        if show_text:
            image = pygame.image.load('zeebee18.png')
            window.blit(image, (250, 250))
            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()

def bees():
    global BG5
    global tensNames
    global tensGrad
    global tensOcc
    global tensQuote
    global tensImg
    global window
    pygame.display.set_caption("Zee Bee 19")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees10.png"), pos=(400, 400),
                  text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + tensNames[1]
    comText2 = comText1 + gradText
    comText3 = comText2 + tensGrad[1]
    comText4 = comText3 + occText
    comText5 = comText4 + tensOcc[1]
    comText6 = comText5 + quoteText
    comText7 = comText6 + tensQuote[1]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    ten()
        if show_text:
            image = pygame.image.load('zeebee19.png')
            window.blit(image, (80, 250))
            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()

def beet():
    global BG5
    global tensNames
    global tensGrad
    global tensOcc
    global tensQuote
    global tensImg
    global window
    pygame.display.set_caption("Zee Bee 20")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees10.png"), pos=(400, 400),
                  text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + tensNames[2]
    comText2 = comText1 + gradText
    comText3 = comText2 + tensGrad[2]
    comText4 = comText3 + occText
    comText5 = comText4 + tensOcc[2]
    comText6 = comText5 + quoteText
    comText7 = comText6 + tensQuote[2]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    ten()
        if show_text:
            image = pygame.image.load('zeebee20.png')
            window.blit(image, (330, 250))
            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()

def beeu():
    global BG5
    global tensNames
    global tensGrad
    global tensOcc
    global tensQuote
    global tensImg
    global window
    pygame.display.set_caption("Zee Bee 21")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees10.png"), pos=(400, 400),
                  text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + tensNames[3]
    comText2 = comText1 + gradText
    comText3 = comText2 + tensGrad[3]
    comText4 = comText3 + occText
    comText5 = comText4 + tensOcc[3]
    comText6 = comText5 + quoteText
    comText7 = comText6 + tensQuote[3]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    ten()
        if show_text:
            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()
def beev():
    global BG5
    global tensNames
    global tensGrad
    global tensOcc
    global tensQuote
    global tensImg
    global window
    pygame.display.set_caption("Zee Bee 22")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees10.png"), pos=(400, 400),
                  text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + tensNames[4]
    comText2 = comText1 + gradText
    comText3 = comText2 + tensGrad[4]
    comText4 = comText3 + occText
    comText5 = comText4 + tensOcc[4]
    comText6 = comText5 + quoteText
    comText7 = comText6 + tensQuote[4]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    ten()
        if show_text:
            image = pygame.image.load('zeebee22.png')
            window.blit(image, (300, 250))
            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()

def beew():
    global BG5
    global tensNames
    global tensGrad
    global tensOcc
    global tensQuote
    global tensImg
    global window
    pygame.display.set_caption("Zee Bee 23")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees10.png"), pos=(400, 400),
                  text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + tensNames[5]
    comText2 = comText1 + gradText
    comText3 = comText2 + tensGrad[5]
    comText4 = comText3 + occText
    comText5 = comText4 + tensOcc[5]
    comText6 = comText5 + quoteText
    comText7 = comText6 + tensQuote[5]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    ten()
        if show_text:
            image = pygame.image.load('zeebee23.png')
            window.blit(image, (300, 250))
            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()

def beex():
    global BG5
    global tensNames
    global tensGrad
    global tensOcc
    global tensQuote
    global tensImg
    global window
    pygame.display.set_caption("Zee Bee 24")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees10.png"), pos=(400, 400),
                  text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + tensNames[6]
    comText2 = comText1 + gradText
    comText3 = comText2 + tensGrad[6]
    comText4 = comText3 + occText
    comText5 = comText4 + tensOcc[6]
    comText6 = comText5 + quoteText
    comText7 = comText6 + tensQuote[6]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    ten()
        if show_text:
            image = pygame.image.load('zeebee24.png')
            window.blit(image, (250, 250))
            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()
def beey():
    global BG5
    global tensNames
    global tensGrad
    global tensOcc
    global tensQuote
    global tensImg
    global window
    pygame.display.set_caption("Zee Bee 25")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees10.png"), pos=(400, 400),
                  text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + tensNames[7]
    comText2 = comText1 + gradText
    comText3 = comText2 + tensGrad[7]
    comText4 = comText3 + occText
    comText5 = comText4 + tensOcc[7]
    comText6 = comText5 + quoteText
    comText7 = comText6 + tensQuote[7]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    ten()
        if show_text:
            image = pygame.image.load('zeebee25.png')
            window.blit(image, (300, 250))
            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()

def beez():
    global BG5
    global tensNames
    global tensGrad
    global tensOcc
    global tensQuote
    global tensImg
    global window
    pygame.display.set_caption("Zee Bee 26")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees10.png"), pos=(400, 400),
                  text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + tensNames[8]
    comText2 = comText1 + gradText
    comText3 = comText2 + tensGrad[8]
    comText4 = comText3 + occText
    comText5 = comText4 + tensOcc[8]
    comText6 = comText5 + quoteText
    comText7 = comText6 + tensQuote[8]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    ten()
        if show_text:
            image = pygame.image.load('zeebee26.png')
            window.blit(image, (300, 250))
            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()

def beeaa():
    global BG5
    global tensNames
    global tensGrad
    global tensOcc
    global tensQuote
    global tensImg
    global window
    pygame.display.set_caption("Zee Bee 27")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees10.png"), pos=(400, 400),
                  text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + tensNames[9]
    comText2 = comText1 + gradText
    comText3 = comText2 + tensGrad[9]
    comText4 = comText3 + occText
    comText5 = comText4 + tensOcc[9]
    comText6 = comText5 + quoteText
    comText7 = comText6 + tensQuote[9]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    ten()
        if show_text:
            image = pygame.image.load('zeebee27.png')
            window.blit(image, (280, 250))
            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()

def beeab():
    global BG5
    global tensNames
    global tensGrad
    global tensOcc
    global tensQuote
    global tensImg
    global window
    pygame.display.set_caption("Zee Bee 28")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees10.png"), pos=(400, 400),
                  text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + tensNames[10]
    comText2 = comText1 + gradText
    comText3 = comText2 + tensGrad[10]
    comText4 = comText3 + occText
    comText5 = comText4 + tensOcc[10]
    comText6 = comText5 + quoteText
    comText7 = comText6 + tensQuote[10]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    ten()
        if show_text:
            image = pygame.image.load('zeebee28.png')
            window.blit(image, (150, 250))
            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()

def beeac():
    global BG5
    global tensNames
    global tensGrad
    global tensOcc
    global tensQuote
    global tensImg
    global window
    pygame.display.set_caption("Zee Bee 29")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees10.png"), pos=(400, 400),
                  text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + tensNames[11]
    comText2 = comText1 + gradText
    comText3 = comText2 + tensGrad[11]
    comText4 = comText3 + occText
    comText5 = comText4 + tensOcc[11]
    comText6 = comText5 + quoteText
    comText7 = comText6 + tensQuote[11]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    ten()
        if show_text:
            image = pygame.image.load('zeebee29.png')
            window.blit(image, (250, 250))
            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()

def beead():
    global BG5
    global tensNames
    global tensGrad
    global tensOcc
    global tensQuote
    global tensImg
    global window
    pygame.display.set_caption("Zee Bee 30")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees10.png"), pos=(400, 400),
                  text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + tensNames[12]
    comText2 = comText1 + gradText
    comText3 = comText2 + tensGrad[12]
    comText4 = comText3 + occText
    comText5 = comText4 + tensOcc[12]
    comText6 = comText5 + quoteText
    comText7 = comText6 + tensQuote[12]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    ten()
        if show_text:
            image = pygame.image.load('zeebee30.png')
            window.blit(image, (330, 250))
            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()

def beeae():
    global BG5
    global tensNames
    global tensGrad
    global tensOcc
    global tensQuote
    global tensImg
    global window
    pygame.display.set_caption("Zee Bee 31")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees10.png"), pos=(400, 400),
                  text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + tensNames[13]
    comText2 = comText1 + gradText
    comText3 = comText2 + tensGrad[13]
    comText4 = comText3 + occText
    comText5 = comText4 + tensOcc[13]
    comText6 = comText5 + quoteText
    comText7 = comText6 + tensQuote[13]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    ten()
        if show_text:
            image = pygame.image.load('zeebee31.png')
            window.blit(image, (180, 250))
            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()

def beeaf():
    global BG5
    global tensNames
    global tensGrad
    global tensOcc
    global tensQuote
    global tensImg
    global window
    pygame.display.set_caption("Zee Bee 32")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees10.png"), pos=(400, 400),
                  text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + tensNames[14]
    comText2 = comText1 + gradText
    comText3 = comText2 + tensGrad[14]
    comText4 = comText3 + occText
    comText5 = comText4 + tensOcc[14]
    comText6 = comText5 + quoteText
    comText7 = comText6 + tensQuote[14]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    ten()
        if show_text:
            image = pygame.image.load('zeebee32.png')
            window.blit(image, (250, 250))
            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()

def beeag():
    global BG5
    global tensNames
    global tensGrad
    global tensOcc
    global tensQuote
    global tensImg
    global window
    pygame.display.set_caption("Zee Bee 33")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees10.png"), pos=(400, 400),
                  text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + tensNames[15]
    comText2 = comText1 + gradText
    comText3 = comText2 + tensGrad[15]
    comText4 = comText3 + occText
    comText5 = comText4 + tensOcc[15]
    comText6 = comText5 + quoteText
    comText7 = comText6 + tensQuote[15]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    ten()
        if show_text:
            image = pygame.image.load('zeebee33.png')
            window.blit(image, (270, 250))
            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()


def beeah():
    global BG5
    global tensNames
    global tensGrad
    global tensOcc
    global tensQuote
    global tensImg
    global window
    pygame.display.set_caption("Zee Bee 34")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees10.png"), pos=(400, 400),
                  text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + tensNames[16]
    comText2 = comText1 + gradText
    comText3 = comText2 + tensGrad[16]
    comText4 = comText3 + occText
    comText5 = comText4 + tensOcc[16]
    comText6 = comText5 + quoteText
    comText7 = comText6 + tensQuote[16]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    ten()
        if show_text:
            image = pygame.image.load('zeebee34.png')
            window.blit(image, (50, 250))
            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()

def beeai():
    global BG5
    global tensNames
    global tensGrad
    global tensOcc
    global tensQuote
    global tensImg
    global window
    pygame.display.set_caption("Zee Bee 35")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees10.png"), pos=(400, 400),
                  text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + tensNames[17]
    comText2 = comText1 + gradText
    comText3 = comText2 + tensGrad[17]
    comText4 = comText3 + occText
    comText5 = comText4 + tensOcc[17]
    comText6 = comText5 + quoteText
    comText7 = comText6 + tensQuote[17]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    ten()
        if show_text:
            image = pygame.image.load('zeebee35.png')
            window.blit(image, (280, 250))
            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()

def beeaj():
    global BG5
    global tensNames
    global tensGrad
    global tensOcc
    global tensQuote
    global tensImg
    global window
    pygame.display.set_caption("Zee Bee 36")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees10.png"), pos=(400, 400),
                  text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + tensNames[18]
    comText2 = comText1 + gradText
    comText3 = comText2 + tensGrad[18]
    comText4 = comText3 + occText
    comText5 = comText4 + tensOcc[18]
    comText6 = comText5 + quoteText
    comText7 = comText6 + tensQuote[18]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    ten()
        if show_text:
            image = pygame.image.load('zeebee36.png')
            window.blit(image, (100, 250))
            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()

def beeak():
    global BG5
    global tensNames
    global tensGrad
    global tensOcc
    global tensQuote
    global tensImg
    global window
    pygame.display.set_caption("Zee Bee 37")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees10.png"), pos=(400, 400),
                  text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + tensNames[19]
    comText2 = comText1 + gradText
    comText3 = comText2 + tensGrad[19]
    comText4 = comText3 + occText
    comText5 = comText4 + tensOcc[19]
    comText6 = comText5 + quoteText
    comText7 = comText6 + tensQuote[19]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    ten()
        if show_text:
            image = pygame.image.load('zeebee37.png')
            window.blit(image, (200, 250))
            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()

def beeal():
    global BG5
    global tensNames
    global tensGrad
    global tensOcc
    global tensQuote
    global tensImg
    global window
    pygame.display.set_caption("Zee Bee 38")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees10.png"), pos=(400, 400),
                  text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + tensNames[20]
    comText2 = comText1 + gradText
    comText3 = comText2 + tensGrad[20]
    comText4 = comText3 + occText
    comText5 = comText4 + tensOcc[20]
    comText6 = comText5 + quoteText
    comText7 = comText6 + tensQuote[20]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    ten()
        if show_text:
            image = pygame.image.load('zeebee38.png')
            window.blit(image, (150, 250))
            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()

def beeam():
    global BG5
    global tensNames
    global tensGrad
    global tensOcc
    global tensQuote
    global tensImg
    global window
    pygame.display.set_caption("Zee Bee 39")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees10.png"), pos=(400, 400),
                  text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + tensNames[21]
    comText2 = comText1 + gradText
    comText3 = comText2 + tensGrad[21]
    comText4 = comText3 + occText
    comText5 = comText4 + tensOcc[21]
    comText6 = comText5 + quoteText
    comText7 = comText6 + tensQuote[21]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    ten()
        if show_text:
            image = pygame.image.load('zeebee39.png')
            window.blit(image, (300, 250))
            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()

def beean():
    global BG5
    global tensNames
    global tensGrad
    global tensOcc
    global tensQuote
    global tensImg
    global window
    pygame.display.set_caption("Zee Bee 40")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees10.png"), pos=(400, 400),
                  text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + tensNames[22]
    comText2 = comText1 + gradText
    comText3 = comText2 + tensGrad[22]
    comText4 = comText3 + occText
    comText5 = comText4 + tensOcc[22]
    comText6 = comText5 + quoteText
    comText7 = comText6 + tensQuote[22]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    ten()
        if show_text:
            image = pygame.image.load('zeebee40.png')
            window.blit(image, (50, 250))
            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()

def beeao():
    global BG5
    global tensNames
    global tensGrad
    global tensOcc
    global tensQuote
    global tensImg
    global window
    pygame.display.set_caption("Zee Bee 41")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees10.png"), pos=(400, 400),
                  text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + tensNames[23]
    comText2 = comText1 + gradText
    comText3 = comText2 + tensGrad[23]
    comText4 = comText3 + occText
    comText5 = comText4 + tensOcc[23]
    comText6 = comText5 + quoteText
    comText7 = comText6 + tensQuote[23]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    ten()
        if show_text:

            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()

def beeap():
    global BG5
    global tensNames
    global tensGrad
    global tensOcc
    global tensQuote
    global tensImg
    global window
    pygame.display.set_caption("Zee Bee 42")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees10.png"), pos=(400, 400),
                  text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + tensNames[24]
    comText2 = comText1 + gradText
    comText3 = comText2 + tensGrad[24]
    comText4 = comText3 + occText
    comText5 = comText4 + tensOcc[24]
    comText6 = comText5 + quoteText
    comText7 = comText6 + tensQuote[24]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    ten()
        if show_text:
            image = pygame.image.load('zeebee42.png')
            window.blit(image, (300, 250))
            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()

def beeaq():
    global BG5
    global tensNames
    global tensGrad
    global tensOcc
    global tensQuote
    global tensImg
    global window
    pygame.display.set_caption("Zee Bee 43")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees10.png"), pos=(400, 400),
                  text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + tensNames[25]
    comText2 = comText1 + gradText
    comText3 = comText2 + tensGrad[25]
    comText4 = comText3 + occText
    comText5 = comText4 + tensOcc[25]
    comText6 = comText5 + quoteText
    comText7 = comText6 + tensQuote[25]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    ten()
        if show_text:
            image = pygame.image.load('zeebee43.png')
            window.blit(image, (300, 250))
            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()

def beear():
    global BG5
    global tensNames
    global tensGrad
    global tensOcc
    global tensQuote
    global tensImg
    global window
    pygame.display.set_caption("Zee Bee 44")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees10.png"), pos=(400, 400),
                  text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + tensNames[26]
    comText2 = comText1 + gradText
    comText3 = comText2 + tensGrad[26]
    comText4 = comText3 + occText
    comText5 = comText4 + tensOcc[26]
    comText6 = comText5 + quoteText
    comText7 = comText6 + tensQuote[26]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    ten()
        if show_text:

            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()

def beeas():
    global BG5
    global tensNames
    global tensGrad
    global tensOcc
    global tensQuote
    global tensImg
    global window
    pygame.display.set_caption("Zee Bee 45")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees10.png"), pos=(400, 400),
                  text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + tensNames[27]
    comText2 = comText1 + gradText
    comText3 = comText2 + tensGrad[27]
    comText4 = comText3 + occText
    comText5 = comText4 + tensOcc[27]
    comText6 = comText5 + quoteText
    comText7 = comText6 + tensQuote[27]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    ten()
        if show_text:
            image = pygame.image.load('zeebee45.png')
            window.blit(image, (60, 250))
            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()

def beeat():
    global BG5
    global tensNames
    global tensGrad
    global tensOcc
    global tensQuote
    global tensImg
    global window
    pygame.display.set_caption("Zee Bee 46")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees10.png"), pos=(400, 400),
                  text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + tensNames[28]
    comText2 = comText1 + gradText
    comText3 = comText2 + tensGrad[28]
    comText4 = comText3 + occText
    comText5 = comText4 + tensOcc[28]
    comText6 = comText5 + quoteText
    comText7 = comText6 + tensQuote[28]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    ten()
        if show_text:

            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()

def beeau():
    global BG5
    global tensNames
    global tensGrad
    global tensOcc
    global tensQuote
    global tensImg
    global window
    pygame.display.set_caption("Zee Bee 47")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees10.png"), pos=(400, 400),
                  text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + tensNames[29]
    comText2 = comText1 + gradText
    comText3 = comText2 + tensGrad[29]
    comText4 = comText3 + occText
    comText5 = comText4 + tensOcc[29]
    comText6 = comText5 + quoteText
    comText7 = comText6 + tensQuote[29]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    ten()
        if show_text:
            image = pygame.image.load('zeebee47.png')
            window.blit(image, (80, 250))
            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()

def beeav():
    global BG5
    global tensNames
    global tensGrad
    global tensOcc
    global tensQuote
    global tensImg
    global window
    pygame.display.set_caption("Zee Bee 48")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees10.png"), pos=(400, 400),
                  text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + tensNames[30]
    comText2 = comText1 + gradText
    comText3 = comText2 + tensGrad[30]
    comText4 = comText3 + occText
    comText5 = comText4 + tensOcc[30]
    comText6 = comText5 + quoteText
    comText7 = comText6 + tensQuote[30]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    ten()
        if show_text:
            image = pygame.image.load('zeebee48.png')
            window.blit(image, (300, 250))
            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()

def beeaw():
    global BG5
    global tensNames
    global tensGrad
    global tensOcc
    global tensQuote
    global tensImg
    global window
    pygame.display.set_caption("Zee Bee 49")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees10.png"), pos=(400, 400),
                  text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + tensNames[31]
    comText2 = comText1 + gradText
    comText3 = comText2 + tensGrad[31]
    comText4 = comText3 + occText
    comText5 = comText4 + tensOcc[31]
    comText6 = comText5 + quoteText
    comText7 = comText6 + tensQuote[31]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    ten()
        if show_text:
            image = pygame.image.load('zeebee49.png')
            window.blit(image, (280, 250))
            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()

def beeax():
    global BG5
    global tensNames
    global tensGrad
    global tensOcc
    global tensQuote
    global tensImg
    global window
    pygame.display.set_caption("Zee Bee 50")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees10.png"), pos=(400, 400),
                  text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + tensNames[32]
    comText2 = comText1 + gradText
    comText3 = comText2 + tensGrad[32]
    comText4 = comText3 + occText
    comText5 = comText4 + tensOcc[32]
    comText6 = comText5 + quoteText
    comText7 = comText6 + tensQuote[32]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    ten()
        if show_text:
            image = pygame.image.load('zeebee50.png')
            window.blit(image, (100, 250))
            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()

def beeay():
    global BG5
    global tensNames
    global tensGrad
    global tensOcc
    global tensQuote
    global tensImg
    global window
    pygame.display.set_caption("Zee Bee 51")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees10.png"), pos=(400, 400),
                  text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + tensNames[33]
    comText2 = comText1 + gradText
    comText3 = comText2 + tensGrad[33]
    comText4 = comText3 + occText
    comText5 = comText4 + tensOcc[33]
    comText6 = comText5 + quoteText
    comText7 = comText6 + tensQuote[33]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    ten()
        if show_text:
            image = pygame.image.load('zeebee51.png')
            window.blit(image, (150, 250))
            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()

def beeaz():
    global BG5
    global tensNames
    global tensGrad
    global tensOcc
    global tensQuote
    global tensImg
    global window
    pygame.display.set_caption("Zee Bee 52")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees10.png"), pos=(400, 400),
                  text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + tensNames[34]
    comText2 = comText1 + gradText
    comText3 = comText2 + tensGrad[34]
    comText4 = comText3 + occText
    comText5 = comText4 + tensOcc[34]
    comText6 = comText5 + quoteText
    comText7 = comText6 + tensQuote[34]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    ten()
        if show_text:
            image = pygame.image.load('zeebee52.png')
            window.blit(image, (250, 250))
            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()

def beeba():
    global BG5
    global tensNames
    global tensGrad
    global tensOcc
    global tensQuote
    global tensImg
    global window
    pygame.display.set_caption("Zee Bee 53")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees10.png"), pos=(400, 400),
                  text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + tensNames[35]
    comText2 = comText1 + gradText
    comText3 = comText2 + tensGrad[35]
    comText4 = comText3 + occText
    comText5 = comText4 + tensOcc[35]
    comText6 = comText5 + quoteText
    comText7 = comText6 + tensQuote[35]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    ten()
        if show_text:

            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()

def beebb():
    global BG5
    global tensNames
    global tensGrad
    global tensOcc
    global tensQuote
    global tensImg
    global window
    pygame.display.set_caption("Zee Bee 54")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees10.png"), pos=(400, 400),
                  text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + tensNames[36]
    comText2 = comText1 + gradText
    comText3 = comText2 + tensGrad[36]
    comText4 = comText3 + occText
    comText5 = comText4 + tensOcc[36]
    comText6 = comText5 + quoteText
    comText7 = comText6 + tensQuote[36]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    ten()
        if show_text:

            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()

def beebc():
    global BG5
    global twentiesNames
    global twentiesGrad
    global twentiesOcc
    global twentiesQuote
    global twentiesImg
    global window
    pygame.display.set_caption("Zee Bee 55")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees20.png"), pos=(400, 400),
                  text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + twentiesNames[0]
    comText2 = comText1 + gradText
    comText3 = comText2 + twentiesGrad[0]
    comText4 = comText3 + occText
    comText5 = comText4 + twentiesOcc[0]
    comText6 = comText5 + quoteText
    comText7 = comText6 + twentiesQuote[0]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    twenty()
        if show_text:

            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()

def beebd():
    global BG5
    global twentiesNames
    global twentiesGrad
    global twentiesOcc
    global twentiesQuote
    global twentiesImg
    global window
    pygame.display.set_caption("Zee Bee 56")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees20.png"), pos=(400, 400),
                  text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + twentiesNames[1]
    comText2 = comText1 + gradText
    comText3 = comText2 + twentiesGrad[1]
    comText4 = comText3 + occText
    comText5 = comText4 + twentiesOcc[1]
    comText6 = comText5 + quoteText
    comText7 = comText6 + twentiesQuote[1]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    twenty()
        if show_text:
            image = pygame.image.load('zeebee56.png')
            window.blit(image, (200, 250))
            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()

def beebe():
    global BG5
    global twentiesNames
    global twentiesGrad
    global twentiesOcc
    global twentiesQuote
    global twentiesImg
    global window
    pygame.display.set_caption("Zee Bee 57")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees20.png"), pos=(400, 400),
                  text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + twentiesNames[2]
    comText2 = comText1 + gradText
    comText3 = comText2 + twentiesGrad[2]
    comText4 = comText3 + occText
    comText5 = comText4 + twentiesOcc[2]
    comText6 = comText5 + quoteText
    comText7 = comText6 + twentiesQuote[2]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    twenty()
        if show_text:
            image = pygame.image.load('zeebee57.png')
            window.blit(image, (230, 250))
            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()

def beebf():
    global BG5
    global twentiesNames
    global twentiesGrad
    global twentiesOcc
    global twentiesQuote
    global twentiesImg
    global window
    pygame.display.set_caption("Zee Bee 58")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees20.png"), pos=(400, 400),
                  text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + twentiesNames[3]
    comText2 = comText1 + gradText
    comText3 = comText2 + twentiesGrad[3]
    comText4 = comText3 + occText
    comText5 = comText4 + twentiesOcc[3]
    comText6 = comText5 + quoteText
    comText7 = comText6 + twentiesQuote[3]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    twenty()
        if show_text:
            image = pygame.image.load('zeebee58.png')
            window.blit(image, (280, 250))
            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()

def beebg():
    global BG5
    global twentiesNames
    global twentiesGrad
    global twentiesOcc
    global twentiesQuote
    global twentiesImg
    global window
    pygame.display.set_caption("Zee Bee 59")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees20.png"), pos=(400, 400),
                  text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + twentiesNames[4]
    comText2 = comText1 + gradText
    comText3 = comText2 + twentiesGrad[4]
    comText4 = comText3 + occText
    comText5 = comText4 + twentiesOcc[4]
    comText6 = comText5 + quoteText
    comText7 = comText6 + twentiesQuote[4]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    twenty()
        if show_text:
            image = pygame.image.load('zeebee59.png')
            window.blit(image, (80, 250))
            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()

def beebh():
    global BG5
    global twentiesNames
    global twentiesGrad
    global twentiesOcc
    global twentiesQuote
    global twentiesImg
    global window
    pygame.display.set_caption("Zee Bee 60")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees20.png"), pos=(400, 400),
                  text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + twentiesNames[5]
    comText2 = comText1 + gradText
    comText3 = comText2 + twentiesGrad[5]
    comText4 = comText3 + occText
    comText5 = comText4 + twentiesOcc[5]
    comText6 = comText5 + quoteText
    comText7 = comText6 + twentiesQuote[5]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    twenty()
        if show_text:

            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()

def beebi():
    global BG5
    global twentiesNames
    global twentiesGrad
    global twentiesOcc
    global twentiesQuote
    global twentiesImg
    global window
    pygame.display.set_caption("Zee Bee 61")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees20.png"), pos=(400, 400),
                  text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + twentiesNames[6]
    comText2 = comText1 + gradText
    comText3 = comText2 + twentiesGrad[6]
    comText4 = comText3 + occText
    comText5 = comText4 + twentiesOcc[6]
    comText6 = comText5 + quoteText
    comText7 = comText6 + twentiesQuote[6]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    twenty()
        if show_text:

            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()

def beebj():
    global BG5
    global twentiesNames
    global twentiesGrad
    global twentiesOcc
    global twentiesQuote
    global twentiesImg
    global window
    pygame.display.set_caption("Zee Bee 62")

    window.blit(BG5, (0, 0))

    bee0 = Button(image=pygame.image.load("bees20.png"), pos=(400, 400),
                  text_input="", font=get_font(60), base_color="#000000", hovering_color="#000000")
    backButton = Button(image=pygame.image.load("backbutton.png"), pos=(120, 620),
                        text_input="Back", font=get_font(60), base_color="#6a282cff", hovering_color="#6a282cff")

    show_text = False

    font = get_font(30)
    nameText = "My name is "
    gradText = ". I graduated in "
    occText = ". ("
    quoteText = ") I want to tell you: "
    comText1 = nameText + twentiesNames[7]
    comText2 = comText1 + gradText
    comText3 = comText2 + twentiesGrad[7]
    comText4 = comText3 + occText
    comText5 = comText4 + twentiesOcc[7]
    comText6 = comText5 + quoteText
    comText7 = comText6 + twentiesQuote[7]
    margin = 20
    maxWidth = 93 - margin * 2  # Max width of 760 pixels

    wrappedText = textwrap.fill(comText7, width=maxWidth)

    while True:
        window.fill((0, 0, 0))
        window.blit(BG5, (0, 0))
        START_MOUSE_POS = pygame.mouse.get_pos()

        for button in [bee0, backButton]:
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee0.checkForInput(START_MOUSE_POS):
                    show_text = True

                if backButton.checkForInput(START_MOUSE_POS):
                    show_text = False

                if backButton.checkForInput(START_MOUSE_POS):
                    twenty()
        if show_text:
            yPos = margin
            # Split wrappedText into lines and display each line
            for line in wrappedText.splitlines():  # Split by lines, not words
                textSurface = font.render(line, True, (250, 250, 0))
                window.blit(textSurface, (margin, yPos))
                yPos += textSurface.get_height()
        pygame.display.update()







def get_font(size):
    return pygame.font.Font("font.ttf", size)


startgame()
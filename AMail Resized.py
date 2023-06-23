
# ---    AMail - Made by Alif Nafili    --- #
# Current time spent: 15 hours

# ---    To improve list    --- #
# - encryption


# ---    Imports    --- #        
import pygame
import random
from datetime import date
from datetime import datetime

# ---    Colours    --- #
BLACK = (33,1,36)
DARKER_GRAY = (98,106,97)
DARK_GRAY = (108,117,107)
GRAY = (147,172,181)
LIGHT_GRAY = (150,197,247)
LIGHTER_GRAY = (169,211,255)
LIGHT_LIGHTER_GRAY = (196,218,255)
WHITE = (242,244,255)

# ---    Variable Inits    --- #
button_list = []
textbox_list = []
account_list = []
email_list = []
email_buttons = []
email_recipients = []
current_user = ""
current_email = ""
emails_sent_display = []
emails_got_display = []
accounts_display = []
current_display = "Emails_Got"
current_sort = "date_made"
descending = False
page = 0
pages = 1

current_screen = "Login" # screens are: Login, Sign_Up, Main, View, Make
caps = False
wrong_password = False
invalid_email = False
invalid_password = False
wrong_recipient = False
password_show = False
recipient_added = False

# ---    Classes    --- #
class Account():
    def __init__(self,name,address,password,date_made,code):
        self.name = name
        self.address = address
        self.password = password
        self.emails_got = []
        self.emails_sent = []
        self.friends = []
        self.date_made = date_made
        self.code = code

class Email():
    def __init__(self,subject,recipients,content,sender,date_made,code):
        self.subject = subject
        self.recipients = recipients
        self.content = content
        self.sender = sender
        self.date_made = date_made
        self.code = code

class Button():
    def __init__(self,name,x,y,width,height,colour,page,alt_colour=DARK_GRAY):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.pressable = False
        self.name = name
        self.colour = colour
        self.toggle = False
        self.page = page
        self.alt_colour = alt_colour
    def do(self):
        print(self.name)
        global current_screen
        global wrong_password
        global current_user
        global password_show
        global email_recipients
        global recipient_added
        global invalid_email
        global invalid_password
        global current_sort
        global current_display
        global descending
        global page
        global current_email
        global done
        if self.name == "Login":
            for i in account_list:
                if textbox_list[0].text[0] == i.address and textbox_list[1].text[0] == i.password:
                    textbox_list[0].text[0] = ""
                    textbox_list[1].text[0] = ""
                    current_screen = "Main"
                    wrong_password = False
                    current_user = i
                    unpack()
                    break
                else:
                    wrong_password = True
        elif self.name == "To Sign Up":
            current_screen = "Sign_Up"
        elif self.name == "To Login":
            current_screen = "Login"
        elif self.name == "Sign Up":
            if textbox_list[3].text[0][-10:] == "@amail.com":
                invalid_email = False
                invalid_password = True
                big_char = False
                small_char = False
                eight_chars = False
                spec_char = False
                num = False
                for i in ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]:
                    if i in textbox_list[4].text[0]:
                        big_char = True
                        break
                for i in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
                    if i in textbox_list[4].text[0]:
                        small_char = True
                        break
                for i in ['1','2','3','4','5','6','7','8','9','0']:
                    if i in textbox_list[4].text[0]:
                        num = True
                        break
                for i in ['!','@','$','%','^','&','*','(',')','<','>','/',':',';','[','{',']','}','\\','|','?','-','+','_','=','.',',','`','~']:
                    if i in textbox_list[4].text[0]:
                        spec_char = True
                        break
                if len(textbox_list[4].text[0]) >= 8:
                    eight_chars = True
                if big_char == True and small_char == True and eight_chars == True and spec_char == True and num == True:
                    invalid_password = False
                if invalid_password == False:
                    with open("Account_List.txt", "a") as f:
                        f.write("\n")
                        f.write("\n"+textbox_list[2].text[0])
                        f.write("\n"+textbox_list[3].text[0])
                        f.write("\n"+textbox_list[4].text[0])
                        now = datetime.now()
                        f.write("\n"+now.strftime("%Y")+"-"+now.strftime("%m")+"-"+now.strftime("%d"))
                        f.write("\n"+str(len(account_list)))
                        f.close()
                    textbox_list[2].text[0] = ""
                    textbox_list[3].text[0] = ""
                    textbox_list[4].text[0] = ""
                    current_screen = "Login"
                    unpack()
            else:
                invalid_email = True
        elif self.name == "Make Email":
            current_screen = "Make"
        elif self.name == "Back to Main":
            current_screen = "Main"
        elif self.name == "Logout":
            current_screen = "Login"
            current_user = ""
        elif self.name == "Show?":
            if self.toggle == False:
                self.toggle = True
                password_show = True
            else:
                self.toggle = False
                password_show = False
        elif self.name == "Add Recipient":
            for i in account_list:
                if i.address == textbox_list[6].text[0]:
                    if len(email_recipients) == 0:
                        email_recipients.append(i)
                        textbox_list[6].text[0] = ""
                        recipient_added = True
                    else:
                        for j in email_recipients:
                            if j.code == i.code:
                                break
                            else:
                                email_recipients.append(i)
                                textbox_list[6].text[0] = ""
                                recipient_added = True
                    break
        elif self.name == "Reset":
            textbox_list[5].text[0] = ""
            textbox_list[6].text[0] = ""
            for i in range(len(textbox_list[7].text)):
                textbox_list[7].text[i] = ""
            email_recipients = []
        elif self.name == "Submit Email":
            if email_recipients == []:
                pass
            else:
                recipient_added = False
                with open("Email_List.txt","a") as f:
                    f.write("\n")
                    f.write("\n"+textbox_list[5].text[0])
                    recipients = ""
                    for i in email_recipients:
                        recipients = recipients + str(i.code) + ","
                    recipients = recipients[:len(recipients)-1]
                    f.write("\n"+recipients)
                    content = ""
                    for i in textbox_list[7].text:
                        content = content + i
                    f.write("\n"+content)
                    f.write("\n"+str(current_user.code))
                    now = datetime.now()
                    f.write("\n"+now.strftime("%Y")+"-"+now.strftime("%m")+"-"+now.strftime("%d"))
                    f.write("\n"+str(len(email_list)))
                    f.close()
                textbox_list[5].text[0] = ""
                textbox_list[6].text[0] = ""
                for i in range(len(textbox_list[7].text)):
                    textbox_list[7].text[i] = ""
                email_recipients = []
                unpack()
                current_screen = "Main"
        elif self.name == "Emails Received":
            page = 0
            current_display = "Emails_Got"
            self.toggle = True
            button_list[8].toggle = False
            button_list[9].toggle = False
            current_sort = "date_made"
            emails_got_sort(current_user,current_sort,descending)
        elif self.name == "Emails Sent":
            page = 0
            current_display = "Emails_Sent"
            self.toggle = True
            button_list[7].toggle = False
            button_list[9].toggle = False
            current_sort = "date_made"
            emails_sent_sort(current_user,current_sort,descending)
        elif self.name == "All accounts":
            page = 0
            current_display = "Accounts"
            self.toggle = True
            button_list[7].toggle = False
            button_list[8].toggle = False
            current_sort = "date_made"
            account_sort(current_sort,descending)
        elif self.name == "Sort by date":
            for i in range(6):
                button_list[i+11].toggle = False
            self.toggle = True
            current_sort = "date_made"
            emails_got_sort(current_user,current_sort,descending)
            emails_sent_sort(current_user,current_sort,descending)
            account_sort(current_sort,descending)
        elif self.name == "Sort by sender":
            for i in range(6):
                button_list[i+11].toggle = False
            self.toggle = True
            current_sort = "sender"
            emails_got_sort(current_user,current_sort,descending)
        elif self.name == "Sort by subject":
            for i in range(6):
                button_list[i+11].toggle = False
            self.toggle = True
            current_sort = "subject"
            emails_got_sort(current_user,current_sort,descending)
            emails_sent_sort(current_user,current_sort,descending)
        elif self.name == "Sort by name":
            for i in range(6):
                button_list[i+11].toggle = False
            self.toggle = True
            current_sort = "name"
            account_sort(current_sort,descending)
        elif self.name == "Sort by recips":
            for i in range(6):
                button_list[i+11].toggle = False
            self.toggle = True
            current_sort = "recipients"
            emails_sent_sort(current_user,current_sort,descending)
        elif self.name == "Sort by address":
            for i in range(6):
                button_list[i+11].toggle = False
            self.toggle = True
            current_sort = "address"
            account_sort(current_sort,descending)
        elif self.name == "Descending?":
            if descending == False:
                self.toggle = True
                descending = True
            else:
                self.toggle = False
                descending = False
            emails_got_sort(current_user,current_sort,descending)
            emails_sent_sort(current_user,current_sort,descending)
            account_sort(current_sort,descending)
        elif self.name == "< Prev page":
            if page == 0:
                pass
            else:
                page -= 1
        elif self.name == "Next page >":
            if page + 1 == pages:
                pass
            else:
                page += 1
        elif self in email_buttons:
            placement = email_buttons.index(self)
            if current_display == "Emails_Got":
                try:
                    current_email = emails_got_display[page*9+placement]
                    current_screen = "View"
                except:
                    pass
            elif current_display == "Emails_Sent":
                try:
                    current_email = emails_sent_display[page*9+placement]
                    current_screen = "View"
                except:
                    pass
        elif self.name == "Exit":
           done = True
           
    def draw(self):
        self.pressable = True
        if self.toggle == False:
            pygame.draw.rect(screen,self.colour,[self.x,self.y,self.width,self.height])
            font = pygame.font.SysFont('Calibri',self.height,True,False)
            text = font.render(self.name, True, BLACK)
            screen.blit(text,[self.x+5,self.y])
        else:
            pygame.draw.rect(screen,self.alt_colour,[self.x,self.y,self.width,self.height])
            font = pygame.font.SysFont('Calibri',self.height,True,False)
            text = font.render(self.name, True, WHITE)
            screen.blit(text,[self.x+5,self.y])
    def deactivate(self):
        self.pressable = False
    def initiate(self):
        self.pressable = True
       

class Textbox():
    def __init__(self,name,x,y,width,height,page,lines=1):
        self.name = name
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.pressable = False
        self.typing = False
        self.text = []
        self.lines = lines
        self.page = page
        if self.lines != 1:
            self.line_height = height // lines
            for i in range(self.lines):
                self.text.append("")
        else:
            self.text.append("")
            self.line_height = height
        self.maxchar = width // (self.line_height*0.7//1)
        self.current_line = 0
    def call(self):
        print(self.name)
    def draw(self):
        self.pressable = True
        if self.typing == True:
            pygame.draw.rect(screen,LIGHT_LIGHTER_GRAY,[self.x,self.y,self.width,self.height])
        else:
            pygame.draw.rect(screen,WHITE,[self.x,self.y,self.width,self.height])
        if self.lines == 1:
            if self.name == "Password" and password_show == False or self.name == "Add_Password" and password_show == False:
                font = pygame.font.SysFont('Calibri',self.line_height,True,False)
                text = font.render(len(self.text[0])*"*", True, BLACK)
                screen.blit(text,[self.x,self.y])
            else:
                font = pygame.font.SysFont('Calibri',self.line_height,True,False)
                text = font.render(self.text[0], True, BLACK)
                screen.blit(text,[self.x,self.y])
        else:
            font = pygame.font.SysFont('Calibri',self.line_height,True,False)
            for i in range(self.lines):
                text = font.render(self.text[i], True, BLACK)
                screen.blit(text,[self.x,self.y+i*20])
    def deactivate(self):
        self.pressable = False

def unpack():
    with open("Account_List.txt", "r") as f:
        global account_list
        account_list = []
        lines = f.readlines()
        terms = 6
        counter = len(lines) // terms + 1
        for i in range(counter):
            name = lines[i*terms].strip("\n")
            address = lines[i*terms+1].strip("\n")
            password = lines[i*terms+2].strip("\n")
            date_list = lines[i*terms+3].strip("\n").split("-")
            date_made = date(int(date_list[0]),int(date_list[1]),int(date_list[2]))
            code = int(lines[i*terms+4])
            account = Account(name,address,password,date_made,code)
            account_list.append(account)
        f.close()
    with open("Email_List.txt", "r") as f:
        global email_list
        email_list = []
        lines = f.readlines()
        terms = 7
        counter = len(lines) // terms + 1
        for i in range(counter):
            name = lines[i*terms].strip("\n")
            recipients = lines[i*terms+1].strip("\n").split(",")
            for j in range(len(recipients)):
                for k in account_list:
                    if k.code == int(recipients[j]):
                        recipients[j] = k
                        break
            content = lines[i*terms+2].strip("\n")
            sender = int(lines[i*terms+3])
            for j in account_list:
                if j.code == sender:
                    sender = j
                    break
            date_list = lines[i*terms+4].strip("\n").split("-")
            date_made = date(int(date_list[0]),int(date_list[1]),int(date_list[2]))
            code = int(lines[i*terms+5])
            email = Email(name,recipients,content,sender,date_made,code)
            email_list.append(email)
            sender.emails_sent.append(email)
            for i in recipients:
                i.emails_got.append(email)
        f.close()
    if current_user == "":
        emails_got_sort(account_list[0],current_sort,descending)
        emails_sent_sort(account_list[0],current_sort,descending)
        account_sort(current_sort,descending)
        button_list[11].toggle = True
    else:
        emails_got_sort(current_user,current_sort,descending)
        emails_sent_sort(current_user,current_sort,descending)
        account_sort(current_sort,descending)

def sort_by_date(obj):
    return obj.date_made
def sort_by_name(obj):
    return obj.name
def sort_by_address(obj):
    return obj.address
def sort_by_subject(obj):
    return obj.subject
def sort_by_recipient(obj):
    return obj.recipient[0].name
def sort_by_sender(obj):
    return obj.sender.name


def emails_got_sort(acc,sort_type,rev):
    global emails_got_display
    emails_got_display = acc.emails_got
    if sort_type == "date_made":
        emails_got_display.sort(reverse=rev,key=sort_by_date)
    elif sort_type == "sender":
        emails_got_display.sort(reverse=rev,key=sort_by_sender)
    elif sort_type == "subject":
        emails_got_display.sort(reverse=rev,key=sort_by_subject)

def emails_sent_sort(acc,sort_type,rev):
    global emails_sent_display
    emails_sent_display = acc.emails_sent
    if sort_type == "date_made":
        emails_sent_display.sort(reverse=rev,key=sort_by_date)
    if sort_type == "recipient":
        emails_sent_display.sort(reverse=rev,key=sort_by_recipient)
    if sort_type == "subject":
        emails_sent_display.sort(reverse=rev,key=sort_by_subject)
       
def account_sort(sort_type,rev):
    global account_display
    account_display = account_list
    if sort_type == "date_made":
        account_display.sort(reverse=rev,key=sort_by_date)
    if sort_type == "name":
        account_display.sort(reverse=rev,key=sort_by_name)
    if sort_type == "address":
        account_display.sort(reverse=rev,key=sort_by_address)

# ---    Button and Textbox Inits    --- #
button_list.append(Button("Login",740,600,120,40,GRAY,"Login")) #0
button_list.append(Button("To Sign Up",740,1000,240,40,GRAY,"Login"))
button_list.append(Button("Show?",1520,460,140,40,GRAY,"Login"))
button_list.append(Button("To Login", 740,1000,240,40,GRAY,"Sign_Up")) #3
button_list.append(Button("Sign Up",800,1000,160,40,GRAY,"Sign_Up"))
button_list.append(Button("Make Email",1500,140,240,40,GRAY,"Main")) #5
button_list.append(Button("Logout",320,140,160,40,GRAY,"Main"))
button_list.append(Button("Emails Received",20,240,240,30,LIGHTER_GRAY,"Main"))
button_list.append(Button("Emails Sent",20,300,240,30,LIGHTER_GRAY,"Main"))
button_list.append(Button("All accounts",20,360,240,30,LIGHTER_GRAY,"Main")) #9
button_list.append(Button("Descending?",20,480,200,30,LIGHTER_GRAY,"Main"))
button_list.append(Button("Sort by date",20,600,200,30,LIGHTER_GRAY,"Main")) #11
button_list.append(Button("Sort by sender",20,660,200,30,LIGHTER_GRAY,"Main"))
button_list.append(Button("Sort by subject",20,720,200,30,LIGHTER_GRAY,"Main"))
button_list.append(Button("Sort by name",20,660,200,30,LIGHTER_GRAY,"Main"))
button_list.append(Button("Sort by recips",20,660,200,30,LIGHTER_GRAY,"Main"))
button_list.append(Button("Sort by address",20,720,200,30,LIGHTER_GRAY,"Main"))
button_list.append(Button("< Prev page",1040,140,200,30,LIGHTER_GRAY, "Main"))
button_list.append(Button("Next page >",1260,140,200,30,LIGHTER_GRAY, "Main"))
button_list.append(Button("Back to Main",320,140,320,40,GRAY,"Make")) #19
button_list.append(Button("Submit Email",320,1000,320,40,GRAY,"Make"))
button_list.append(Button("Add Recipient",320,460,340,40,GRAY,"Make"))
button_list.append(Button("Reset",320,400,200,40,GRAY,"Make"))
button_list.append(Button("Show?",1520,520,140,40,GRAY,"Sign_Up"))
button_list.append(Button("Exit",740,900,240,40,GRAY,"Login"))#24

email_buttons.append(Button("Email 1",300,200,1460,100,WHITE,"Main")) #1
email_buttons.append(Button("Email 2",300,300,1460,100,WHITE,"Main"))
email_buttons.append(Button("Email 3",300,400,1460,100,WHITE,"Main"))
email_buttons.append(Button("Email 4",300,500,1460,100,WHITE,"Main"))
email_buttons.append(Button("Email 5",300,600,1460,100,WHITE,"Main"))
email_buttons.append(Button("Email 6",300,700,1460,100,WHITE,"Main"))
email_buttons.append(Button("Email 7",300,800,1460,100,WHITE,"Main"))
email_buttons.append(Button("Email 8",300,900,1460,100,WHITE,"Main"))
email_buttons.append(Button("Email 9",300,1000,1460,100,WHITE,"Main"))

textbox_list.append(Textbox("Address",700,400,800,40,"Login")) #0
textbox_list.append(Textbox("Password",700,460,800,40,"Login"))
textbox_list.append(Textbox("Add_Name",700,400,800,40,"Sign_Up")) #2
textbox_list.append(Textbox("Add_Address",700,460,800,40,"Sign_Up"))
textbox_list.append(Textbox("Add_Password",700,520,800,40,"Sign_Up"))
textbox_list.append(Textbox("Email_Subject",700,220,1000,40,"Make")) #5
textbox_list.append(Textbox("Email_Recipients",700,280,1000,40,"Make"))
textbox_list.append(Textbox("Email_Content",700,340,1000,720,"Make",18))

# ---    Screen Inits    --- #
pygame.init()
size = (1800,1200)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("AMail - Made by Alif Nafili")
done = False
clock = pygame.time.Clock()
unpack()
button_list[7].toggle = True

# ---    The main loop    --- #
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # --- Button detection --- #
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down = True
            init_x = x
            init_y = y
            for i in button_list:
                if i.pressable == True:
                    if x > i.x and x < i.x + i.width and y > i.y and y < i.y + i.height:
                        i.do()
            for i in email_buttons:
                if i.pressable == True:
                    if x > i.x and x < i.x + i.width and y > i.y and y < i.y + i.height:
                        i.do()
                       
        # --- Textbox hitbox detection --- #
            for i in textbox_list:
                if i.pressable == True:
                    if x > i.x and x < i.x + i.width and y > i.y and y < i.y + i.height:
                        i.call()
                        if i.typing == False:
                            for j in textbox_list:
                                j.typing = False
                            i.typing = True
                        else:
                            i.typing = False

        # --- Textbox typing code --- #
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LSHIFT and caps == False:
                caps = True
            elif event.key == pygame.K_LSHIFT and caps == True:
                caps = False
            else:
                for i in textbox_list:
                    if i.typing == True:
                        if caps == False:
                            if event.key == pygame.K_a:
                                i.text[i.current_line] = i.text[i.current_line] + "a"
                            elif event.key == pygame.K_b:
                                i.text[i.current_line] = i.text[i.current_line] + "b"
                            elif event.key == pygame.K_c:
                                i.text[i.current_line] = i.text[i.current_line] + "c"
                            elif event.key == pygame.K_d:
                                i.text[i.current_line] = i.text[i.current_line] + "d"
                            elif event.key == pygame.K_e:
                                i.text[i.current_line] = i.text[i.current_line] + "e"
                            elif event.key == pygame.K_f:
                                i.text[i.current_line] = i.text[i.current_line] + "f"
                            elif event.key == pygame.K_g:
                                i.text[i.current_line] = i.text[i.current_line] + "g"
                            elif event.key == pygame.K_h:
                                i.text[i.current_line] = i.text[i.current_line] + "h"
                            elif event.key == pygame.K_i:
                                i.text[i.current_line] = i.text[i.current_line] + "i"
                            elif event.key == pygame.K_j:
                                i.text[i.current_line] = i.text[i.current_line] + "j"
                            elif event.key == pygame.K_k:
                                i.text[i.current_line] = i.text[i.current_line] + "k"
                            elif event.key == pygame.K_l:
                                i.text[i.current_line] = i.text[i.current_line] + "l"
                            elif event.key == pygame.K_m:
                                i.text[i.current_line] = i.text[i.current_line] + "m"
                            elif event.key == pygame.K_n:
                                i.text[i.current_line] = i.text[i.current_line] + "n"
                            elif event.key == pygame.K_o:
                                i.text[i.current_line] = i.text[i.current_line] + "o"
                            elif event.key == pygame.K_p:
                                i.text[i.current_line] = i.text[i.current_line] + "p"
                            elif event.key == pygame.K_q:
                                i.text[i.current_line] = i.text[i.current_line] + "q"
                            elif event.key == pygame.K_r:
                                i.text[i.current_line] = i.text[i.current_line] + "r"
                            elif event.key == pygame.K_s:
                                i.text[i.current_line] = i.text[i.current_line] + "s"
                            elif event.key == pygame.K_t:
                                i.text[i.current_line] = i.text[i.current_line] + "t"
                            elif event.key == pygame.K_u:
                                i.text[i.current_line] = i.text[i.current_line] + "u"
                            elif event.key == pygame.K_v:
                                i.text[i.current_line] = i.text[i.current_line] + "v"
                            elif event.key == pygame.K_w:
                                i.text[i.current_line] = i.text[i.current_line] + "w"
                            elif event.key == pygame.K_x:
                                i.text[i.current_line] = i.text[i.current_line] + "x"
                            elif event.key == pygame.K_y:
                                i.text[i.current_line] = i.text[i.current_line] + "y"
                            elif event.key == pygame.K_z:
                                i.text[i.current_line] = i.text[i.current_line] + "z"
                            elif event.key == pygame.K_1:
                                i.text[i.current_line] = i.text[i.current_line] + "1"
                            elif event.key == pygame.K_2:
                                i.text[i.current_line] = i.text[i.current_line] + "2"
                            elif event.key == pygame.K_3:
                                i.text[i.current_line] = i.text[i.current_line] + "3"
                            elif event.key == pygame.K_4:
                                i.text[i.current_line] = i.text[i.current_line] + "4"
                            elif event.key == pygame.K_5:
                                i.text[i.current_line] = i.text[i.current_line] + "5"
                            elif event.key == pygame.K_6:
                                i.text[i.current_line] = i.text[i.current_line] + "6"
                            elif event.key == pygame.K_7:
                                i.text[i.current_line] = i.text[i.current_line] + "7"
                            elif event.key == pygame.K_8:
                                i.text[i.current_line] = i.text[i.current_line] + "8"
                            elif event.key == pygame.K_9:
                                i.text[i.current_line] = i.text[i.current_line] + "9"
                            elif event.key == pygame.K_0:
                                i.text[i.current_line] = i.text[i.current_line] + "0"
                            elif event.key == pygame.K_PERIOD:
                                i.text[i.current_line] = i.text[i.current_line] + "."
                            elif event.key == pygame.K_COMMA:
                                i.text[i.current_line] = i.text[i.current_line] + ","
                            elif event.key == pygame.K_SLASH:
                                i.text[i.current_line] = i.text[i.current_line] + "/"
                            elif event.key == pygame.K_BACKQUOTE:
                                i.text[i.current_line] = i.text[i.current_line] + "`"
                            elif event.key == pygame.K_SEMICOLON:
                                i.text[i.current_line] = i.text[i.current_line] + ";"
                            elif event.key == pygame.K_EQUALS:
                                i.text[i.current_line] = i.text[i.current_line] + "="
                            elif event.key == pygame.K_MINUS:
                                i.text[i.current_line] = i.text[i.current_line] + "-"
                            elif event.key == pygame.K_LEFTBRACKET:
                                i.text[i.current_line] = i.text[i.current_line] + "["
                            elif event.key == pygame.K_MINUS:
                                i.text[i.current_line] = i.text[i.current_line] + "]"
                            elif event.key == pygame.K_BACKSLASH:
                                i.text[i.current_line] = i.text[i.current_line] + "\\"
                        else:
                            if event.key == pygame.K_a:
                                i.text[i.current_line] = i.text[i.current_line] + "A"
                            elif event.key == pygame.K_b:
                                i.text[i.current_line] = i.text[i.current_line] + "B"
                            elif event.key == pygame.K_c:
                                i.text[i.current_line] = i.text[i.current_line] + "C"
                            elif event.key == pygame.K_d:
                                i.text[i.current_line] = i.text[i.current_line] + "D"
                            elif event.key == pygame.K_e:
                                i.text[i.current_line] = i.text[i.current_line] + "E"
                            elif event.key == pygame.K_f:
                                i.text[i.current_line] = i.text[i.current_line] + "F"
                            elif event.key == pygame.K_g:
                                i.text[i.current_line] = i.text[i.current_line] + "G"
                            elif event.key == pygame.K_h:
                                i.text[i.current_line] = i.text[i.current_line] + "H"
                            elif event.key == pygame.K_i:
                                i.text[i.current_line] = i.text[i.current_line] + "I"
                            elif event.key == pygame.K_j:
                                i.text[i.current_line] = i.text[i.current_line] + "J"
                            elif event.key == pygame.K_k:
                                i.text[i.current_line] = i.text[i.current_line] + "K"
                            elif event.key == pygame.K_l:
                                i.text[i.current_line] = i.text[i.current_line] + "L"
                            elif event.key == pygame.K_m:
                                i.text[i.current_line] = i.text[i.current_line] + "M"
                            elif event.key == pygame.K_n:
                                i.text[i.current_line] = i.text[i.current_line] + "N"
                            elif event.key == pygame.K_o:
                                i.text[i.current_line] = i.text[i.current_line] + "O"
                            elif event.key == pygame.K_p:
                                i.text[i.current_line] = i.text[i.current_line] + "P"
                            elif event.key == pygame.K_q:
                                i.text[i.current_line] = i.text[i.current_line] + "Q"
                            elif event.key == pygame.K_r:
                                i.text[i.current_line] = i.text[i.current_line] + "R"
                            elif event.key == pygame.K_s:
                                i.text[i.current_line] = i.text[i.current_line] + "S"
                            elif event.key == pygame.K_t:
                                i.text[i.current_line] = i.text[i.current_line] + "T"
                            elif event.key == pygame.K_u:
                                i.text[i.current_line] = i.text[i.current_line] + "U"
                            elif event.key == pygame.K_v:
                                i.text[i.current_line] = i.text[i.current_line] + "V"
                            elif event.key == pygame.K_w:
                                i.text[i.current_line] = i.text[i.current_line] + "W"
                            elif event.key == pygame.K_x:
                                i.text[i.current_line] = i.text[i.current_line] + "X"
                            elif event.key == pygame.K_y:
                                i.text[i.current_line] = i.text[i.current_line] + "Y"
                            elif event.key == pygame.K_z:
                                i.text[i.current_line] = i.text[i.current_line] + "Z"
                            elif event.key == pygame.K_1:
                                i.text[i.current_line] = i.text[i.current_line] + "!"
                            elif event.key == pygame.K_2:
                                i.text[i.current_line] = i.text[i.current_line] + "@"
                            elif event.key == pygame.K_3:
                                i.text[i.current_line] = i.text[i.current_line] + "#"
                            elif event.key == pygame.K_4:
                                i.text[i.current_line] = i.text[i.current_line] + "$"
                            elif event.key == pygame.K_5:
                                i.text[i.current_line] = i.text[i.current_line] + "%"
                            elif event.key == pygame.K_6:
                                i.text[i.current_line] = i.text[i.current_line] + "^"
                            elif event.key == pygame.K_7:
                                i.text[i.current_line] = i.text[i.current_line] + "&"
                            elif event.key == pygame.K_8:
                                i.text[i.current_line] = i.text[i.current_line] + "*"
                            elif event.key == pygame.K_9:
                                i.text[i.current_line] = i.text[i.current_line] + "("
                            elif event.key == pygame.K_0:
                                i.text[i.current_line] = i.text[i.current_line] + ")"
                            elif event.key == pygame.K_PERIOD:
                                i.text[i.current_line] = i.text[i.current_line] + ">"
                            elif event.key == pygame.K_COMMA:
                                i.text[i.current_line] = i.text[i.current_line] + "<"
                            elif event.key == pygame.K_SLASH:
                                i.text[i.current_line] = i.text[i.current_line] + "?"
                            elif event.key == pygame.K_BACKQUOTE:
                                i.text[i.current_line] = i.text[i.current_line] + "~"
                            elif event.key == pygame.K_SEMICOLON:
                                i.text[i.current_line] = i.text[i.current_line] + ":"
                            elif event.key == pygame.K_EQUALS:
                                i.text[i.current_line] = i.text[i.current_line] + "+"
                            elif event.key == pygame.K_MINUS:
                                i.text[i.current_line] = i.text[i.current_line] + "_"
                            elif event.key == pygame.K_LEFTBRACKET:
                                i.text[i.current_line] = i.text[i.current_line] + "{"
                            elif event.key == pygame.K_MINUS:
                                i.text[i.current_line] = i.text[i.current_line] + "}"
                            elif event.key == pygame.K_BACKSLASH:
                                i.text[i.current_line] = i.text[i.current_line] + "|"
                        if event.key == pygame.K_SPACE:
                            i.text[i.current_line] = i.text[i.current_line] + " "
                        if event.key == pygame.K_TAB:
                            i.text[i.current_line] = i.text[i.current_line] + "ඞ"                          
                        if event.key == pygame.K_BACKSPACE:
                            i.text[i.current_line] = i.text[i.current_line][:len(i.text[i.current_line])-1]
                        if i.lines == 1:
                            if len(i.text[i.current_line]) > i.maxchar:
                                i.text[i.current_line] = i.text[i.current_line][:len(i.text[i.current_line])-1]
                        else:
                            if len(i.text[i.current_line]) > i.maxchar:
                                if i.current_line+1 == i.lines:
                                    i.text[i.current_line] = i.text[i.current_line][:len(i.text[i.current_line])-1]
                                else:
                                    i.current_line = i.current_line + 1
                                    i.text[i.current_line] = i.text[i.current_line] + i.text[i.current_line-1][len(i.text[i.current_line])-1:]
                                    i.text[i.current_line-1] = i.text[i.current_line-1][:len(i.text[i.current_line-1])-1]
                         
                       
# ---    Mouse Init and stuff    --- #
    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]
           
# ---    Drawing Base Background    --- #
    screen.fill(LIGHTER_GRAY)
    pygame.draw.rect(screen, GRAY, [0,0,300,1200])
    pygame.draw.rect(screen, GRAY, [1760,0,40,1200])
    pygame.draw.rect(screen, DARK_GRAY, [0,1100,1800,100])
    pygame.draw.rect(screen, DARK_GRAY, [0,40,1800,80])
    pygame.draw.rect(screen, LIGHTER_GRAY, [0,0,300,40])
    pygame.draw.rect(screen, LIGHT_GRAY, [300,0,300,40])
    pygame.draw.rect(screen, LIGHTER_GRAY, [600,0,300,40])
    pygame.draw.rect(screen, LIGHT_GRAY, [900,0,300,40])
    pygame.draw.rect(screen, LIGHTER_GRAY, [1200,0,300,40])
    pygame.draw.rect(screen, LIGHT_LIGHTER_GRAY, [1500,0,300,40])
    pygame.draw.rect(screen, WHITE, [300, 60, 1480, 40])
    font = pygame.font.SysFont("Calibri",36,True,False)
    text = font.render("Made by Alif Nafili", True, BLACK)
    screen.blit(text,[1512,2])

# ---    Drawing Login Screen    --- #
    if current_screen == "Login":
        font = pygame.font.SysFont("Calibri",40,True,False)
        pygame.draw.rect(screen, GRAY, [0,0,300,40])
        text = font.render("AMail.com - Login", True, WHITE)
        screen.blit(text,[16,2])
        font = pygame.font.SysFont("Calibri",40,True,False)
        text = font.render("Email Address:", True, BLACK)
        screen.blit(text,[310,400])
        text = font.render("Password:", True, BLACK)
        screen.blit(text,[310,460])
        if wrong_password == True:
            text = font.render("Wrong email or password entered.", True, WHITE)
            screen.blit(text,[310,520])
        for i in button_list:
            if i.page == "Login":
                i.draw()
            else:
                i.deactivate()
        for i in textbox_list:
            if i.page == "Login":
                i.draw()
            else:
                i.deactivate()
        for i in email_buttons:
            i.deactivate()

# ---    Drawing Sign-Up Screen    --- #
    elif current_screen == "Sign_Up":
        font = pygame.font.SysFont("Calibri",40,True,False)
        pygame.draw.rect(screen, GRAY, [300,0,300,40])
        text = font.render("AMail.com - Sign up", True, WHITE)
        screen.blit(text,[302,2])
        font = pygame.font.SysFont("Calibri",40,True,False)
        text = font.render("Add Name:", True, BLACK)
        screen.blit(text,[310,400])
        text = font.render("Add Email Address:", True, BLACK)
        screen.blit(text,[310,460])
        text = font.render("Add Password:", True, BLACK)
        screen.blit(text,[310,520])
        if invalid_email == True:
            text = font.render("Invalid email, must end in @amail.com", True, WHITE)
            screen.blit(text,[310,640])
        if invalid_password == True:
            text = font.render("Password does not include all the criteria", True, WHITE)
            screen.blit(text,[310,640])
            text = font.render("Should include a number, lower and upper case,", True, WHITE)
            screen.blit(text,[310,700])
            text = font.render("a special character, and be at least 8 characters long.", True, WHITE)
            screen.blit(text,[310,760])
        for i in button_list:
            if i.page == "Sign_Up":
                i.draw()
            else:
                i.deactivate()
        for i in textbox_list:
            if i.page == "Sign_Up":
                i.draw()
            else:
                i.deactivate()
        for i in email_buttons:
            i.deactivate()

# ---    Drawing Main Screen    --- #
    elif current_screen == "Main":
        font = pygame.font.SysFont("Calibri",40,True,False)
        pygame.draw.rect(screen, GRAY, [600,0,300,40])
        text = font.render("AMail.com - Main", True, WHITE)
        screen.blit(text,[602,2])
        pygame.draw.rect(screen,LIGHT_GRAY, [300,120,1460,80])
        pygame.draw.rect(screen, LIGHT_LIGHTER_GRAY, [300,300,1460,100])
        pygame.draw.rect(screen, LIGHT_LIGHTER_GRAY, [300,500,1460,100])
        pygame.draw.rect(screen, LIGHT_LIGHTER_GRAY, [300,700,1460,100])
        pygame.draw.rect(screen, LIGHT_LIGHTER_GRAY, [300,900,1460,100])
        text = font.render("Hello, "+current_user.name, True, BLACK)
        screen.blit(text,[500,142])
        font = pygame.font.SysFont("Calibri",40,False,False)
        text = font.render("Page: "+str(page), True, WHITE)
        screen.blit(text,[800,142])
        for i in textbox_list:
            if i.page == "Main":
                i.draw()
            else:
                i.deactivate()
        for i in button_list:
            if i.page == "Main":
                if current_display == "Emails_Got":
                    if i in [button_list[14],button_list[15],button_list[16]]:
                        pass
                    else:
                        i.draw()
                elif current_display == "Emails_Sent":
                    if i in [button_list[14],button_list[12],button_list[16]]:
                        pass
                    else:
                        i.draw()
                elif current_display == "Accounts":
                    if i in [button_list[13],button_list[12],button_list[15]]:
                        pass
                    else:
                        i.draw()
            else:
                i.deactivate()
        for i in email_buttons:
            i.initiate()
        font = pygame.font.SysFont("Calibri",32,False,False)
        if current_display == "Emails_Got":
            pages = len(emails_got_display)//9+1
            for i in range(len(emails_got_display)%9):
                text = font.render(emails_got_display[9*page+i].subject, True, BLACK)
                screen.blit(text,[310,200+i*100+2])
                text = font.render("From: "+emails_got_display[9*page+i].sender.name, True, BLACK)
                screen.blit(text,[310,200+i*100+34])
                text = font.render(str(emails_got_display[9*page+i].sender.date_made), True, BLACK)
                screen.blit(text,[310,200+i*100+66])
        elif current_display == "Emails_Sent":
            pages = len(emails_sent_display)//9+1
            for i in range(len(emails_sent_display)%9):
                text = font.render(emails_sent_display[9*page+i].subject, True, BLACK)
                screen.blit(text,[310,200+i*100+2])
                temp = ""
                if len(emails_sent_display[i].recipients) == 1:
                    temp = emails_sent_display[i].recipients[0].name
                else:
                    for j in range(len(emails_sent_display[9*page+i].recipients)):
                        temp = temp + emails_sent_display[9*page+i].recipients[j].name + ", "
                    temp = temp[:len(temp)-2]
                text = font.render("To: "+temp, True, BLACK)
                screen.blit(text,[310,200+i*100+34])
                text = font.render(str(emails_sent_display[9*page+i].date_made), True, BLACK)
                screen.blit(text,[310,200+i*100+66])
        elif current_display == "Accounts":
            pages = len(account_display)//9+1
            for i in range(len(account_display)%9):
                text = font.render(account_display[9*page+i].name, True, BLACK)
                screen.blit(text,[310,200+i*100+10])
                text = font.render(account_display[9*page+i].address, True, BLACK)
                screen.blit(text,[310,200+i*100+34])
                text = font.render(str(account_display[9*page+i].date_made), True, BLACK)
                screen.blit(text,[310,200+i*100+66])
           

# ---    Drawing View Email Screen    --- #
    elif current_screen == "View":
        for i in button_list:
            if i.page == "View":
                i.draw()
            else:
                i.deactivate()
        for i in textbox_list:
            if i.page == "View":
                i.draw()
            else:
                i.deactivate()
        for i in email_buttons:
            i.deactivate()
        button_list[19].draw()
        font = pygame.font.SysFont("Calibri",40,True,False)
        text = font.render(current_email.subject, True, BLACK)
        screen.blit(text,[310,200])
        text = font.render("From: "+current_email.sender.name, True, BLACK)
        screen.blit(text,[310,250])
        temp = ""
        if len(current_email.recipients) == 1:
            temp = current_email.recipients[0].name
        else:
            for j in range(len(current_email.recipients)):
                temp = temp + current_email.recipients[j].name + ", "
            temp = temp[:len(temp)-2]
        text = font.render("To: "+temp, True, BLACK)
        screen.blit(text,[310,300])
        lines = len(current_email.content)//595
        for i in range(lines):
            text = current_email.content[i*595:(i+1)*595]
            screen.blit(text,[310,400+i*50])
        text = font.render(current_email.content[(lines)*595:],True,BLACK)
        screen.blit(text,[310,400+(lines)*50])

# ---    Drawing Make Email Screen    --- #
    elif current_screen == "Make":
        font = pygame.font.SysFont("Calibri",40,True,False)
        pygame.draw.rect(screen,LIGHT_GRAY, [300,120,1460,80])
        pygame.draw.rect(screen, GRAY, [1200,0,300,40])
        text = font.render("AMail.com - Make", True, WHITE)
        screen.blit(text,[1200,2])
        text = font.render("Email Subject:", True, BLACK)
        screen.blit(text,[310,222])
        text = font.render("Email Recipients:", True, BLACK)
        screen.blit(text,[310,282])
        text = font.render("Email Content:", True, BLACK)
        screen.blit(text,[310,342])
        for i in button_list:
            if i.page == "Make":
                i.draw()
            else:
                i.deactivate()
        for i in textbox_list:
            if i.page == "Make":
                i.draw()
            else:
                i.deactivate()
        for i in email_buttons:
            i.deactivate()
        font = pygame.font.SysFont("Calibri",24,False,False)
        if recipient_added == True:
            text = font.render(email_recipients[-1].address, True, WHITE)
            screen.blit(text,[2,222])
            text = font.render("added to recipient list.", True, WHITE)
            screen.blit(text,[2,246])
            text = font.render("Leave blank if no more to add.", True, WHITE)
            screen.blit(text,[2,270])
        else:
            text = font.render("Remember to press the", True, WHITE)
            screen.blit(text,[2,222])
            text = font.render("\"Add Recipient\" button to", True, WHITE)
            screen.blit(text,[2,246])
            text = font.render("add a recipient.", True, WHITE)
            screen.blit(text,[2,270])

# ---    End codes    --- #
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
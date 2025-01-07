class MenuElement:
    def __init__(self, name, text, active):
        self.name = name
        self.text = text
        self.active = active

menuList = []

menuList.append(MenuElement("back", "Zpět", False))
menuList.append(MenuElement("poweroff", "Vypnout", False))
menuList.append(MenuElement("restart", "Restartovat", False))
menuList.append(MenuElement("test1", "Test 1", False))
menuList.append(MenuElement("test2", "Test 2", False))

menuSelection = 1

numberOfLines = 3

i = 0
while i < numberOfLines:
    menuList[i].active = True
    i=i+1

def moveSelection(way):
    # up = 1, down=0
    global menuSelection
    if way == 0:
        if menuSelection < len(menuList) and menuList[menuSelection].active is False:
           menuList[menuSelection].active = True
           menuList[menuSelection-numberOfLines].active = False
        menuSelection = menuSelection + 1
        menuDisplay()
    if way == 1:
        print(menuList[menuSelection-2].active)
        if menuSelection-1 >= 1 and menuList[menuSelection-2].active is False:
           menuList[menuSelection-2].active = True
           menuList[menuSelection+numberOfLines-2].active = False
        menuSelection = menuSelection - 1
        menuDisplay()

def menuDisplay():
    global menuSelection
    print(menuSelection)
    i = 0
    for element in menuList:
        i = i+1
        if element.active is True and i == menuSelection:
            print("> " + element.text)
        if element.active is True and i != menuSelection:
            print(element.text)

        
    scrollMenu()
        
def scrollMenu():
    global menuSelection
    menuInput = input()
    if menuInput == "s" and menuSelection < len(menuList):
        moveSelection(0)
    if menuInput == "w" and menuSelection > 1:
        moveSelection(1)
    else:
        menuDisplay()
menuDisplay()
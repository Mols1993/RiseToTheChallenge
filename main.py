import tkinter as tk
from tkinter import ttk
import math
import random
import PIL.Image
import PIL.ImageTk

def generateChallenge():
    monsterSelection = []
    for i in monsterCheckboxes:
        if(i[1].get() == 1):
            monsterSelection.append(i[0].cget("text"))
    
    weaponSelection = []
    for i in weaponCheckboxes:
        if(i[1].get() == 1):
            weaponSelection.append(i[0].cget("text"))

    challengeSelection = []
    for i in challengeCheckboxes:
        if(i[1].get() == 1):
            challengeSelection.append(i[0].cget("text"))

    monster = monsterSelection[random.randint(0, len(monsterSelection) - 1)]

    monsterImg = ""
    for i in monsterList:
        if(monster == i[0]):
            monsterImg = i[1]

    weapon = weaponSelection[random.randint(0, len(weaponSelection) - 1)]

    weaponImg = ""
    for i in weaponList:
        if(weapon == i[0]):
            weaponImg = i[1]

    #Get weapon ID, to filter compatible challenges
    weaponID = 0
    for i in weaponList:
        if(weapon == i[0]):
            weaponID = weaponList.index(i)

    #[Challenge name, ID's to filter compatible weapons, non-compatible challenges by ID]
    compatibleChallenges = []
    for i in challengeList:
        if(weaponID in i[1] and i[0] in challengeSelection):
            compatibleChallenges.append(i)

    challenges = []
    random.shuffle(compatibleChallenges)
    for i in range(min(challengeNumberSlider.get(), len(compatibleChallenges))):
        if(compatibleChallenges[0][0] == "Switch skills randomizer"):
            compatibleChallenges[0][0] = "Switch skills randomizer: " + str(random.randint(1,2)) + " - " + str(random.randint(1,2)) + " - " + str(random.randint(1,2))
        challenges.append(compatibleChallenges[0][0])

        for j in compatibleChallenges[0][2]:
            for k in compatibleChallenges:
                if(k[1] == j):
                    compatibleChallenges.remove(k)
        
        compatibleChallenges.pop(0)
        if(len(compatibleChallenges) == 0):
            break

    challengeWindow(monster, monsterImg, weapon, weaponImg, challenges)

def challengeWindow(monster, monsterImg, weapon, weaponImg, challenges):
    root = tk.Toplevel()
    root.minsize(300, 200)
    root.title("Challenge")
    frame = tk.Frame(root, borderwidth = 5, relief = tk.GROOVE)
    monsterLabel = tk.Label(frame, text = "Monster:", font=("arial", 20))
    monsterSelected = tk.Label(frame, text = monster)

    monsterImage = tk.Label(frame, image = monsterImg)

    weaponLabel = tk.Label(frame, text = "Weapon:", font=("arial", 20))
    weaponSelected = tk.Label(frame, text = weapon)

    weaponImage = tk.Label(frame, image = weaponImg)

    challengesText = "\n".join(challenges)
    challengeLabel = tk.Label(frame, text = "Challenges:", font=("arial", 20))
    challengeSelected = tk.Label(frame, text = challengesText)

    frame.pack()
    monsterLabel.pack()
    monsterImage.pack()
    monsterSelected.pack()
    weaponLabel.pack()
    weaponImage.pack()
    weaponSelected.pack()
    challengeLabel.pack()
    challengeSelected.pack()

def changeAll(list, state):
    if(state == "enable"):
        for i in list:
            i[0].select()
    else:
        for i in list:
            i[0].deselect()

root = tk.Tk()
root.geometry("+50+50")
root.title("Rise to the Challenge")
root.minsize(1600, 870)
#root.state("zoomed")

#[Monster name, image icon]
monsterList = [
    ["Aknosom", PIL.ImageTk.PhotoImage(PIL.Image.open("images/aknosom.png"))], 
	["Almudron", PIL.ImageTk.PhotoImage(PIL.Image.open("images/almudron.png"))], 
	["Anjanath", PIL.ImageTk.PhotoImage(PIL.Image.open("images/anjanath.png"))], 
	["Arzuros", PIL.ImageTk.PhotoImage(PIL.Image.open("images/arzuros.png"))], 
	["Apex Arzuros", PIL.ImageTk.PhotoImage(PIL.Image.open("images/apexArzuros.png"))], 
	["Barioth", PIL.ImageTk.PhotoImage(PIL.Image.open("images/barioth.png"))], 
	["Barroth", PIL.ImageTk.PhotoImage(PIL.Image.open("images/barroth.png"))], 
	["Bazelgeuse", PIL.ImageTk.PhotoImage(PIL.Image.open("images/bazelgeuse.png"))], 
	["Basarios", PIL.ImageTk.PhotoImage(PIL.Image.open("images/basarios.png"))], 
	["Bishaten", PIL.ImageTk.PhotoImage(PIL.Image.open("images/bishaten.png"))], 
	["Chameleos", PIL.ImageTk.PhotoImage(PIL.Image.open("images/chameleos.png"))], 
	["Diablos", PIL.ImageTk.PhotoImage(PIL.Image.open("images/diablos.png"))], 
	["Apex Diablos", PIL.ImageTk.PhotoImage(PIL.Image.open("images/apexDiablos.png"))], 
	["Goss Harag", PIL.ImageTk.PhotoImage(PIL.Image.open("images/gossHarag.png"))], 
	["Great Baggi", PIL.ImageTk.PhotoImage(PIL.Image.open("images/greatBaggi.png"))], 
	["Great Izuchi", PIL.ImageTk.PhotoImage(PIL.Image.open("images/greatIzuchi.png"))], 
	["Great Wroggi", PIL.ImageTk.PhotoImage(PIL.Image.open("images/greatWroggi.png"))], 
	["Jyuratodus", PIL.ImageTk.PhotoImage(PIL.Image.open("images/jyuratodus.png"))], 
	["Khezu", PIL.ImageTk.PhotoImage(PIL.Image.open("images/khezu.png"))], 
	["Kulu-Ya-Ku", PIL.ImageTk.PhotoImage(PIL.Image.open("images/kuluYaKu.png"))], 
	["Kushala Daora", PIL.ImageTk.PhotoImage(PIL.Image.open("images/kushalaDaora.png"))], 
	["Lagombi", PIL.ImageTk.PhotoImage(PIL.Image.open("images/lagombi.png"))], 
	["Magnamalo", PIL.ImageTk.PhotoImage(PIL.Image.open("images/magnamalo.png"))], 
	["Mizutsune", PIL.ImageTk.PhotoImage(PIL.Image.open("images/mizutsune.png"))], 
	["Apex Mizutsune", PIL.ImageTk.PhotoImage(PIL.Image.open("images/apexMizutsune.png"))], 
	["Nargacuga", PIL.ImageTk.PhotoImage(PIL.Image.open("images/nargacuga.png"))], 
	["Pukei-Pukei", PIL.ImageTk.PhotoImage(PIL.Image.open("images/pukeiPukei.png"))], 
	["Rajang", PIL.ImageTk.PhotoImage(PIL.Image.open("images/rajang.png"))], 
	["Rakna-Kadaki", PIL.ImageTk.PhotoImage(PIL.Image.open("images/raknaKadaki.png"))], 
	["Rathalos", PIL.ImageTk.PhotoImage(PIL.Image.open("images/rathalos.png"))], 
	["Apex Rathalos", PIL.ImageTk.PhotoImage(PIL.Image.open("images/apexRathalos.png"))], 
	["Rathian", PIL.ImageTk.PhotoImage(PIL.Image.open("images/rathian.png"))], 
	["Apex Rathian", PIL.ImageTk.PhotoImage(PIL.Image.open("images/apexRathian.png"))], 
	["Royal Ludroth", PIL.ImageTk.PhotoImage(PIL.Image.open("images/royalLudroth.png"))], 
	["Somnacanth", PIL.ImageTk.PhotoImage(PIL.Image.open("images/somnacanth.png"))], 
	["Teostra", PIL.ImageTk.PhotoImage(PIL.Image.open("images/teostra.png"))], 
	["Tetranadon", PIL.ImageTk.PhotoImage(PIL.Image.open("images/tetranadon.png"))], 
	["Thunder Serpent Narwa", PIL.ImageTk.PhotoImage(PIL.Image.open("images/narwa.png"))], 
	["Tigrex", PIL.ImageTk.PhotoImage(PIL.Image.open("images/tigrex.png"))], 
	["Tobi-Kadachi", PIL.ImageTk.PhotoImage(PIL.Image.open("images/tobiKadachi.png"))], 
	["Wind Serpent Ibushi", PIL.ImageTk.PhotoImage(PIL.Image.open("images/ibushi.png"))], 
	["Volvidon", PIL.ImageTk.PhotoImage(PIL.Image.open("images/volvidon.png"))], 
	["Zinogre", PIL.ImageTk.PhotoImage(PIL.Image.open("images/zinogre.png"))]
]

#[Weapon name, ID to filter compatible challenges, image icon]
weaponList = [
    ["Greatsword", PIL.ImageTk.PhotoImage(PIL.Image.open("images/GS.png"))],
    ["Long sword", PIL.ImageTk.PhotoImage(PIL.Image.open("images/LS.png"))],
    ["Sword and shield", PIL.ImageTk.PhotoImage(PIL.Image.open("images/SnS.png"))],
    ["Dual blades", PIL.ImageTk.PhotoImage(PIL.Image.open("images/DB.png"))],
    ["Hammer", PIL.ImageTk.PhotoImage(PIL.Image.open("images/Hmr.png"))],
    ["Hunting horn", PIL.ImageTk.PhotoImage(PIL.Image.open("images/HH.png"))],
    ["Lance", PIL.ImageTk.PhotoImage(PIL.Image.open("images/Lnc.png"))],
    ["Gunlance", PIL.ImageTk.PhotoImage(PIL.Image.open("images/GL.png"))],
    ["Switch axe", PIL.ImageTk.PhotoImage(PIL.Image.open("images/SA.png"))],
    ["Charge blade", PIL.ImageTk.PhotoImage(PIL.Image.open("images/CB.png"))],
    ["Insect glaive", PIL.ImageTk.PhotoImage(PIL.Image.open("images/IG.png"))],
    ["Light bowgun", PIL.ImageTk.PhotoImage(PIL.Image.open("images/LBG.png"))],
    ["Heavy bowgun", PIL.ImageTk.PhotoImage(PIL.Image.open("images/HBG.png"))],
    ["Bow", PIL.ImageTk.PhotoImage(PIL.Image.open("images/Bow.png"))]
]

#[Challenge name, ID's to filter compatible weapons, non-compatible challenges by ID, challenge tier 1-5]
challengeList = [
    #0
    ["No wirefall", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [14], 1],
    ["Switch skills randomizer", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [], 1],
    ["No healing", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [], 3],
    ["Start with no items (Live off the land)", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [4, 34], 2],
    ["No items", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [3, 15, 34], 4],
    #5
    ["Hardcore (No carting)", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [], 3],
    ["Low rank gear", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [], 3],
    ["No dodging", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [], 2],
    ["No sharpening", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 34], 4],
    ["Only Normal 1/No Coating", [11, 12, 13], [10, 33, 34], 4],
    #10
    ["Only attack from palamute", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [12, 18, 22, 24, 25, 26, 27, 29, 32, 33], 5],
    ["Inverted controls", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [], 2],
    ["Silkbind attacks only", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [10, 13, 14], 5],
    ["No silkbind attacks", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [10, 12, 14, 34], 1],
    ["No wirebug (Play like it's MH1)", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [0, 12, 13], 2],
    #15
    ["No moving while using items (Old school flex)", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [4, 10], 3],
    ["Gyroscope camera", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [], 1],
    ["No charging", [0, 4, 13], [10, 18, 34], 4],
    ["Lv 3 charge only", [0, 4, 13], [10, 17, 33, 34], 2],
    ["No counters", [1, 6], [10, 34], 3],
    #20
    ["No spirit charges", [1], [10, 34], 3],
    ["No blocking", [0, 2, 6, 7, 9], [10], 4],
    ["Blade dance only", [3], [10, 34], 3],
    ["No self improvement song", [5], [10, 34], 4],
    ["Shelling, Wyrmstake and Wyvernfire only (Lance-less Gunlance)", [7], [10, 25, 34], 2],
    #25
    ["Poking only (Gun-less Gunlance)", [7], [10, 24, 34], 2],
    ["Axe mode only", [8, 9], [10, 27, 34], 4],
    ["Sword mode only", [8, 9], [10, 26, 34], 3],
    ["No shield charging", [9], [10, 34], 2],
    ["Kinsect only", [10], [10, 30, 32, 34], 4],
    #30
    ["No kinsect", [10], [10, 29, 34], 3],
    ["No aerial attacks", [10], [10, 32, 34], 2],
    ["Aerial attacks only", [10], [10, 29, 31, 34], 2],
    ["Melee only", [11, 12, 13], [9, 10, 18, 34], 5],
    ["Items Only", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [3, 4, 8, 9, 10, 12, 13, 17, 18, 19, 20, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33], 5],
    #35
    ["No dango", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [], 1]
]


frameForCanvas = tk.LabelFrame(root)
frameForCanvas.pack(fill = tk.BOTH, expand = "yes")
mainCanvas = tk.Canvas(frameForCanvas)
mainCanvas.pack(side = tk.LEFT, fill = tk.BOTH, expand = "yes")
scrollbar = ttk.Scrollbar(frameForCanvas, orient = "vertical", command = mainCanvas.yview)
scrollbar.pack(side = tk.RIGHT, fill = tk.Y)

mainCanvas.configure(yscrollcommand = scrollbar.set)

mainCanvas.bind("<Configure>", lambda e: mainCanvas.configure(scrollregion = mainCanvas.bbox("all")))

mainFrame = tk.Frame(mainCanvas, borderwidth = 5, relief = tk.GROOVE)

#Setup monster selection checkboxes
monsterColor = "#3B446B"
monsterFrame = tk.Frame(mainFrame, borderwidth = 5, relief = tk.GROOVE, bg = monsterColor)
monsterCheckboxes = []
monsterSubFramesContainer = tk.Frame(monsterFrame, bg = monsterColor)
monsterSubFrames = [tk.Frame(monsterSubFramesContainer, bg = monsterColor)]
j = 0
xcor = 0
ycor = 0
subFrameCounter = -1

monsterLabel = tk.Label(monsterFrame, text = "Monster List", font=("arial", 20), bg = monsterColor, fg = "#FFFFFF")
for i in monsterList:
    #Max 20 monsters per column
    if(j % 11 == 0):
        subFrameCounter = subFrameCounter + 1
        monsterSubFrames.append(tk.Frame(monsterSubFramesContainer, bg = monsterColor))
        xcor = xcor + 1

    var = tk.IntVar()
    monsterCheckboxes.append([tk.Checkbutton(monsterSubFrames[subFrameCounter], text = i[0], width = 18, height = 1, borderwidth = 5, relief = tk.RAISED, variable = var), var])
    monsterCheckboxes[j][0].select()
    monsterCheckboxes[j][0].grid(row = ycor, column = xcor, sticky = "n", padx = 5, pady = 3)
    j = j + 1
    ycor = ycor + 1

j = 0
monsterLabel.grid(row = 0, column = 0)
monsterSubFramesContainer.grid(row = 1, column = 0)
for i in monsterSubFrames:
    i.grid(row = 0, column = j, sticky = "n")
    j = j + 1

#Setup enable all/disable all buttons
monsterButtonsFrame = tk.Frame(monsterFrame, bg = monsterColor)
monstersEnableButton = tk.Button(monsterButtonsFrame, text = "Enable All", command = lambda: changeAll(monsterCheckboxes, "enable"))
monstersDisableButton = tk.Button(monsterButtonsFrame, text = "Disable All", command = lambda: changeAll(monsterCheckboxes, "disable"))
monstersEnableButton.grid(row = 0, column = 0, padx = 5)
monstersDisableButton.grid(row = 0, column = 1, padx = 5)
monsterButtonsFrame.grid(row = 2, column = 0)


#Setup weapon selection checkboxes
weaponColor = "#434F82"
weaponFrame = tk.Frame(mainFrame, borderwidth = 5, relief = tk.GROOVE, bg = weaponColor)
weaponCheckboxes = []
weaponSubFramesContainer = tk.Frame(weaponFrame, bg = weaponColor)
weaponSubFrames = [tk.Frame(weaponSubFramesContainer, bg = weaponColor)]
j = 0
xcor = 0
ycor = 0
subFrameCounter = -1

weaponLabel = tk.Label(weaponFrame, text = "Weapon List", font=("arial", 20), bg = weaponColor, fg = "#FFFFFF")
for i in weaponList:
    #Max 11 weapons per column, so the gunner ones have their own column, this just looks neat that way
    if(j % 4 == 0):
        subFrameCounter = subFrameCounter + 1
        weaponSubFrames.append(tk.Frame(weaponSubFramesContainer, bg = weaponColor))
        xcor = xcor + 1

    var = tk.IntVar()
    weaponCheckboxes.append(
        [
            tk.Checkbutton(
                weaponSubFrames[subFrameCounter], 
                text = i[0], 
                borderwidth = 5, 
                relief = tk.RAISED, 
                variable = var, 
                image =  i[1], 
                compound = "left"), 
            var
        ])
    weaponCheckboxes[j][0].select()
    weaponCheckboxes[j][0].grid(row = ycor, column = xcor, sticky = "ew", padx = 5, pady = 3)
    j = j + 1
    ycor = ycor + 1

j = 0
weaponLabel.grid(row = 0, column = 0)
weaponSubFramesContainer.grid(row = 1, column = 0, sticky = "ns")
for i in weaponSubFrames:
    i.grid(row = 0, column = j, sticky = "n")
    j = j + 1

#Setup enable all/disable all buttons
weaponButtonsFrame = tk.Frame(weaponFrame, bg = weaponColor)
weaponsEnableButton = tk.Button(weaponButtonsFrame, text = "Enable All", command = lambda: changeAll(weaponCheckboxes, "enable"))
weaponsDisableButton = tk.Button(weaponButtonsFrame, text = "Disable All", command = lambda: changeAll(weaponCheckboxes, "disable"))
weaponsEnableButton.grid(row = 0, column = 0, padx = 5)
weaponsDisableButton.grid(row = 0, column = 1, padx = 5)
weaponButtonsFrame.grid(row = 2, column = 0)

#Setup challenge selection checkboxes
challengeColor = "#475699"
challengeFrame = tk.Frame(mainFrame, borderwidth = 5, relief = tk.GROOVE, bg = challengeColor)
challengeCheckboxes = []
challengeTierFramesContainer = tk.Frame(challengeFrame, bg = challengeColor)
challengeTierFrames = [
    tk.Frame(challengeTierFramesContainer, bg = challengeColor, borderwidth = 5, relief = tk.GROOVE), 
    tk.Frame(challengeTierFramesContainer, bg = challengeColor, borderwidth = 5, relief = tk.GROOVE), 
    tk.Frame(challengeTierFramesContainer, bg = challengeColor, borderwidth = 5, relief = tk.GROOVE), 
    tk.Frame(challengeTierFramesContainer, bg = challengeColor, borderwidth = 5, relief = tk.GROOVE), 
    tk.Frame(challengeTierFramesContainer, bg = challengeColor, borderwidth = 5, relief = tk.GROOVE)
]

tier1png = PIL.ImageTk.PhotoImage(PIL.Image.open("images/tier1.png"))
tier2png = PIL.ImageTk.PhotoImage(PIL.Image.open("images/tier2.png"))
tier3png = PIL.ImageTk.PhotoImage(PIL.Image.open("images/tier3.png"))
tier4png = PIL.ImageTk.PhotoImage(PIL.Image.open("images/tier4.png"))
tier5png = PIL.ImageTk.PhotoImage(PIL.Image.open("images/tier5.png"))

tierLabels = [
    #tk.Label(challengeTierFrames[0], text = "Tier 1", font=("arial", 20), bg = challengeColor),
    #tk.Label(challengeTierFrames[1], text = "Tier 2", font=("arial", 20), bg = challengeColor),
    #tk.Label(challengeTierFrames[2], text = "Tier 3", font=("arial", 20), bg = challengeColor),
    #tk.Label(challengeTierFrames[3], text = "Tier 4", font=("arial", 20), bg = challengeColor),
    #tk.Label(challengeTierFrames[4], text = "Tier 5", font=("arial", 20), bg = challengeColor)
                                             
    tk.Label(challengeTierFrames[0], image = tier1png, bg = challengeColor), 
    tk.Label(challengeTierFrames[1], image = tier2png, bg = challengeColor), 
    tk.Label(challengeTierFrames[2], image = tier3png, bg = challengeColor), 
    tk.Label(challengeTierFrames[3], image = tier4png, bg = challengeColor), 
    tk.Label(challengeTierFrames[4], image = tier5png, bg = challengeColor)
]

tierSubFramesContainer = [
    tk.Frame(challengeTierFrames[0], bg = challengeColor),
    tk.Frame(challengeTierFrames[1], bg = challengeColor),
    tk.Frame(challengeTierFrames[2], bg = challengeColor),
    tk.Frame(challengeTierFrames[3], bg = challengeColor),
    tk.Frame(challengeTierFrames[4], bg = challengeColor)
]

tierSubFrames = [
    [], 
    [], 
    [], 
    [], 
    []
]

numPlacedChallenges = [[0, -1], [0, -1], [0, -1], [0, -1], [0, -1]]

#challengeSubFrames = [tk.Frame(challengeTierFramesContainer, bg = challengeColor)]
j = 0
xcor = 0
ycor = 0
subFrameCounter = -1

challengeLabel = tk.Label(challengeFrame, text = "Challenge List", font=("arial", 20), bg = challengeColor, fg = "#FFFFFF")
for i in challengeList:
    #print(i)
    #print(numPlacedChallenges)
    #Make new row
    if(numPlacedChallenges[i[3] - 1][0] == 0):
        numPlacedChallenges[i[3] - 1][1] = numPlacedChallenges[i[3] - 1][1] + 1
        tierSubFrames[i[3] - 1].append(tk.Frame(tierSubFramesContainer[i[3] - 1], bg = challengeColor))
        #print(tierSubFrames)
        #challengeSubFrames.append(tk.Frame(challengeTierFramesContainer, bg = challengeColor))
        #xcor = xcor + 1

    var = tk.IntVar()
    #print(i[3] - 1, math.floor(len(tierSubFrames[i[3] - 1]) / 5))
    challengeCheckboxes.append([tk.Checkbutton(tierSubFrames[i[3] - 1][math.floor(len(tierSubFrames[i[3] - 1]) / 5)], text = i[0], borderwidth = 5, relief = tk.RAISED, variable = var, wraplength = 90), var, numPlacedChallenges[i[3] - 1][0], numPlacedChallenges[i[3] - 1][1]])
    numPlacedChallenges[i[3] - 1][0] = numPlacedChallenges[i[3] - 1][0] + 1

    #Max challenges per row = 5
    if(numPlacedChallenges[i[3] - 1][0] == 7):
        numPlacedChallenges[i[3] - 1][0] = 0

    #print(numPlacedChallenges)
    #print(tierSubFrames[i[3] - 1][math.floor(len(tierSubFrames[i[3] - 1]) / 5)].winfo_children())
    #a = input()


challengeLabel.grid(row = 0, column = 0)
challengeTierFramesContainer.grid(row = 1, column = 0)

#print(challengeFrame.winfo_children())

k = 0
for i in challengeTierFrames:
    i.grid(row = k, column = 0, sticky = "we")
    k = k + 1

for i in tierLabels:
    #i.grid(row = 0, column = 0)
    i.pack()

for i in tierSubFramesContainer:
    #i.grid(row = 1, column = 0)
    i.pack()

#print(tierSubFrames)
for i in tierSubFrames:
    k = 0
    for j in i:
        #print(k)
        j.grid(row = 0, column = k)
        k = k + 1

for i in challengeCheckboxes:
    i[0].grid(row = i[3], column = i[2], sticky = "news", padx = 5, pady = 3)
    i[0].select()
    #challengeCheckboxes[j][0].grid(row = numPlacedChallenges[i[3] - 1][0], column = numPlacedChallenges[i[3] - 1][1], sticky = "new", padx = 5, pady = 3)

#Setup enable all/disable all buttons
challengeButtonsFrame = tk.Frame(challengeFrame, bg = challengeColor)
challengesEnableButton = tk.Button(challengeButtonsFrame, text = "Enable All", command = lambda: changeAll(challengeCheckboxes, "enable"))
challengesDisableButton = tk.Button(challengeButtonsFrame, text = "Disable All", command = lambda: changeAll(challengeCheckboxes, "disable"))
challengesEnableButton.grid(row = 0, column = 0, padx = 5)
challengesDisableButton.grid(row = 0, column = 1, padx = 5)
challengeButtonsFrame.grid(row = 2, column = 0)


#Setup settings selection frame
settingsColor = "#4D62C1"
settingsFrame = tk.Frame(mainFrame, borderwidth = 5, relief = tk.GROOVE, bg = settingsColor)
challengeNumberSlider = tk.Scale(settingsFrame, from_ = 1, to = 15, orient = tk.HORIZONTAL, label = "Number of restrictions (We recommend no more than 3)", length = 320)
challengeNumberSlider.grid(row = 0, column = 0, padx = 5)
challengeButton = tk.Button(settingsFrame, text = "Challenge!", command = generateChallenge)
challengeButton.grid(row = 0, column = 1, padx = 5)

mainCanvas.create_window((0, 0), window = mainFrame, anchor = "nw")
#mainFrame.pack(fill = tk.BOTH)
monsterFrame.grid(row = 0, column = 0, sticky = "ns")
weaponFrame.grid(row = 1, column = 0, sticky = "news")
challengeFrame.grid(row = 0, column = 1, rowspan = 2, sticky = "news")
settingsFrame.grid(row = 2, column = 0, columnspan = 2, sticky = "ew")
#challengeFrame.grid(row = 0, column = 1, sticky = "news")
#settingsFrame.grid(row = 1, column = 1, sticky = "ew")

root.mainloop()
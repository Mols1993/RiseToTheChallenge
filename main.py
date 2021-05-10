import tkinter as tk
import math
import random
import PIL.Image
import PIL.ImageTk

root = tk.Tk()
root.geometry("+50+50")
root.title("Rise to the Challenge")

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
    ["Greatsword", 0, PIL.ImageTk.PhotoImage(PIL.Image.open("images/GS.png"))],
    ["Long sword", 1, PIL.ImageTk.PhotoImage(PIL.Image.open("images/LS.png"))],
    ["Sword and shield", 2, PIL.ImageTk.PhotoImage(PIL.Image.open("images/SnS.png"))],
    ["Dual blades", 3, PIL.ImageTk.PhotoImage(PIL.Image.open("images/DB.png"))],
    ["Hammer", 4, PIL.ImageTk.PhotoImage(PIL.Image.open("images/Hmr.png"))],
    ["Hunting horn", 5, PIL.ImageTk.PhotoImage(PIL.Image.open("images/HH.png"))],
    ["Lance", 6, PIL.ImageTk.PhotoImage(PIL.Image.open("images/Lnc.png"))],
    ["Gunlance", 7, PIL.ImageTk.PhotoImage(PIL.Image.open("images/GL.png"))],
    ["Switch axe", 8, PIL.ImageTk.PhotoImage(PIL.Image.open("images/SA.png"))],
    ["Charge blade", 9, PIL.ImageTk.PhotoImage(PIL.Image.open("images/CB.png"))],
    ["Insect glaive", 10, PIL.ImageTk.PhotoImage(PIL.Image.open("images/IG.png"))],
    ["Light bowgun", 11, PIL.ImageTk.PhotoImage(PIL.Image.open("images/LBG.png"))],
    ["Heavy bowgun", 12, PIL.ImageTk.PhotoImage(PIL.Image.open("images/HBG.png"))],
    ["Bow", 13, PIL.ImageTk.PhotoImage(PIL.Image.open("images/Bow.png"))]
]

#[Challenge name, challenge ID N°, ID's to filter compatible weapons, non-compatible challenges by ID]
challengeList = [
    ["No wirefall", 0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [14]],
    ["Switch skills randomizer", 1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], []],
    ["No healing", 2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], []],
    ["Start with no items (Live off the land)", 3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [4, 34]],
    ["No items", 4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [3, 15, 34]],
    ["Hardcore (No carting)", 5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], []],
    ["Low rank gear", 6, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], []],
    ["No dodging", 7, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], []],
    ["No sharpening", 8, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 34]],
    ["Only Normal 1/No Coating", 9, [11, 12, 13], [10, 33, 34]],
    ["Only attack from palamute", 10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [12, 18, 22, 24, 25, 26, 27, 29, 32, 33]],
    ["Inverted controls (or normal, the ones you don't use)", 11, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], []],
    ["Silkbind attacks only", 12, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [10, 13, 14]],
    ["No silkbind attacks", 13, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [10, 12, 14, 34]],
    ["No wirebug (Play like it's MH1)", 14, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [0, 12, 13]],
    ["No moving while using items (Old school flex)", 15, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [4, 10]],
    ["Gyroscope camera", 16, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], []],

    ["No charging", 17, [0, 4, 13], [10, 18, 34]],
    ["Lv 3 charge only", 18, [0], [10, 17, 34]],
    ["No counters", 19, [1, 6], [10, 34]],
    ["No spirit charges", 20, [1], [10, 34]],
    ["No blocking", 21, [0, 2, 6, 7, 9], [10]],
    ["Demon flurry only", 22, [3], [10, 34]],
    ["No self improvement song", 23, [5], [10, 34]],
    ["Shelling and Wyvernfire only (Lance-less Gunlance)", 24, [7], [10, 25, 34]],
    ["Poking only (Gun-less Gunlance)", 25, [7], [10, 24, 34]],
    ["Axe mode only", 26, [8], [10, 27, 34]],
    ["Sword mode only", 27, [8, 9], [10, 26, 34]],
    ["No shield charging", 28, [9], [10, 34]],
    ["Kinsect only", 29, [10], [10, 30, 32, 34]],
    ["No kinsect", 30, [10], [10, 29, 34]],
    ["No aerial attacks", 31, [10], [10, 32, 34]],
    ["Aerial attacks only", 32, [10], [10, 29, 31, 34]],
    ["Melee only", 33, [11, 12, 13], [9, 10, 34]],
    ["Items Only", 34, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [3, 4, 8, 9, 10, 12, 13, 17, 18, 19, 20, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]]
]

mainFrame = tk.Frame(root, borderwidth = 5, relief = tk.GROOVE)

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

monsterLabel = tk.Label(monsterFrame, text = "Monster List", font=("arial", 35), bg = monsterColor)
for i in monsterList:
    #Max 20 monsters per column
    if(j % 20 == 0):
        subFrameCounter = subFrameCounter + 1
        monsterSubFrames.append(tk.Frame(monsterSubFramesContainer, bg = monsterColor))
        xcor = xcor + 1

    var = tk.IntVar()
    monsterCheckboxes.append([tk.Checkbutton(monsterSubFrames[subFrameCounter], text = i[0], width = 25, height = 1, borderwidth = 5, relief = tk.RAISED, variable = var), var])
    monsterCheckboxes[j][0].select()
    monsterCheckboxes[j][0].grid(row = ycor, column = xcor, sticky = "n", padx = 5, pady = 3)
    #print(monsterCheckboxes[j])
    j = j + 1
    ycor = ycor + 1

j = 0
monsterLabel.grid(row = 0, column = 0)
monsterSubFramesContainer.grid(row = 1, column = 0)
for i in monsterSubFrames:
    i.grid(row = 0, column = j, sticky = "n")
    j = j + 1


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

weaponLabel = tk.Label(weaponFrame, text = "Weapon List", font=("arial", 35), bg = weaponColor)
for i in weaponList:
    #Max 11 weapons per column, so the gunner ones have their own column, this just looks neat that way
    if(j % 11 == 0):
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
                image =  i[2], 
                compound = "left"), 
            var])
    weaponCheckboxes[j][0].select()
    weaponCheckboxes[j][0].grid(row = ycor, column = xcor, sticky = "ew", padx = 5, pady = 3)
    j = j + 1
    ycor = ycor + 1

j = 0
weaponLabel.grid(row = 0, column = 0)
weaponSubFramesContainer.grid(row = 1, column = 0)
for i in weaponSubFrames:
    i.grid(row = 0, column = j, sticky = "n")
    j = j + 1

#Setup challenge selection checkboxes
challengeColor = "#475699"
challengeFrame = tk.Frame(mainFrame, borderwidth = 5, relief = tk.GROOVE, bg = challengeColor)
challengeCheckboxes = []
challengeSubFramesContainer = tk.Frame(challengeFrame, bg = challengeColor)
challengeSubFrames = [tk.Frame(challengeSubFramesContainer, bg = challengeColor)]
j = 0
xcor = 0
ycor = 0
subFrameCounter = -1

challengeLabel = tk.Label(challengeFrame, text = "Challenge List", font=("arial", 35), bg = challengeColor)
for i in challengeList:
    #Max 20 challenges per column
    if(j % 20 == 0):
        subFrameCounter = subFrameCounter + 1
        challengeSubFrames.append(tk.Frame(challengeSubFramesContainer, bg = challengeColor))
        xcor = xcor + 1

    var = tk.IntVar()
    challengeCheckboxes.append([tk.Checkbutton(challengeSubFrames[subFrameCounter], text = i[0], borderwidth = 5, relief = tk.RAISED, variable = var), var])
    challengeCheckboxes[j][0].select()
    challengeCheckboxes[j][0].grid(row = ycor, column = xcor, sticky = "new", padx = 5, pady = 3)
    j = j + 1
    ycor = ycor + 1

j = 0
challengeLabel.grid(row = 0, column = 0)
challengeSubFramesContainer.grid(row = 1, column = 0)
for i in challengeSubFrames:
    i.grid(row = 0, column = j, sticky = "n")
    j = j + 1

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
            weaponImg = i[2]

    #Get weapon ID, to filter compatible challenges
    weaponID = 0
    for i in weaponList:
        if(weapon == i[0]):
            weaponID = i[1]

    #[Challenge name, challenge ID N°, ID's to filter compatible weapons, non-compatible challenges by ID]
    compatibleChallenges = []
    for i in challengeList:
        if(weaponID in i[2]):
            compatibleChallenges.append(i)

    challenges = []
    random.shuffle(compatibleChallenges)
    for i in range(min(challengeNumberSlider.get(), len(compatibleChallenges))):
        if(compatibleChallenges[0][0] == "Switch skills randomizer"):
            compatibleChallenges[0][0] = "Switch skills randomizer: " + str(random.randint(1,2)) + " - " + str(random.randint(1,2)) + " - " + str(random.randint(1,2))
        challenges.append(compatibleChallenges[0][0])

        for j in compatibleChallenges[0][3]:
            for k in compatibleChallenges:
                if(k[1] == j):
                    compatibleChallenges.remove(k)
        
        compatibleChallenges.pop(0)
        if(len(compatibleChallenges) == 0):
            break

    newWindow(monster, monsterImg, weapon, weaponImg, challenges)


#Setup settings selection frame
settingsColor = "#4D62C1"
settingsFrame = tk.Frame(mainFrame, borderwidth = 5, relief = tk.GROOVE, bg = settingsColor)
challengeNumberSlider = tk.Scale(settingsFrame, from_ = 1, to = len(challengeCheckboxes), orient = tk.HORIZONTAL, label = "Number of restrictions", length = 300)
challengeNumberSlider.grid(row = 0, column = 0, padx = 5)
testButton = tk.Button(settingsFrame, text = "Challenge!", command = generateChallenge)
testButton.grid(row = 0, column = 1, padx = 5)

mainFrame.pack(fill = tk.BOTH)
monsterFrame.grid(row = 0, column = 0, sticky = "ns")
weaponFrame.grid(row = 0, column = 1, sticky = "ns")
challengeFrame.grid(row = 0, column = 2, sticky = "ns")
settingsFrame.grid(row = 1, column = 0, columnspan = 3, sticky = "ew")


def newWindow(monster, monsterImg, weapon, weaponImg, challenges):
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

    #root.update()
    # now root.geometry() returns valid size/placement
    #root.minsize(root.winfo_width(), root.winfo_height())

root.mainloop()
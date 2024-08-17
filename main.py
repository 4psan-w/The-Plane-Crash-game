import random as r
import time 
import keyboard as kb

class plane_crash:
    chances = 3
    score = 0
    completion_score = 333

    def  intro(self):
        print("++++++++++++++++++++++++++++++")
        print("<<<<<<<PLANE CRASH GAME>>>>>>>")
        print("++++++++++++++++++++++++++++++")
        print()
        print()
        print("____________________________________________________________________")
        print()
        print(f"Eject Before the plane crashes Collect the scores upto {self.completion_score} in {self.chances } chances ")
        print("BEST OF LUCK")

    def game(self):
        i=0
        print()
        print()
        print("=======================================")
        print("||SINGLE PLAYER PLANE CRASH GAME MODE||")
        print("=======================================")
        print()
        print()
        print("Game Started")
        print("You have", self.chances, "chances")
        while(self.chances > 0):
            print("Get Ready To Eject before The Plane Crashes")
            for i in range(1,4):
                print(i)
                time.sleep(1)
            print("GO!")

            print("The Game Has begun: ")
            start = r.randint(0,r.randint(0,r.randint(1,100)))
            end =  r.randint(1,r.randint(1,r.randint(10,10000)))
            if(end<start):
                 end = r.randint(start , start *2)
            random = r.randint(start,end)
            while (i <=random) :
                i= i+1
                val = i
                val = val/10
                print(val)
                time.sleep(0.01)
                if(kb.is_pressed("\n")):
                    print()
                    print()
                    print(f"       + {val} points")
                    self.score = val + self.score
                    break
                
            else:
                print()
                print()
                print(f"       -{val} points")
                print("++++++!! THE PLANE CRASHED !!++++++")
                print("you lost a chance")
                self.score = self.score - val
                self.chances = self.chances -1
            
            print()
            print()
            print(f"=====TOTAL SCORE <<[{self.score}]>>")
            print()
            print()
            if(self.score >= self.completion_score):
                print("CONGRATULATIONS YOU WON")
                break
            elif(self.chances == 0):
                print("===========================================")
                print("!!   YOU LOST THE GAME PLEASE TRY AGAIN  !!")
                print("===========================================")
                break

            print(f"=====YOU GOT <<{self.chances} CHANCES LEFT>>")
            

def game():
    mode = input("Press ENTER to Play The Game")
    if(mode == ""):
        player = plane_crash()
        player.intro()
        player.game()

__name__=="__main__"
game()
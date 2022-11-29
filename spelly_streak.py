import random
from words import word

class streak():
    chosen_word = random.choice(word) #從list中隨機抓一個字
    current_word = [] #持續更新已猜對的字母
    already_guessed = [] #列出玩家猜過的字母
    letter_counts = len(chosen_word) #將字母長度存在此變數
    alphabets = "abcdefghijklmnopqrstuvwxyz" #所有字母
    lives = 0

    def live():
        global lives #使此變數可以在其他函數使用

        while(1):
            difficulty = input("請選擇難易度 1 ~ 5\n1為最簡單，5為最難。\n\n請輸入難易度: ")
            
            try: 
                difficulty = int(difficulty)
                
                if difficulty == 1:
                    streak.lives = 10
                    break
                elif difficulty == 2:
                    streak.lives = 8
                    break
                elif difficulty == 3:
                    streak.lives = 6
                    break
                elif difficulty == 4:
                    streak.lives = 4
                    break
                elif difficulty == 5:
                    streak.lives = 2
                    break
                else:
                    print()
                    print("***請輸入1 ~ 5 喔！***\n")
                

            except:
                print() 
                print("***請輸入1 ~ 5 喔！***\n")

    def check(): #回報玩家目前猜字狀態


        print(f"你還有{streak.lives}個機會")

        visual = ""

        for i in streak.current_word: #將list中的項目輸入string
            visual += i

        print(f"目前猜字狀況：{visual}")

        visual1 = ""

        for i in sorted(streak.already_guessed): #順便將already_guessed排序
            visual1 += f"{i} "

        print(f"你已經猜過的字母：{visual1}")



    def question():
        streak.live()
        print(f"你還有{streak.lives}個機會")

        print(f"這個字有{streak.letter_counts}個字母。") #跟玩家說字中有多少字母

        for i in range(streak.letter_counts): #將字母視覺化
            streak.current_word.append("-")


    def game_process():
        guess = input("猜一個字母吧: ").lower() #用lower確保輸入大寫字母也沒問題

        while (len(guess) != 1) or (guess not in streak.alphabets): #禁止非字母及多字母的輸入
            print("***要輸入英文字母喔***")
            guess = input("請輸入一個字母： ").lower()
        
        if guess not in streak.already_guessed:
            streak.already_guessed.append(guess) #輸入猜過的字母


        if guess not in streak.chosen_word: #如果猜錯
            print("錯了！在猜一次吧！")
            streak.lives -= 1 #少一點血
        else: #猜對
            print("太棒了你答對了！")

            count = 0 #紀錄迴圈執行次數
            for i in streak.chosen_word:#確認猜對的字在哪
                if i == guess: #如果找到
                    streak.current_word[count] = i #更新此字母到current_word
            
                count += 1
                
        streak.check()






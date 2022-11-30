#從其餘檔案輸入
from spelly_streak import streak
from spelly_match import match

#玩家總分
point = 0
chosegame =0

print("你好，歡迎參加Spelly拼字遊戲！")

#確定分數由0開始
name = input("開始之前，我們需要基本資料。<輸入完成請按[ENTER]鍵> 請輸入你的姓名： ") 
stripname = name.strip()
#確保使用者輸入的名字沒有空格

while 1:
    try:
        namecheck = int(input("\n為確保資料無誤，與你核對名字。你叫 [" + stripname + "] 對嗎？ <輸入完成請按[ENTER]鍵> 是請輸入數字1，否請輸入數字2： \n"))
        if namecheck == 1:
            print("歡迎你! " + stripname)
            break
        elif namecheck == 2: 
            name = input("\n好吧！我們再試一次！<輸入完成請按[ENTER]鍵> 請在此輸入你的姓名： ")
            stripname = name.strip()
    except:
        print("抱歉，請輸入1或2喔!")
        name = input("\n我們再試一次！<輸入完成請按[ENTER]鍵> 請在此輸入你的姓名： ")
        stripname = name.strip()
        
        

while chosegame!=1 and chosegame !=2:
  try:
    chosegame = int(input("你要遊玩哪個遊戲？請輸入1遊玩spelly match，輸入2遊玩spelly streak: "))
    if chosegame !=1 and chosegame !=2:
      print("***請輸入1或2來參加遊戲喔！***")
  except:
    print("***請輸入1或2來參加遊戲喔！***")
    

if chosegame == 1:
  #Spelly match
  print("你好！歡迎參加SPELLY Match拼字大賽\n")
  print("在此提醒，若執行過程中，出現erroe等字詞，代表使用者輸入錯誤，必須重新啟動程式！如需支援，請舉手！\n")
  
  match.game_process()
  point += match.p
  
  print(f"遊戲結果:Spelly-match獲得{point}分")
elif chosegame == 2:
    #Spelly streak
    print("你好！歡迎參加SPELLY streak拼字大賽\n")
    print("Spelly streak遊戲說明:\n")
    print("玩家要一次猜一個英文字母，並嘗試猜出完整的英文單字。(範例:apple)\n要猜的字以一列橫線表示(-----)，代表目前猜字狀況。\n如果猜字的玩家猜中其中一個字母，另一位便須於該字母出現的所有位置上寫上該字母。(-pp--)\n直到猜出單字或機會用光為止。\n")
    
    input("\n瞭解規則後，按下[ENTER]鍵開始吧\n:")
    
    streak.question()
    
    
    
    while(1): # 1 == true
        if "-" not in streak.current_word: #如果已經猜完
            print("恭喜你猜中了！")
            break
        elif streak.lives == 0:
            print(f"你輸了，正確答案為{streak.chosen_word}，下次再加油。")
            break
    
        streak.game_process()
    print(f"遊戲結果:Spelly-streak剩餘{streak.lives}次機會")

#end
print()
print("感謝遊玩，希望你的英文能有所進步喔！")
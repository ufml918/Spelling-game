from spelly_streak import streak
from spelly_match import match

#玩家總分
point = 0

#Spelly match
print("你好！歡迎參加SPELLY Match拼字大賽\n")
print("在此提醒，若執行過程中，出現erroe等字詞，代表使用者輸入錯誤，必須重新啟動程式！如需支援，請舉手！\n")

match.game_process()
point += match.p

print(point)

#Spelly streak
print("Spelly streak遊戲說明:\n")
print("玩家要一次猜一個英文字母，並嘗試猜出完整的英文單字。(範例:apple)\n要猜的字以一列橫線表示(-----)，代表目前猜字狀況。\n如果猜字的玩家猜中其中一個字母，另一位便須於該字母出現的所有位置上寫上該字母。(-pp--)\n直到猜出單字或機會用光為止。\n")

streak.question()



while(1): # 1 == true
    if "-" not in streak.current_word: #如果已經猜完
        print("恭喜你猜中了！")
        break
    elif streak.lives == 0:
        print(f"你輸了，正確答案為{streak.chosen_word}，下次再加油。")
        break

    streak.game_process()

class match():
    p = 0
    def game_process():

            print("\n以下是基本規則:")
            print("\n規則1:題目中文為，選手須回答英文，單字拼字需正確才給分")
            print("\n規則2:答案不分大小寫，只要拼字正確便得1分")
            input("\n瞭解規則後，按下[ENTER]鍵開始吧\n:")
            #確保使用者清楚閱讀規則後，才開始出題
            print("\n題目正式開始！加油！\n")
            qs = ["河流","大海","海灘","湖泊","山","銀行","書店","辦公室","公園","餐廳"]
            ans = ["river", "sea", "beach", "lake","mountain","bank","bookstore","office","park","restaurant"]
            for i in range(10):
                q = input("\n第" + str(i+1) + "題. 請輸入『" + qs[i] + "』的英文: <輸入完畢請按[ENTER]鍵>：")
                #以for迴圈加list使程式精簡
                #str(i+1)讓題號從1開始
                qsl = q.strip().lower()
                #確保使用者即使用大寫或誤按空格，只要拼字正確，都能算對
                if qsl == ans[i]:
                    match.p +=  1
                    #回答正確加1分
                    print("恭喜答對！  目前分數："  + str(match.p))
                    #依照p值顯示分數
                else:
                    print("回答錯誤！  正確答案應該是『 " + ans[i] + " 』  目前分數：" + str(match.p) + "  加油！")
                #以ans[i]給予正確解答
                #依照p值顯示分數
            print("\n比賽結束!")
            print("\n太棒了！你總共答對" + str(match.p) + "題")
            if (match.p >= 10):
                print(f"\n恭喜你獲得金牌獎{match.p}分")
            elif match.p >= 8:
                print(f"\n恭喜你獲得銀牌獎{match.p}分")
            elif match.p >= 6:
                print(f"\n恭喜你獲得銅銅牌獎{match.p}分")
            else:
                print(f"\n你得到了{match.p}分，下次再加油，不要氣餒喔！")
            #依答對題數給予獎項
            return match.p

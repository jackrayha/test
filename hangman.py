import random


def hangman_game():
    # 1. 准备一些单词供随机选择
    word_list = ["python", "javascript", "hangman", "programming",
                 "complex", "development", "function", "variable",
                 "algorithm", "virtual"]

    # 2. 随机选取一个单词
    secret_word = random.choice(word_list)

    # 3. 初始化
    guessed_letters = set()  # 存储玩家已经猜过的字母
    correct_letters = set()  # 存储玩家猜对的字母
    remaining_guesses = 6    # 玩家最多能错误猜测的次数

    # 提示信息
    print("欢迎来到 Hangman 猜词游戏！")
    print("系统随机选择了一个单词，请猜猜它是什么？")
    print("你有 6 次机会可以猜错，之后游戏就会结束。\n")

    # 4. 主游戏循环
    while True:
        # 4.1 显示当前已猜对的字母和未猜到的部分
        # 如果某个字母已猜对，则显示字母，否则显示下划线 _
        display_word = ""
        for char in secret_word:
            if char in correct_letters:
                display_word += char + " "
            else:
                display_word += "_ "
        print("当前进度：", display_word.strip())

        # 4.2 判断是否已经全部猜出
        if all(char in correct_letters for char in secret_word):
            print(f"恭喜你，单词是 '{secret_word}'，你猜对了！")
            break

        # 4.3 显示当前的错误次数信息
        print(f"你还可以猜错 {remaining_guesses} 次。")

        # 4.4 让玩家输入猜测的字母
        guess = input("请输入一个字母进行猜测： ").lower().strip()

        # 4.5 验证输入是否为单个字母
        if len(guess) != 1 or not guess.isalpha():
            print("无效输入，请输入单个英文字母。\n")
            continue

        # 4.6 判断玩家是否已经猜过这个字母
        if guess in guessed_letters:
            print(f"你已经猜过字母 '{guess}' 了，请换一个。\n")
            continue
        else:
            guessed_letters.add(guess)

        # 4.7 根据猜测结果进行处理
        if guess in secret_word:
            print(f"好！字母 '{guess}' 存在于单词中。\n")
            correct_letters.add(guess)
        else:
            remaining_guesses -= 1
            print(f"很遗憾，字母 '{guess}' 不在单词中。\n")

        # 4.8 判断剩余猜测次数是否用完
        if remaining_guesses == 0:
            print(f"你已经没有猜测次数了，游戏结束！正确答案是 '{secret_word}'。")
            break


if __name__ == "__main__":
    hangman_game()

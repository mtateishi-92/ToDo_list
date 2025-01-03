todo_list = []
todo_disc = str(input('ToDoを入力してください。:'))
todo_list.append(todo_disc)

#さらに入力を追加するか判定
judge = str(input('他のToDoを入力しますか? yes or no :'))
#yesまたはnoを入力するまで繰り返す
while not judge == 'yes' and not judge == 'no':
    print('yesかnoを入力してください。')
    judge = str(input('他のToDoを入力しますか? yes or no :'))

#yesの場合は追加を繰り返す
while judge == 'yes' :
    if judge == 'yes':
        todo_disc = str(input('ToDoを入力してください。:'))
        todo_list.append(todo_disc)
        #さらに入力を追加するか判定
        judge = str(input('他のToDoを入力しますか? yes or no :'))
        #yesまたはnoを入力するまで繰り返す
        while not judge == 'yes' and not judge == 'no':
            print('yesかnoを入力してください。')
            judge = str(input('他のToDoを入力しますか? yes or no :'))
#noの場合、繰り返しを終了しリストの内容を表示する
if judge == 'no':
    print('ToDoを表示します。')

#ToDoを出力
for number, ToDo in enumerate(todo_list, 1):
    print(str(number) + ':' + ToDo)


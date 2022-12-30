# SA_ClientCenter

第一次pull請先
```sh
python manage.py makemigrations
python manage.py migrate
#這樣才會建立db檔，然後建立使用者去登入admin
```

1. 有git ignore，但有留migrations資料夾（資料庫模型紀錄檔）跑django不影響，直接runserver就好
2. 已建立多個app環境，在apps中建立新的app並註冊即可  
3. settings 裡面有 line帳號token*2 跟 內網轉發網址(ngork)，在裡面修改即可套用到全域設定.

[line-login官方說明](https://developers.line.biz/en/reference/line-login/#response-headers)

[使用轉發：ngrok](https://ngrok.com/)（記得去辦會員就不會過期了）

## ！！！還無法判定是否為初次登入！！！
目前推測是網址中的redirect進迴圈了，待解決
還有授權按不同意會跳500，待解決

還有登入方法還要再查一下，我裡面是亂寫的也不知道對不對

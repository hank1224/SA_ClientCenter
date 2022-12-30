# SA_ClientCenter
第一次pull請先
python manage.py makemigrations
python migrate
這樣才會建立db檔，然後建立使用者去登入admin

有git ignore，但有留migrations資料夾（資料庫模型紀錄檔）跑django不影響，直接runserver就好

已建立多個app環境，在apps中建立新的app並註冊即可
settings 裡面有 line帳號token*2 跟 內網轉發網址(ngork)，在裡面修改即可套用到全域設定

https://developers.line.biz/en/reference/line-login/#response-headers
https://ngrok.com/ （記得去辦會員就不會過期了）
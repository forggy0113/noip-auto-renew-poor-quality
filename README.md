# noip-auto-renew-poor-quality
# noip30天試用自動延長(DX旗艦版)

* 請先安裝和客戶端版本相同之Google Chrome Driver

https://tinyurl.com/y6zqvcfp

* 並且將Driver 放入PATH中




**使用時請進入文件修改登入帳號以及密碼**

**雙擊兩下即可以無痕視窗開啟瀏覽器自動延期**



可搭配Windows排程功能每天或每周自動執行



* 已知的問題:

  * 免費版一次最多可能有三個需要激活的按鈕，但執行一次程式時只會激活一個按鈕後就自動關閉，_很愛偷懶_。

  * 如果偵測不到可以激活的對象，瀏覽器不會自動關閉，_它很倔將_。

  * 開發者連for迴圈不會寫，因為他不會然後都也忘光了，_給他一杯啤酒好嗎_。



* 未來的想像:

  * 可在json檔裡輸入帳號和密碼，雙擊兩下即可執行，_好方便_。

  * 執行一次程式即可同時激活三個按鈕，_有效率_。

  * 就算沒有可以激活對象也會自動關閉程式，_好聰明_。

  * 希望可以不顯示任何畫面，在背地裡偷偷執行，_就像下水道的老鼠一般_。

  * ~希望可以買一戶陶朱隱園。~


* 來自he10910的話:

  * 新增json檔案，_真D方便_。

  * 其實還要安裝 psutil 還有 selenium 才能執行，~_作者沒講的BUG_~。
  
  * 可以透過 ```pip install psutil``` 來安裝。

  * 可以透過 ```pip install selenium``` 來安裝。

  * 可以自定義PATH了，_撒花_。

  * 其實我是用while迴圈不是for，_硬要_。

  * 他會自己跑三次 如果激活按鈕是同一個的話就解決了，_讚啦_。

  * 程式找不到可以按的就會自己關掉了，_再倔強也沒用_。

  * ~我不會背景執行 咩噗。~

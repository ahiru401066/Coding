# よく使う
- split
- join
- replace
- find
- f-string  
    文字列に変数を埋め込む  
    ex) f"Max: {maximum}, Min: {minimum}"
- 10進数と16進数  
    hex, int  
    10進数 -> 16進数
    ```
    num = 255
    print(hex(num))  # 出力: '0xff'
    ```
    16進数 -> 10進数
    ```
    hex_str = "0xff"
    num = int(hex_str, 16)
    print(num)  # 出力: 255
    ```
- 文字列逆順
    text(string) text[::-1]
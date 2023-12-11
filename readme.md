# 介绍

利用cryptography库中的Fernet来加密和解密信息

# 代码核心内容

```python
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet

# 生成密钥
def generate_key():
    return Fernet.generate_key()

# 加密文本
def encrypt_text(key, plaintext):
    cipher = Fernet(key)
    encrypted_text = cipher.encrypt(plaintext.encode())
    return encrypted_text

# 解密文本
def decrypt_text(key, ciphertext):
    cipher = Fernet(key)
    decrypted_text = cipher.decrypt(ciphertext).decode()
    return decrypted_text

# 主函数，演示加密和解密
def main():
    # 生成密钥
    key = generate_key()

    # 待加密的文本
    plaintext = "Hello, cryptography!"

    # 加密文本
    ciphertext = encrypt_text(key, plaintext)
    print(f"Encrypted Text: {ciphertext}")

    # 解密文本
    decrypted_text = decrypt_text(key, ciphertext)
    print(f"Decrypted Text: {decrypted_text}")

if __name__ == "__main__":
    main()
```

# 完整的代码

```python
# This Python file uses the following encoding: utf-8
import sys
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
from base64 import b64encode, b64decode
import os
import pyperclip
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup()

    def setup(self):
        # 按钮事件
        self.encrypt_btn.clicked.connect(self.encrypt_b)        # 加密
        self.decrypt_btn.clicked.connect(self.decrypt_b)        # 解密
        self.copy_key_btn.clicked.connect(self.copy_key)        # 复制密码
        self.clear_btn.clicked.connect(self.clear_all)          # 清空全部
        self.copy_result_btn.clicked.connect(self.copy_result)  # 复制结果

    def encrypt_b(self):
        key = Fernet.generate_key()                     # 得到密码
        plaintext = self.input_box.toPlainText()        # 获取内容
        cipher = Fernet(key)                            # 创建cipher对象 
        bytes_data = bytes(plaintext, encoding='utf-8') # 将内容转为bytes类型
        encrypted_text = cipher.encrypt(bytes_data)     # 加密

        key = key.decode('utf-8')                       # 将key转为str类型
        encrypted_text = encrypted_text.decode('utf-8') # 将结果转为str类型

        # 显示结果与密码
        self.key_box.setText(str(key))
        self.output_box.setText(str(encrypted_text))

    def decrypt_b(self):
        plaintext = self.input_box.toPlainText()        # 获取内容
        key = self.key_box.text()                       # 获取key
        key = bytes(key, encoding='utf-8')              # 将key转为bytes类型
        cipher = Fernet(key)                            # 创建cipher对象
        decrypted_text = cipher.decrypt(plaintext)      # 解密

        decrypted_text = decrypted_text.decode('utf-8') # 将结果转为str类型

        # 显示结果
        self.output_box.setText(decrypted_text)

    def copy_key(self):
        key = self.key_box.text()
        pyperclip.copy(key)

    def clear_all(self):
        self.input_box.clear()
        self.output_box.clear()
        self.key_box.clear()

    def copy_result(self):
        result = self.output_box.toPlainText()
        pyperclip.copy(result)

    def generate_key(self):
        # 生成一个随机的32字节密钥
        return b64encode(os.urandom(32))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
```

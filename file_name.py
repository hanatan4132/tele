from selenium import webdriver
import time
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException, MoveTargetOutOfBoundsException

profile_path = "C:/Users/ASUS/AppData/Roaming/Mozilla/Firefox/Profiles/eyqk3l9g.default"  # 修改为你的 Firefox 配置文件路径

def scroll_into_view(element):
    driver.execute_script("arguments[0].scrollIntoView(true);", element)

def highlight_element(element):
    driver.execute_script("arguments[0].style.border='3px solid red'", element)

def save_storage(driver, local_storage_file, session_storage_file):
    # 保存本地存储
    local_storage = driver.execute_script("return window.localStorage;")
    with open(local_storage_file, 'w') as file:
        json.dump(local_storage, file)
    
    # 保存会话存储
    session_storage = driver.execute_script("return window.sessionStorage;")
    with open(session_storage_file, 'w') as file:
        json.dump(session_storage, file)

def load_storage(driver, local_storage_file, session_storage_file):
    driver.get("https://web.telegram.org/k/")
    
    # 加载本地存储
    with open(local_storage_file, 'r') as file:
        local_storage = json.load(file)
        for key, value in local_storage.items():
            driver.execute_script(f"window.localStorage.setItem('{key}', '{value}');")
    
    # 加载会话存储
    with open(session_storage_file, 'r') as file:
        session_storage = json.load(file)
        for key, value in session_storage.items():
            driver.execute_script(f"window.sessionStorage.setItem('{key}', '{value}');")
    
    driver.refresh()

options = webdriver.FirefoxOptions()
options.set_preference("profile", profile_path)

# 初始化 WebDriver
driver = webdriver.Firefox(options=options)

# 打开目标网页
driver.get("https://example.com")  # 替换为目标网页的URL

# 尝试加载存储数据以保持登录状态
try:
    load_storage(driver, "local_storage.json", "session_storage.json")
except Exception as e:
    print(f"加载存储数据失败: {e}")

# 检查是否成功登录
time.sleep(5)  # 等待页面加载

if "Log in" not in driver.page_source:
    print("成功登录")
else:
    print("需要手动登录")
    input("请手动登录并按回车继续...")
    # 保存登录后的存储数据
    save_storage(driver, "local_storage.json", "session_storage.json")
input("回车继续...")
time.sleep(2)

try:
   
    
    
    # 找到 class 为 "search-super-month-items" 的 div
        # 找到所有 class 為 "search-super-month-items" 的父元素
    parent_elements = driver.find_elements(By.CLASS_NAME, "search-super-month-items")
    
    # 顯示總共有幾個可選
    print(f"共找到 {len(parent_elements)} 個 search-super-month-items 區塊")
    
    # 讓使用者輸入想要的索引（從 0 開始）
    target_index = int(input("請輸入你想要選擇的區塊編號（從 0 開始）："))
    
    # 檢查索引是否合法
    if target_index < 0 or target_index >= len(parent_elements):
        print("錯誤：輸入的索引超出範圍")
    else:
        # 取得選定的區塊
        parent = parent_elements[target_index]
    
        # 取得其下的所有第一層子元素
        child_elements = parent.find_elements(By.XPATH, "./div")
    
        # 建立檔案名稱清單
        file_names = []
    
        for element in child_elements:
            try:
                # 注意：class 名稱中間要用 . 連接（不是空格）
                name_element = element.find_element(By.CSS_SELECTOR, "div.document-name > middle-ellipsis-element")

                file_name = name_element.text
                if file_name:
                    file_names.append(file_name)
            except Exception as e:
                print(f"找不到檔案名稱元素：{e}")
    
        # 寫入 txt 檔案
        with open('file_names.txt', 'w', encoding='utf-8') as file:
            for name in file_names:
                file.write(f"{name}\n")
    
        print("已將選定區塊中的所有文件名記錄在 file_names.txt 中")



finally:
    # 关闭 webdriver
    driver.quit()

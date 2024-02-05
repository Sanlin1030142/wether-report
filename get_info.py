import requests
from xml.etree import ElementTree as ET

def generate_html_for_element(element, indent=0):
    html_content = ""
    if list(element):  # 如果元素有子元素，則遞歸處理
        html_content += "  " * indent + f"<tr><td colspan='2'><strong>{element.tag}</strong></td></tr>\n"
        for child in list(element):
            html_content += generate_html_for_element(child, indent + 1)
    else:  # 如果元素沒有子元素，直接顯示
        html_content += "  " * indent + f"<tr><td>{element.tag}</td><td>{element.text}</td></tr>\n"
    return html_content

# API URL
url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-D0047-005?Authorization=CWA-DDE75E74-3BE3-415B-A2DC-ADAA80D9B8BB&limit=1&format=XML&locationName=%E6%A5%8A%E6%A2%85%E5%8D%80&sort=time&startTime=2024-02-01T18%3A00%3A00&dataTime=2024-02-02T06%3A00%3A00"

# 發送請求
response = requests.get(url)

# 檢查請求是否成功
if response.status_code == 200:
    # 解析 XML 數據
    root = ET.fromstring(response.content)

    # 開始 HTML 文檔
    html_content = "<html>\n<head>\n<title>天氣報告</title>\n</head>\n<body>\n<h1>天氣報告</h1>\n<table border='1'>\n"

    # 遍歷 XML 結構並生成 HTML
    html_content += generate_html_for_element(root)

    # 結束 HTML 表格和文檔
    html_content += "</table>\n</body>\n</html>"

    # 將 HTML 內容存儲到檔案中
    with open('./docs/index.html', 'w', encoding='utf-8') as file:
        file.write(html_content)

    print("天氣報告 HTML 頁面已生成。")
else:
    print("請求失敗，狀態碼：",response.status_code)

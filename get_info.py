import requests
from xml.etree import ElementTree

# API URL
url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-D0047-005?Authorization=CWA-DDE75E74-3BE3-415B-A2DC-ADAA80D9B8BB&limit=1&format=XML&locationName=%E6%A5%8A%E6%A2%85%E5%8D%80&sort=time&startTime=2024-02-01T18%3A00%3A00&dataTime=2024-02-02T06%3A00%3A00"

# 發送請求
response = requests.get(url)

# 檢查請求是否成功
if response.status_code == 200:
    # 解析 XML 數據
    root = ElementTree.fromstring(response.content)
    
    # 尋找 <records> 元素
    records = root.find('.//records')
    if records is not None:
        # 開始 HTML 文檔
        html_content = "<html>\n<head>\n<title>天氣報告</title>\n</head>\n<body>\n<h1>天氣報告</h1>\n"
        
        # 遍歷 <records> 元素及其子元素的內容，添加到 HTML 中
        for element in records.iter():
            html_content += f"<p><strong>{element.tag}:</strong> {element.text}</p>\n"
        
        # 結束 HTML 文檔
        html_content += "</body>\n</html>"
        
        # 將 HTML 內容存儲到檔案中
        with open('./docs/index.html', 'w', encoding='utf-8') as file:
            file.write(html_content)
            
        print("天氣報告 HTML 頁面已生成。")
    else:
        print("<records> 元素未找到")
else:
    print("請求失敗，狀態碼：", response.status_code)

import os
import requests

# 從環境變數安全讀取 API Key，避免硬編碼洩漏
CWA_API_KEY = os.environ.get("CWA_API_KEY")


def get_nantou_weather():
    url = f"https://opendata.cwa.gov.tw/api/v1/rest/datastore/O-A0001-001?Authorization={CWA_API_KEY}&locationName=南投&format=JSON"
    print(f"準備請求氣象資料，使用的 API Key 長度為：{len(CWA_API_KEY) if CWA_API_KEY else 0}")
    # 此處可補充 requests 邏輯


if __name__ == "__main__":
    get_nantou_weather()

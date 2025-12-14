# AWS Bedrock Claude Scripts

這是一組使用 AWS Bedrock Claude 3.5 Sonnet 模型的 Python 腳本工具集，提供多種文字處理功能，包括翻譯、摘要、正式化改寫等。

## 功能特色

- **問答系統** - 向 Claude AI 提問任何問題
- **文字正式化** - 將文字改寫為正式且邏輯清晰的版本
- **會議摘要** - 為 AWS Cloud Support 會議生成摘要
- **翻譯功能** - 支援英文與繁體中文雙向翻譯
- **文字摘要** - 以繁體中文生成文字摘要
- **串流輸出** - 所有功能都支援即時串流回應

## 系統需求

- Python 3.12
- AWS 帳號與 Bedrock 存取權限
- 已設定 AWS 認證（透過 AWS CLI 或環境變數）

## 安裝

1. 克隆此專案：
```bash
git clone <repository-url>
cd raycast-bedrock-scripts
```

2. 安裝依賴套件（使用 pdm）：
```bash
pdm install
```

或使用 pip：
```bash
pip install -r requirements.txt
```

## AWS 設定

確保你的 AWS 認證已正確設定，並且有權限存取 Bedrock 服務。

查看可用的 Anthropic 模型：
```bash
aws bedrock list-foundation-models --region=us-west-2 --by-provider anthropic --query "modelSummaries[*].modelId"
```

## 使用方式

### 1. 問答系統 (Ask Me Anything)

向 Claude AI 提問任何問題：

```bash
# 直接輸入問題
python source/ask-me-anything.py "What is AWS Lambda?"

# 從檔案讀取問題
python source/ask-me-anything.py -f question.txt

# 儲存回應到檔案
python source/ask-me-anything.py "Explain Docker" -o answer.txt

# 使用 shell 腳本
./ask-me-anything.sh "Your question here"
```

### 2. 文字正式化

將文字改寫為正式且邏輯清晰的版本：

```bash
# 直接輸入文字
python source/formal-text-with-bedrock.py "casual text here"

# 從檔案讀取
python source/formal-text-with-bedrock.py -f input.txt -o formal.txt

# 使用 shell 腳本
./formal-text-with-bedrock.sh "text to formalize"
```

### 3. 會議摘要生成

為 AWS Cloud Support 會議生成摘要：

```bash
# 從檔案讀取會議記錄
python source/generate-taiwan-meeting-summarize.py -f meeting.txt

# 儲存摘要
python source/generate-taiwan-meeting-summarize.py -f meeting.txt -o summary.txt

# 使用 shell 腳本
./generate-taiwan-meeting-summarize.sh
```

### 4. 翻譯功能

#### 翻譯為英文：
```bash
# 翻譯繁體中文到英文
python source/translate-article-to-english.py "要翻譯的中文文字"

# 從檔案翻譯
python source/translate-article-to-english.py -f chinese.txt -o english.txt

# 使用 shell 腳本
./translate-article-to-english.sh
```

#### 翻譯為繁體中文：
```bash
# 翻譯英文到繁體中文
python source/translate-article-to-taiwannese.py "Text to translate"

# 從檔案翻譯
python source/translate-article-to-taiwannese.py -f english.txt -o chinese.txt

# 使用 shell 腳本
./translate-article-to-taiwannese.sh
```

### 5. 文字摘要（繁體中文）

生成繁體中文摘要：

```bash
# 直接輸入文字
python source/summarize-taiwanese-text-with-bedrock.py "長篇文字內容"

# 從檔案讀取
python source/summarize-taiwanese-text-with-bedrock.py -f article.txt -o summary.txt

# 使用 shell 腳本
./summarize-taiwanese-text-with-bedrock.sh
```

## 進階選項

所有腳本都支援以下選項：

```bash
--model MODEL_ID          # 指定使用的模型 ID
--max-tokens N            # 設定回應的最大 token 數（預設：4096）
--temperature T           # 設定生成溫度（預設：1.0）
-f, --file FILE          # 從檔案讀取輸入
-o, --output FILE        # 將輸出儲存到檔案
```

範例：
```bash
python source/ask-me-anything.py \
  --model anthropic.claude-3-5-sonnet-20241022-v2:0 \
  --max-tokens 2048 \
  --temperature 0.7 \
  -f input.txt \
  -o output.txt
```

## 專案結構

```
.
├── source/
│   ├── ask-me-anything.py                      # 問答系統
│   ├── formal-text-with-bedrock.py            # 文字正式化
│   ├── generate-taiwan-meeting-summarize.py   # 會議摘要
│   ├── translate-article-to-english.py        # 翻譯為英文
│   ├── translate-article-to-taiwannese.py     # 翻譯為繁體中文
│   ├── summarize-taiwanese-text-with-bedrock.py # 繁體中文摘要
│   ├── config_manager.py                       # 設定管理
│   ├── constants.py                            # 常數定義
│   └── AnthropicBedrock.py                    # Bedrock 客戶端
├── *.sh                                        # Shell 腳本包裝器
├── pyproject.toml                              # 專案設定
└── README.md                                   # 本文件
```

## 依賴套件

- `boto3` - AWS SDK for Python
- `anthropic[bedrock]` - Anthropic Claude SDK with Bedrock support
- `argparse` - 命令列參數解析

## 注意事項

- 所有腳本都使用串流輸出，可即時看到生成結果
- 輸入文字必須為 UTF-8 編碼
- 確保 AWS 認證有足夠權限存取 Bedrock 服務
- 使用 Bedrock 服務會產生費用，請注意用量

## 錯誤處理

腳本包含完整的錯誤處理：
- 檔案不存在檢查
- UTF-8 編碼驗證
- 空白輸入驗證
- 模型 ID 驗證
- API 錯誤處理

## 授權

請參考專案授權文件。

## 貢獻

歡迎提交 Issue 或 Pull Request。


# 项目简介

课程作业，一个用于演示 PayNow 充值与链上交互的简单 Flask 应用，包含基本页面与数据库示例。

# 在 Remix 部署合约

1. 打开 Remix: https://remix.ethereum.org
2. 上传 `smart_contract/deposit_money.sol` 和 `smart_contract/w1_paynow.sol`
3. 左侧选择 `Solidity Compiler`，选择合适版本后点击 `Compile`。
4. 切换到 `Deploy & Run Transactions`，在 `Environment` 选择 `WalletConnect` 。
5. 选择编译出的合约，点击 `Deploy`。
6. 部署完成后在同面板找到已部署合约实例，展开即可调用合约方法；将 Remix 部署结果中的合约地址和编译输出的 ABI 复制到 `templates/deposit.html` 和 `templates/paynow.html` 的 `contractAddress`、`contractABI`。

# 快速开始

1. 安装依赖：`pip install -r requirements.txt`
2. 启动服务：`python app.py`，默认运行在 `http://127.0.0.1:5000/`。
3. 访问页面：在浏览器打开主页，按网页内容进行演示。

# 部署到服务器

可在 Render 平台部署以满足 TT 需求；

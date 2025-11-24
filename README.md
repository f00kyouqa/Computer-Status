<div align="center">

# 🖥️ Discord PC Stats Monitor

**リアルタイムでPCのパフォーマンスをDiscordに表示**

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)](https://github.com)

*CPU・GPU・RAM使用率をDiscord Rich Presenceでスタイリッシュに表示*

[特徴](#-特徴) • [セットアップ](#-セットアップ) • [使い方](#-使い方) • [カスタマイズ](#-カスタマイズ) • [トラブルシューティング](#-トラブルシューティング)

</div>

---

## ✨ 特徴

<table>
<tr>
<td width="50%">

### 📊 リアルタイム監視
- **CPU使用率** の即座な表示
- **GPU使用率** のモニタリング (NVIDIA)
- **RAM使用率** の可視化
- **システムスペック** 情報の表示

</td>
<td width="50%">

### ⚙️ カスタマイズ可能
- 更新間隔の調整
- 表示項目の選択
- 経過時間の自動追跡
- 独自の画像設定

</td>
</tr>
</table>

---

## 📋 必要要件

| 項目 | 要件 |
|------|------|
| 🐍 **Python** | 3.7以上 |
| 💬 **Discord** | デスクトップアプリ（必須） |
| 🌐 **インターネット** | 接続必須 |
| 💻 **OS** | Windows 10/11, macOS, Linux |

---

## 🚀 セットアップ

### ステップ 1️⃣ : パッケージのインストール

```bash
pip install -r requirements.txt
```

<details>
<summary>📦 インストールされるパッケージ</summary>

| パッケージ | 用途 |
|-----------|------|
| `pypresence` | Discord Rich Presence API |
| `psutil` | システム情報取得 |
| `GPUtil` | GPU情報取得 (NVIDIA) |

</details>

### ステップ 2️⃣ : Discord Applicationの作成

> 💡 **なぜ必要？** Rich Presenceを使用するにはDiscord側でアプリケーションを登録する必要があります

1. **[Discord Developer Portal](https://discord.com/developers/applications)** にアクセス
2. 右上の **「New Application」** をクリック
3. アプリケーション名を入力 (例: `PC Stats Monitor`)
4. **「General Information」** タブから **Application ID** をコピー 📋
5. **(オプション)** カスタム画像をアップロード
   - **「Rich Presence」** → **「Art Assets」**
   - Asset Name: `computer`
   - 推奨サイズ: 512x512px 以上

### ステップ 3️⃣ : 設定ファイルの編集

`config.json` にApplication IDを設定:

```json
{
    "client_id": "1234567890123456789",  // ← ここにIDを貼り付け
    "update_interval": 15,
    "show_cpu": true,
    "show_gpu": true,
    "show_ram": true,
    "show_specs": true
}
```

---

## ⚙️ カスタマイズ

| オプション | 説明 | デフォルト | 推奨値 |
|-----------|------|----------|-------|
| `client_id` | Discord Application ID | 必須 | - |
| `update_interval` | 更新間隔（秒） | 15 | 15-60 |
| `show_cpu` | CPU使用率を表示 | `true` | - |
| `show_gpu` | GPU使用率を表示 | `true` | - |
| `show_ram` | RAM使用率を表示 | `true` | - |
| `show_specs` | スペック情報を表示 | `true` | - |

---

## 💻 使い方

### 起動方法

```bash
# 1. Discordアプリを起動
# 2. プログラムを実行
python discord_status.py
```

> ⚠️ **重要:** Discordデスクトップアプリが起動していないと動作しません

### 実行画面

```
==================================================
Discord Rich Presence - PC Stats Monitor
==================================================
システムスペック:
  CPU: Intel(R) Core(TM) i7-9700K CPU @ 3.60GHz
  コア数: 8 コア / 16 スレッド
  RAM: 32.0 GB
  GPU: NVIDIA GeForce RTX 3080
==================================================
Discord Rich Presenceに接続しました！
ステータス更新を開始します...
Ctrl+C で終了します。
==================================================
[14:32:15] ステータス更新: CPU: 45.2% | GPU: 32.1%
           RAM: 58.3% | 8C/16T | 32.0GB RAM
```

### Discord での表示

<div align="center">

```
┌─────────────────────────────────┐
│  🖥️  PC Stats Monitor          │
├─────────────────────────────────┤
│  CPU: 45.2% | GPU: 32.1%       │
│  RAM: 58.3% | 8C/16T | 32GB    │
│  ⏱️ 00:15:32 経過              │
└─────────────────────────────────┘
```

</div>

### 停止方法

`Ctrl + C` を押してプログラムを終了

---

## 🔧 トラブルシューティング

<details>
<summary><b>❌ 「接続できません」エラー</b></summary>

### 原因と対処法

| 問題 | 解決方法 |
|------|---------|
| 🚫 Discordが起動していない | デスクトップアプリを起動 (ブラウザ版は不可) |
| 🔑 Client IDが間違っている | Developer Portalで再確認 |
| 🛡️ ファイアウォールの制限 | Pythonを例外に追加 |

</details>

<details>
<summary><b>⚠️ GPU使用率が表示されない</b></summary>

### 対応GPU

| GPU | 対応状況 | 設定 |
|-----|---------|------|
| NVIDIA | ✅ 対応 | そのまま使用可能 |
| AMD | ❌ 非対応 | `show_gpu: false` に設定 |
| Intel | ❌ 非対応 | `show_gpu: false` に設定 |

**解決方法:**
```json
{
    "show_gpu": false  // ← falseに変更
}
```

</details>

<details>
<summary><b>📦 インストールエラー</b></summary>

### Windows の場合

管理者権限でコマンドプロンプトを開く:

```bash
# Pipのアップグレード
pip install --upgrade pip

# パッケージの再インストール
pip install -r requirements.txt
```

### Mac/Linux の場合

```bash
# Python 3を明示的に指定
pip3 install -r requirements.txt

# 権限エラーの場合
sudo pip3 install -r requirements.txt
```

</details>

<details>
<summary><b>⏱️ 更新間隔について</b></summary>

- **最小値:** 15秒（推奨）
- **理由:** CPU使用率の計測に1秒必要
- **推奨値:** 15-60秒

```json
{
    "update_interval": 30  // ← 30秒がバランス良好
}
```

</details>

---

## 📊 技術仕様

<table>
<tr>
<td width="33%">

### 🔌 使用API
- Discord Rich Presence (IPC)
- psutil (システム監視)
- GPUtil (GPU監視)

</td>
<td width="33%">

### 💻 対応OS
- ✅ Windows 10/11
- ✅ macOS
- ✅ Linux

</td>
<td width="33%">

### 🎮 GPU対応
- ✅ NVIDIA
- ❌ AMD
- ❌ Intel

</td>
</tr>
</table>

---

## ⚠️ 注意事項

> **重要:** このプログラムを使用する前に必ずお読みください

- 🔴 Discordデスクトップアプリが**必須**（ブラウザ版不可）
- 🔵 Application IDは公開しても問題ないが、念のため非公開推奨
- 🟢 CPU使用率の取得に1秒かかるため、実際の更新間隔は設定値+1秒
- 🟡 長時間起動する場合は、更新間隔を30秒以上に設定することを推奨

---

## 📚 参考資料

- 📖 [Discord Developer Portal](https://discord.com/developers/applications)
- 📖 [Discord Rich Presence Documentation](https://discord.com/developers/docs/rich-presence/how-to)
- 📖 [pypresence GitHub](https://github.com/qwertyquerty/pypresence)
- 🎥 [元動画: Discord Rich Presence Tutorial](https://youtu.be/Pa6T4ccloqo)

---

## 📄 ライセンス

このプロジェクトはMITライセンスの下で公開されています。  
教育目的で作成されており、使用は自己責任でお願いします。

---

<div align="center">

**Made with ❤️ for Discord Community**

⭐ 気に入ったらスターをお願いします！

</div>

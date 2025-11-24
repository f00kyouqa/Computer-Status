from pypresence import Presence
import psutil
import GPUtil
import time
import json
import platform
import os

def load_config():
    if not os.path.exists('config.json'):
        print("config.jsonが見つかりません。サンプルファイルを作成します。")
        sample_config = {
            "client_id": "YOUR_APPLICATION_CLIENT_ID_HERE",
            "update_interval": 15,
            "show_cpu": True,
            "show_gpu": True,
            "show_ram": True,
            "show_specs": True
        }
        with open('config.json', 'w', encoding='utf-8') as f:
            json.dump(sample_config, f, indent=4, ensure_ascii=False)
        print("config.jsonを編集してClient IDを設定してください。")
        print("Discord Developer Portalでアプリケーションを作成してください: https://discord.com/developers/applications")
        exit()
    
    with open('config.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def get_system_specs():
    cpu_name = platform.processor()
    cpu_cores = psutil.cpu_count(logical=False)
    cpu_threads = psutil.cpu_count(logical=True)
    ram_total = round(psutil.virtual_memory().total / (1024**3), 1)
    
    gpu_info = "N/A"
    try:
        gpus = GPUtil.getGPUs()
        if gpus:
            gpu_info = gpus[0].name
    except:
        pass
    
    return {
        "cpu": cpu_name,
        "cpu_cores": cpu_cores,
        "cpu_threads": cpu_threads,
        "ram": ram_total,
        "gpu": gpu_info
    }

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_gpu_usage():
    try:
        gpus = GPUtil.getGPUs()
        if gpus:
            return round(gpus[0].load * 100, 1)
    except:
        pass
    return None

def get_ram_usage():
    return psutil.virtual_memory().percent

def create_presence_data(config, specs):
    details = []
    state = []
    
    if config.get("show_cpu", True):
        cpu_usage = get_cpu_usage()
        details.append(f"CPU: {cpu_usage}%")
    
    if config.get("show_gpu", True):
        gpu_usage = get_gpu_usage()
        if gpu_usage is not None:
            details.append(f"GPU: {gpu_usage}%")
    
    if config.get("show_ram", True):
        ram_usage = get_ram_usage()
        state.append(f"RAM: {ram_usage}%")
    
    if config.get("show_specs", True):
        state.append(f"{specs['cpu_cores']}C/{specs['cpu_threads']}T | {specs['ram']}GB RAM")
    
    return {
        "details": " | ".join(details) if details else "System Monitor",
        "state": " | ".join(state) if state else None
    }

def main():
    print('='*50)
    print('Discord Rich Presence - PC Stats Monitor')
    print('='*50)
    
    config = load_config()
    
    if config["client_id"] == "YOUR_APPLICATION_CLIENT_ID_HERE":
        print("エラー: config.jsonにClient IDを設定してください。")
        print("Discord Developer Portalでアプリケーションを作成してください:")
        print("https://discord.com/developers/applications")
        return
    
    specs = get_system_specs()
    print('システムスペック:')
    print(f'  CPU: {specs["cpu"]}')
    print(f'  コア数: {specs["cpu_cores"]} コア / {specs["cpu_threads"]} スレッド')
    print(f'  RAM: {specs["ram"]} GB')
    print(f'  GPU: {specs["gpu"]}')
    print('='*50)
    
    start_time = int(time.time())
    client_id = config["client_id"]
    RPC = Presence(client_id)
    
    try:
        RPC.connect()
        print("Discord Rich Presenceに接続しました！")
        print("ステータス更新を開始します...")
        print("Ctrl+C で終了します。")
        print('='*50)
        
        while True:
            try:
                presence_data = create_presence_data(config, specs)
                
                RPC.update(
                    details=presence_data["details"],
                    state=presence_data["state"],
                    start=start_time,
                    large_image="computer",
                    large_text=f"{specs['cpu']}"
                )
                
                print(f'[{time.strftime("%H:%M:%S")}] ステータス更新: {presence_data["details"]}')
                if presence_data["state"]:
                    print(f'                    {presence_data["state"]}')
                
                time.sleep(config.get("update_interval", 15))
                
            except Exception as e:
                print(f'更新エラー: {e}')
                time.sleep(config.get("update_interval", 15))
                
    except KeyboardInterrupt:
        print("\nプログラムを終了します...")
        RPC.close()
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        print("\n接続できない場合:")
        print("1. Discordアプリケーションが起動しているか確認してください")
        print("2. Client IDが正しいか確認してください")
        print("3. Discord Developer Portalでアプリケーションを作成してください")

if __name__ == "__main__":
    main()

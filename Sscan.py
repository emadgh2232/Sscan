import requests
import os

banner = r"""
 ____ ____                      
 / ___/ ___|  ___ __ _ _ __      
 \___ \___ \ / __/ _` | '_ \     
 ___) |__) | (_| (_| | | | |    
 |____/____/ \___\__,_|_| |_|    
                                 
 [By Emad Alghamdi - OSINT Tool v1.0]
 --------------------------------
"""

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
}

def sscan():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(banner)

    username = input("Enter the username to scan: ")
    results = []
    
    social_media = {
        "GitHub": {"url": "https://github.com/{}", "key": "repositories"},
        "Telegram": {"url": "https://t.me/{}", "key": "tgme_page_extra"},
        "Chess.com": {"url": "https://www.chess.com/member/{}", "key": "joined"},
        "Steam": {"url": "https://steamcommunity.com/id/{}", "key": "inventory", "private_key": "this profile is private"},
        "Youtube": {"url": "https://www.youtube.com/@{}", "key": "subscribers"},
    }

    print(f"\n [+] Sscan is searching for {username}...\n")

    for site, info in social_media.items():
        formatted_url = info["url"].format(username)
        try:
            response = requests.get(formatted_url, headers=headers, timeout=7)
            content = response.text.lower() if response.text else ""
           

            if response.status_code == 200 and info["key"].lower() in content:
                res_text = f"[FOUND]: {site}: {formatted_url}"
                print(res_text)
                results.append(res_text) 
            elif site == "Steam" and "private_key" in info and info["private_key"].lower() in content:
                res_text = f"[FOUND/PRIVATE]: {site}: {formatted_url}"
                print(res_text)
                results.append(res_text)            
            else:
                print(f"[NOT FOUND]: {site}")
                
        except requests.exceptions.RequestException:
            print(f"[X] Error: Could not connect to {site}")
            
    print("-" * 45) 
    
    if results:
        file_name = f"{username}_results.txt"
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(f"Sscan Report for: {username}\n")
            f.write("-" * 30 + "\n")
            for line in results:
                f.write(line + "\n")
        print(f"[!] Results saved to: {file_name}")
    else:
        print("[!] No accounts found to save.")
        
    print("\n[+] Search Completed.")

if __name__ == "__main__":
    sscan()
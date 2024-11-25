import random
import time
from datetime import datetime

try:
    from colorama import Fore, Back, Style, init
    init(autoreset=True)
except ModuleNotFoundError:
    print("Thư viện 'colorama' chưa được cài đặt. Ứng dụng sẽ chạy mà không có màu sắc.")
    Fore = Back = Style = ""

# Danh sách các phòng
rooms = [
    "NHÀ KHO", "VĂN PHÒNG", "PHÒNG GIÁM SÁT", "PHÒNG NHÂN SỰ", 
    "PHÒNG TÀI VỤ", "PHÒNG GIÁM ĐỐC", "PHÒNG TRÒ CHUYỆN", "PHÒNG HỌP"
]

# Yêu cầu người dùng nhập ID
user_id = input(Fore.CYAN + "🆔 VUI LÒNG NHẬP ID ACC: ")

print(Fore.GREEN + f"✅ HELLO BY MHOA {user_id}! TOOL SẮP BẮT ĐẦU.")

while True:
    # Chọn ngẫu nhiên một phòng từ danh sách
    random_room = random.choice(rooms)
    
    # Tạo phần trăm chiến thắng ngẫu nhiên
    win_percentage = random.uniform(0, 100)
    
    # Lấy thời gian hiện tại
    current_time = datetime.now().strftime("%H:%M:%S")
    
    # Hiển thị phòng ngẫu nhiên, phần trăm chiến thắng, và thời gian hiện tại
    print(Back.BLUE + Fore.WHITE + f"🕒 THỜI GIAN: {current_time}")
    print(Back.BLUE + Fore.WHITE + f"🏠 BẮT ĐẦU: {random_room} - TỈ LỆ: {win_percentage:.2f}%")
    
    # Đếm ngược 60 giây
    for remaining_time in range(60, 0, -1):
        print(Fore.YELLOW + f"⏳ Đếm ngược: {remaining_time}s", end="\r")
        time.sleep(1)
    
    print(Fore.GREEN + "\nTiến Hành Bắt Đầu <Mhoa>🚀")
 

# Thư viện
import pygame
from pygame.locals import *
import random

pygame.init()

# Màu nền
cam = (255,69,0)
xanh_la = (76,208,56)
vang = (255,232,0)
do = (200,0,0)
trang = (255,255,255)
xanh_duong = (0,191,255)
den = (0,0,0)
nau = (139,69,19)
xam = (128,128,128)
#cửa sổ 
rong = 500
cao = 500
kich_thuoc_man_hinh = (rong, cao)
man_hinh = pygame.display.set_mode(kich_thuoc_man_hinh)
pygame.display.set_caption('Đua xe đường phố')

# Khởi tạo các biến
gameplay = False
toc_do = 2
diem = 0	

# Đường cho xe đua 
chieu_rong_duong = 300
chieu_rong_pho = 10
chieu_cao_pho = 50

# Hàng lang đường
hang_lang_trai = 150
hang_lang_giua = 250
hang_lang_phai = 350
hang_lang = [hang_lang_trai, hang_lang_phai, hang_lang_giua]
di_chuyen_hang_lang_y = 0

# Biên đường 
duong = (100, 0, chieu_rong_duong, cao)
mep_trai = (95, 0, chieu_rong_pho, cao)
mep_phai = (395, 0, chieu_rong_pho, cao)
# Vị trí xe người chơi
nguoi_choi_x = 250
nguoi_choi_y = 400
# Đối tượng xe lưu thông (vehicle)
class Xe(pygame.sprite.Sprite):
    def __init__(self, hinh_anh, x, y):
        pygame.sprite.Sprite.__init__(self)
        # Thay đổi kích thước hình ảnh
        ty_le_hinh_anh = 45 / hinh_anh.get_rect().width
        chieu_rong_moi = hinh_anh.get_rect().width * ty_le_hinh_anh
        chieu_cao_moi = hinh_anh.get_rect().height  * ty_le_hinh_anh
        self.hinh_anh = pygame.transform.scale(hinh_anh, (chieu_rong_moi, chieu_cao_moi))
        self.khoi = self.hinh_anh.get_rect()
        self.khoi.center = (x, y)
# Đối tượng xe người chơi
# ...
class XeNguoiChoi(Xe):
    def __init__(self, x, y):
        hinh_anh = pygame.image.load('images/car.png')
        super().__init__(hinh_anh, x, y)
# ...

# Nhóm sprite
nhom_nguoi_choi = pygame.sprite.Group()
nhom_xe = pygame.sprite.Group()
# Tạo xe người chơi
nguoi_choi = XeNguoiChoi (nguoi_choi_x, nguoi_choi_y)
nhom_nguoi_choi.add(nguoi_choi)
# Nạp các hình ảnh xe lưu thông
ten_hinh_anh = ['pickup_truck.png', 'semi_trailer.png', 'taxi.png', 'van.png']
hinh_anh_xe = []
for ten in ten_hinh_anh:
    hinh_anh = pygame.image.load('images/' + ten)
    hinh_anh_xe.append(hinh_anh)

# Thiết lập FPS của trò chơi
dong_ho = pygame.time.Clock()
fps = 120
 
# Vòng lặp xử lý
dang_chay = True
while dang_chay:
    dong_ho.tick(fps)
    for su_kien in pygame.event.get():
        if su_kien.type == QUIT:
            dang_chay = False

    # Vẽ địa hình
    man_hinh.fill(nau)
    # Vẽ đường và phố
    pygame.draw.rect(man_hinh, xam, duong)
    # Vẽ mep-hàng lang đường
    pygame.draw.rect(man_hinh, vang, mep_trai)
    pygame.draw.rect(man_hinh, vang, mep_phai)
    # Vẽ hàng lang đường 	   	
    di_chuyen_hang_lang_y += toc_do * 2
    if di_chuyen_hang_lang_y >= chieu_cao_pho * 2:
        di_chuyen_hang_lang_y = 0
    for y in range(chieu_cao_pho * -2, cao, chieu_cao_pho * 2):
        pygame.draw.rect(man_hinh, trang, (hang_lang_trai + 45, y + di_chuyen_hang_lang_y, chieu_rong_pho, chieu_cao_pho))
        pygame.draw.rect(man_hinh, trang, (hang_lang_giua + 45, y + di_chuyen_hang_lang_y, chieu_rong_pho, chieu_cao_pho))

    # Vẽ xe người chơi
    nhom_nguoi_choi.draw(man_hinh)

    if len(nhom_xe) < 2:
        them_xe = True
        for xe in nhom_xe:
            if xe.khoi.top < xe.khoi.height * 1.5:
                them_xe = False
            if them_xe:
                hang = random.choice(hang_lang)
                hinh_anh = random.choice(hinh_anh_xe)
                xe = Xe(hinh_anh, hang, cao / -2)
                nhom_xe.add(xe)

    for xe in nhom_xe:
        xe.khoi.y += toc_do

        if xe.khoi.top >= cao:
            xe.kill()
            diem += 1

            if diem > 0 and diem % 5 == 0:
                toc_do += 1

    nhom_xe.draw(man_hinh)

    # Cập nhật phần hiển thị
    pygame.display.update()

pygame.quit()

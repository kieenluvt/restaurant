from acount import register, login, forget_password, acount_admin, acount_customer, acount_staff
from user import Admin, Customer, Staff

def admin_main(admin):
    while True:
        print("\nADMIN MENU")
        print("1. Xem thông tin cá nhân")
        print("2. Tạo tài khoản staff")
        print("0. Đăng xuất")
        choose = input("Chọn(0-2): ").strip()

        if choose == '1':
            print(admin)
        elif choose == '2':
            name = input("Tên staff: ").strip()
            phone = input("SĐT: ").strip()
            email = input("Email: ").strip()
            password = input("Password: ").strip()
            gender = "khác"

            # Kiểm tra email đã tồn tại chưa
            if any(st.email == email for st in acount_staff):
                print("Email đã tồn tại!")
                continue

            new_staff = Staff(name, phone, email, password, gender)
            acount_staff.append(new_staff)
            print("Tạo tài khoản staff thành công!")

        elif choose == '0':
            break
        else:
            print("Lựa chọn không hợp lệ!")

def staff_main(staff):
    while True:
        print("\nSTAFF MENU")
        print("1. Xem thông tin cá nhân")
        print("0. Đăng xuất")
        choose = input("Chọn(0-1): ").strip()

        if choose == '1':
            print(staff)
        elif choose == '0':
            break
        else:
            print("Lựa chọn không hợp lệ!")

def customer_main(customer):
    while True:
        print("\nCUSTOMER MENU")
        print("1. Xem thông tin cá nhân")
        print("0. Đăng xuất")
        choose = input("Chọn(0-1): ").strip()

        if choose == '1':
            print(customer)
        elif choose == '0':
            break
        else:
            print("Lựa chọn không hợp lệ!")

def main():
    while True:
        print("\nHỆ THỐNG RESTAURANT")
        print("1. Đăng ký")
        print("2. Đăng nhập")
        print("3. Quên mật khẩu")
        print("0. Thoát")
        choose = input("Chọn(0-3): ").strip()

        if choose == '1':
            register()
        elif choose == '2':
            user = login()
            if not user:
                print("Sai email hoặc mật khẩu!")
                continue

            # Phân loại user
            if user in acount_admin:
                admin_main(user)
            elif user in acount_staff:
                staff_main(user)
            elif user in acount_customer:
                customer_main(user)
        elif choose == '3':
            forget_password()
        elif choose == '0':
            print("Thoát hệ thống")
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()

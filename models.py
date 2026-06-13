"""File chứa các class đối tượng chính (sản phẩm, hoá đơn, chi tiết hoá đơn, khách hàng)"""
class Product:
    def __init__(self, product_id, name, price, unit, category, min_quantity, discount_rate):
        self.product_id = product_id                    # Mã sản phẩm
        self.name = name                                # Tên sản phẩm
        self.price = price                              # Giá tiền
        self.unit = unit                                # Đơn vị
        self.category = category                        # Loại sản phẩm (đồ ăn, đồ uống,...)
        self.min_quantity = min_quantity                # Số lượng tối thiểu để được chiết khấu
        self.discount_rate = discount_rate              # Phần trăm chiết khấu

class Bill:
    def __init__(self, bill_id, customer_id, time_created, vat = 0.1):
        self.bill_id = bill_id                          # Mã hoá đơn
        self.customer_id = customer_id                  # Mã khách hàng
        self.time_created = time_created                # Thời gian tạo
        self.vat = vat                                  # Thuế VAT    
        self.amount_before_vat = 0                      # Tổng tiền trước VAT
        self.final_amount = 0                           # Tổng tiền phải trả
        self.details = []                               # Danh sách lưu chi tiết hoá đơn
        self.status = 1                                 # Trạng thái (1 = Hợp lệ, 0 = Đã huỷ)

class BillDetail:
    def __init__(self, product_id, quantity, current_price, current_discount):
        self.product_id = product_id                    # Mã sản phẩm
        self.quantity = quantity                        # Số lượng mua
        self.current_price = current_price              # Giá bán tại thời điểm lập hoá đơn
        self.current_discount = current_discount        # Chiết khấu tại thời điểm lập hoá đơn

class Customer:
    def __init__(self, customer_id, name, phone, gender, customer_type):
        self.customer_id = customer_id                  # Mã khách hàng
        self.name = name                                # Tên khách hàng
        self.phone = phone                              # Số điện thoại
        self.gender = gender                            # Giới tính (0 = nam, 1 = nữ, 2 = khác)
        self.customer_type = customer_type              # Loại khách hàng (0 = khách vãng lai, 1 = khách đã đăng ký)


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
    def __init__(self, bill_id, customer_id, time_created, amount_before_vat, vat, final_amount):
        self.bill_id = bill_id                          # Mã hoá đơn
        self.customer_id = customer_id                  # Mã khách hàng
        self.time_created = time_created                # Thời gian tạo    
        self.amount_before_vat = amount_before_vat      # Tổng tiền trước VAT
        self.vat = vat                                  # Thuế VAT
        self.final_amount = final_amount                # Tổng tiền phải trả
        self.details = []                               # Danh sách lưu chi tiết hoá đơn

class BillDetail:
    def __init__(self, product_id, bill_id, quantity, current_price):
        self.product_id = product_id                    # Mã sản phẩm
        self.bill_id = bill_id                          # Mã hoá đơn
        self.quantity = quantity                        # Số lượng mua
        self.current_price = current_price              # Giá bán tại thời điểm lập hoá đơn

class Customer:
    def __init__(self, customer_id, name, phone, gender, customer_type):
        self.customer_id = customer_id                  # Mã khách hàng
        self.name = name                                # Tên khách hàng
        self.phone = phone                              # Số điện thoại
        self.gender = gender                            # Giới tính
        self.customer_type = customer_type              # Loại khách hàng


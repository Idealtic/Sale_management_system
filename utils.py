"""Các công cụ khác (ví dụ xử lý chuỗi, xoá màn hình,... không liên quan tới nghiệp vụ chính)"""
import os
from models import Product, Customer, Bill, BillDetail
from data_structure import DoublyLinkedList

def load_file(file_path, parse_func):
    """
    Nạp dữ liệu vào file để hệ thống sử dụng.
    Nhận đường dẫn của file và hàm parse_func chuyển đổi từ chữ thành đối tượng (tuỳ thuộc vào đối tượng) làm tham số.
    """
    data_list = DoublyLinkedList()
    if not os.path.exists(file_path):
        return data_list
    
    with open(file_path, "r", encoding = "utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split(',')

            parsed_object = parse_func(parts)
            data_list.append(parsed_object)
    
    return data_list

def save_file(file_path, data_list, format_func):
    """
    Ghi dữ liệu mới vào file
    Nnhận đường dẫn của file, danh sách cần lưu, hàm format_func chuyển đổi từ đối tượng thành chữ (tuỳ thuộc vào đối tượng) làm tham số.
    """
    with open(file_path, "w", encoding = "utf-8") as file:
        for item in data_list:
            line_string = format_func(item)
            file.write(line_string + "\n")

def parse_product(parts):
    return Product(
        parts[0],
        parts[1],
        float(parts[2]),
        parts[3],
        parts[4],
        int(parts[5]),
        float(parts[6])
    )

def format_product(product):
    return f"{product.product_id},{product.name},{product.price},{product.unit},{product.category},{product.min_quantity},{product.discount_rate}"

def parse_customer(parts):
    return Customer(
        parts[0],
        parts[1],
        parts[2],
        int(parts[3]),
        int(parts[4])
    )

def format_customer(customer):
    return f"{customer.customer_id},{customer.name},{customer.phone},{customer.gender},{customer.customer_type}"

def parse_bill(parts):
    bill = Bill(parts[0], parts[1], parts[2], parts[3])
    for i in range(4, len(parts)):
        detail_parts = parts[i].split(';')

        bill_detail = BillDetail(
            detail_parts[0],
            int(detail_parts[1]),
            float(detail_parts[2]),
            float(detail_parts[3]),
        )

        bill.details.append(bill_detail)
    
    return bill

def format_bill(bill):
    result_string = f"{bill.bill_id},{bill.customer_id},{bill.time_created},{bill.vat}"
    
    for detail in bill.details:
        detail_string = f"{detail.product_id};{detail.quantity};{detail.current_price};{detail.current_discount}"
        result_string += f",{detail_string}" 

    return result_string

def load_products(file_path):
    return load_file(file_path, parse_product)

def save_product(file_path, product_list):
    return save_file(file_path, product_list, format_product)

def load_customer(file_path):
    return load_file(file_path, parse_customer)

def save_customers(file_path, customer_list):
    save_file(file_path, customer_list, format_customer)

def load_bill(file_path):
    return load_file(file_path, parse_bill)

def save_bills(file_path, bill_list):
    save_file(file_path, bill_list, format_bill)

 

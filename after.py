def calculate_total(products):
    """计算商品总价（含税率）"""
    total = 0
    for p in products:
        if p["type"] == "food":
            total += p["price"] * 1.08
        elif p["type"] == "electronics":
            total += p["price"] * 1.13
    return total


def print_details(products, rate, total, is_refund=False):
    """打印订单/退款详情"""
    title = "退款详情" if is_refund else "订单详情"
    rate_text = "退款比例" if is_refund else "折扣"
    print(f"{title}：")
    print("商品列表：")
    for p in products:
        print(f"{p['name']} - {p['price']}元")
    print(f"{rate_text}：{rate*100}%")
    print(f"最终金额：{total:.2f}元")


def calculate_order_price(products, discount):
    """计算订单价格并打印详情"""
    total = calculate_total(products)
    if discount > 0:
        total = total * (1 - discount)
    print_details(products, discount, total)
    return total


def calculate_refund_price(products, refund_rate):
    """计算退款金额并打印详情"""
    total = calculate_total(products)
    if refund_rate > 0:
        total = total * refund_rate
    print_details(products, refund_rate, total, is_refund=True)
    return total


# 测试代码
if __name__ == "__main__":
    order_products = [
        {"name": "面包", "type": "food", "price": 10},
        {"name": "耳机", "type": "electronics", "price": 200}
    ]
    calculate_order_price(order_products, 0.1)
    calculate_refund_price(order_products, 0.5)

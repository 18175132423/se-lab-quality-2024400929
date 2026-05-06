def calculate_order_price(products, discount):
    # 未使用的变量
    unused_var = "我是多余的变量"
    total = 0
    # 计算总价
    for p in products:
        if p["type"] == "food":
            total += p["price"] * 1.08  # 食品税率8%
        elif p["type"] == "electronics":
            total += p["price"] * 1.13  # 电子产品税率13%
    # 应用折扣
    if discount > 0:
        total = total * (1 - discount)
    # 打印订单
    print("订单详情：")
    print("商品列表：")
    for p in products:
        print(f"{p['name']} - {p['price']}元")
    print(f"折扣：{discount*100}%")
    print(f"最终总价：{total:.2f}元")
    return total


def calculate_refund_price(products, refund_rate):
    # 未使用的变量
    another_unused_var = "我也是多余的变量"
    total = 0
    # 计算退款金额
    for p in products:
        if p["type"] == "food":
            total += p["price"] * 1.08  # 食品税率8%
        elif p["type"] == "electronics":
            total += p["price"] * 1.13  # 电子产品税率13%
    # 应用退款比例
    if refund_rate > 0:
        total = total * refund_rate
    # 打印退款单
    print("退款详情：")
    print("商品列表：")
    for p in products:
        print(f"{p['name']} - {p['price']}元")
    print(f"退款比例：{refund_rate*100}%")
    print(f"退款总额：{total:.2f}元")
    return total


# 测试代码
if __name__ == "__main__":
    order_products = [
        {"name": "面包", "type": "food", "price": 10},
        {"name": "耳机", "type": "electronics", "price": 200}
    ]
    calculate_order_price(order_products, 0.1)
    calculate_refund_price(order_products, 0.5)

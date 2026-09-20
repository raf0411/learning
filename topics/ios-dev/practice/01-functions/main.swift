func shippingFee(order_total: Int) -> Int {
    if order_total >= 50 {
        return 0
    } else {
        return 5
    }
}

print(shippingFee(order_total: 50))
print(shippingFee(order_total: 49))
print(shippingFee(order_total: 51))

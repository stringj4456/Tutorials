# This program shows an example of a user defined exception

class CouponError(Exception):
    def __init__(self, coupon):
        self.coupon = coupon

    def __str__(self):
        return (self.coupon) + " is an invalid coupon"


coupon_list = ["FREEAUG", "STUDENT", "FREEWEEK"]
x = str(input("Enter a coupon code: "))

if x not in coupon_list:
    raise CouponError(x)
print("Coupon is valid")

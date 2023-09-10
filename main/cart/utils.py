# import json
# from orders.models import Order, OrderItem, Customer
# from menu.models import Menu
#
#
# def cookie_cart(request):
#     # Create empty cart for now for non-logged in user
#     try:
#         cart = json.loads(request.COOKIES['cart'])
#     except Exception as e:
#         cart = {}
#         print('Error:', e)
#
#     items = []
#     order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
#     cart_items = order['get_cart_items']
#
#     for i in cart:
#         # We use try block to prevent items in cart that may have been removed from causing error
#         try:
#             if cart[i]['quantity'] > 0:  # items with negative quantity = lot of freebies
#                 cart_items += cart[i]['quantity']
#
#                 dish = Dish.objects.get(id=i)
#                 total = (dish.price * cart[i]['quantity'])
#
#                 order['get_cart_total'] += total
#                 order['get_cart_items'] += cart[i]['quantity']
#
#                 item = {
#                     'id': dish.id,
#                     'dish': {
#                         'id': dish.id,
#                         'name': dish.name,
#                         'price': dish.price,
#                         'description': dish.description,
#                         'weight': dish.weight,
#                         'category': dish.category,
#                         'imageURL': dish.image,
#                     },
#                     'amount': cart[i]['quantity'] if cart[i]['quantity'] <= dish.amount else dish.amount,
#                     'get_total': total,
#                 }
#                 items.append(item)
#         except Exception as e:
#             print('Error', e)
#             pass
#     return {'cart_items': cart_items, 'order': order, 'items': items}
#

import math
import numpy as np
from datetime import datetime

def get_items():
    items = []
    print("Enter shipment items (name, cost, quantity).")
    print("Type 'done' as item name when finished.\n")
    while True:
        name = input("Enter item name (or 'done' to finish): ")
        if name.lower() == "done":
            break
        cost_input = input(f"Enter cost for '{name}': ")
        qty_input = input(f"Enter quantity for '{name}': ")
        try:
            cost = float(cost_input)
            qty = int(qty_input)
            if cost < 0:
                cost = abs(cost)
            if qty < 0:
                qty = abs(qty)
            items.append({"name": name, "cost": cost, "quantity": qty})
        except ValueError:
            print("Invalid cost or quantity. This item is skipped.\n")
            continue
        print("Item added.\n")
    if len(items) == 0:
        print("No valid shipment items entered. Exiting program.")
        exit()
    return items

def get_conditions():
    print("\nEnter extra details (press Enter for default value).")
    handling_input = input("Enter fixed handling charge (default 100): ")
    handling_charge = 100.0 if handling_input.strip() == "" else float(handling_input)
    gst_input = input("Enter GST percentage (default 18): ")
    gst_percent = 18.0 if gst_input.strip() == "" else float(gst_input)
    discount_limit_input = input("Enter minimum subtotal for discount (default 1000): ")
    discount_limit = 1000.0 if discount_limit_input.strip() == "" else float(discount_limit_input)
    discount_percent_input = input("Enter discount percentage (default 10): ")
    discount_percent = 10.0 if discount_percent_input.strip() == "" else float(discount_percent_input)
    return handling_charge, gst_percent, discount_limit, discount_percent

def calculate_subtotals(items):
    costs = np.array([item["cost"] for item in items])
    quantities = np.array([item["quantity"] for item in items])
    total_per_item = costs * quantities
    subtotal = np.sum(total_per_item)
    return total_per_item, subtotal

def calculate_totals(subtotal, handling_charge, gst_percent, discount_limit, discount_percent):
    discount_amount = (discount_percent / 100.0) * subtotal if subtotal >= discount_limit else 0.0
    amount_after_discount = subtotal - discount_amount
    gst_base = amount_after_discount + handling_charge
    gst_amount = (gst_percent / 100.0) * gst_base
    final_total = gst_base + gst_amount
    return discount_amount, amount_after_discount, gst_base, gst_amount, final_total

def print_bill(items, total_per_item, subtotal, discount_amount, amount_after_discount, gst_base, gst_amount, final_total, handling_charge, gst_percent):
    print("\n========== SHIPMENT BILL ==========")
    current_time = datetime.now()
    print("Bill generated on:", current_time.strftime("%Y-%m-%d %H:%M:%S"))
    print("\nItems and their shipment cost (cost * quantity):")
    for i, item in enumerate(items, start=1):
        print(f"  {i}. {item['name']} | Cost: {item['cost']} x Qty: {item['quantity']} = {round(total_per_item[i-1], 2)}")
    print("-----------------------------------")
    print("Number of unique items    :", len(items))
    average_cost = np.mean(total_per_item) if len(total_per_item) > 0 else 0
    print("Average cost per item set :", round(average_cost, 2))
    print("Subtotal (items total)    :", round(subtotal, 2))
    print("Handling charge           :", round(handling_charge, 2))
    print("Discount applied          :", round(discount_amount, 2))
    print("Amount after discount     :", round(amount_after_discount, 2))
    print("GST percentage            :", gst_percent, "%")
    print("GST base amount           :", round(gst_base, 2))
    print("GST amount                :", round(gst_amount, 2))
    print("-----------------------------------")
    final_total_rounded = math.ceil(final_total * 100) / 100
    print("FINAL TOTAL SHIPMENT COST :", final_total_rounded)
    print("===================================\n")
    print("Thank you for using the Shipment Cost Calculator!")

def main():
    items = get_items()
    handling_charge, gst_percent, discount_limit, discount_percent = get_conditions()
    total_per_item, subtotal = calculate_subtotals(items)
    discount_amount, amount_after_discount, gst_base, gst_amount, final_total = calculate_totals(
        subtotal, handling_charge, gst_percent, discount_limit, discount_percent)
    print_bill(items, total_per_item, subtotal, discount_amount, amount_after_discount, gst_base, gst_amount, final_total, handling_charge, gst_percent)

if __name__ == "__main__":
    main()

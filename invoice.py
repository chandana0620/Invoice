
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Function to create invoice PDF
def create_invoice(order_id, customer_name, product_details, total_price, filename='invoice.pdf'):
    # Create a canvas object
    c = canvas.Canvas(filename, pagesize=letter)

    # Set up font
    c.setFont("Times-Roman", 12)

    # Title of the invoice
    c.drawString(200, 750, "Invoice")

    # Order ID
    c.drawString(50, 700, f"Order ID: {order_id}")

    # Customer Name
    c.drawString(50, 675, f"Customer: {customer_name}")

    # Product details heading
    c.drawString(50, 650, "Product Details:")
    y_position = 630  # Starting Y position for product listing

    # Loop through the product details and display each product line
    for product in product_details:
        product_name = product.get("name", "Unknown Product")
        quantity = product.get("quantity", 0)
        price = product.get("price", 0.0)
        line_total = quantity * price
        c.drawString(50, y_position, f"{product_name} (x{quantity}) - {price:.2f} each")
        c.drawString(300, y_position, f"Total: {line_total:.2f}")
        y_position -= 20

    # Display total price at the bottom
    c.drawString(50, y_position - 30, f"Total Price: {total_price:.2f}")

    # Save the PDF
    c.save()

# Sample data to generate the invoice
order_id = "ORD123456"
customer_name = "Priya"
product_details = [
    {"name": "TV", "quantity": 1, "price": 50000},
    {"name": "Couch", "quantity": 2, "price": 30000},
    {"name": "Washing machine", "quantity": 1, "price": 45000},
]
total_price = sum(item["quantity"] * item["price"] for item in product_details)

# Call the function to create the invoice
create_invoice(order_id, customer_name, product_details, total_price)

print("Invoice generated successfully!")

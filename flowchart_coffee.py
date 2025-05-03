from graphviz import Digraph

# Create a flowchart using Graphviz
dot = Digraph(format='pdf')
dot.attr(size='8', rankdir='TB')

# Start
dot.node('Start', 'Start', shape='ellipse')

# User Prompt
dot.node('Prompt', 'Prompt user: What would you like? (espresso/latte/cappuccino)', shape='parallelogram')

# Check Input
dot.node('Check', 'Check user input', shape='diamond')

# Actions
dot.node('Off', 'Turn off machine', shape='parallelogram')
dot.node('Report', 'Print report', shape='parallelogram')
dot.node('Check_Resources', 'Check resources sufficient?', shape='diamond')

# If resources insufficient
dot.node('Not_Enough', 'Sorry, not enough resources.', shape='parallelogram')

# Process coins
dot.node('Insert_Coins', 'Prompt user to insert coins', shape='parallelogram')
dot.node('Calculate', 'Calculate total amount', shape='parallelogram')

# Check transaction
dot.node('Check_Money', 'Check if enough money inserted', shape='diamond')

# If not enough money
dot.node('Refund', 'Money refunded', shape='parallelogram')

# If enough money
dot.node('Deduct_Resources', 'Deduct resources from machine', shape='parallelogram')
dot.node('Give_Change', 'Return change if needed', shape='parallelogram')
dot.node('Dispense', 'Dispense coffee & Enjoy!', shape='parallelogram')

# End
dot.node('End', 'End', shape='ellipse')

# Flow connections
dot.edge('Start', 'Prompt')
dot.edge('Prompt', 'Check')

dot.edge('Check', 'Off', label='User inputs "off"')
dot.edge('Check', 'Report', label='User inputs "report"')
dot.edge('Check', 'Check_Resources', label='User selects a drink')

dot.edge('Check_Resources', 'Not_Enough', label='Not enough resources')
dot.edge('Check_Resources', 'Insert_Coins', label='Enough resources')

dot.edge('Insert_Coins', 'Calculate')
dot.edge('Calculate', 'Check_Money')

dot.edge('Check_Money', 'Refund', label='Not enough money')
dot.edge('Check_Money', 'Deduct_Resources', label='Enough money')

dot.edge('Deduct_Resources', 'Give_Change')
dot.edge('Give_Change', 'Dispense')

dot.edge('Dispense', 'Prompt', label='Repeat process')
dot.edge('Off', 'End')

# Save as PDF
pdf_path = "/mnt/data/Coffee_Machine_Flowchart"
dot.render(pdf_path)
pdf_path + ".pdf"

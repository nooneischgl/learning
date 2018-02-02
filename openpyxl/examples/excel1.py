#!/usr/bin/env python3
import openpyxl

# Creating and Saving Excel Documents

wb = openpyxl.Workbook()
print(wb.get_sheet_names())
sheet = wb.get_active_sheet()
print(sheet.title)
sheet.title = 'Spam Bacon Eggs Sheet'
print(wb.get_sheet_names())

wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.get_active_sheet()
sheet.title = 'Spam Spam Spam'
wb.save('example_copy.xlsx')

### Create Sheets
wb = openpyxl.Workbook()
print(wb.get_sheet_names())
wb.create_sheet()
print(wb.get_sheet_names())
wb.create_sheet(index=0, title='First Sheet')
print(wb.get_sheet_names())
wb.create_sheet(index=2, title='Middle Sheet')
print(wb.get_sheet_names())

### Remove Sheets
print()
print(wb.get_sheet_names())
wb.remove_sheet(wb.get_sheet_by_name('Middle Sheet'))
wb.remove_sheet(wb.get_sheet_by_name('Sheet1'))
print(wb.get_sheet_names())
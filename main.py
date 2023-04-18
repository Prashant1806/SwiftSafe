import os
import shutil
from compare import compare_accounts
from report import PDFReport
from config import SCREENSHOT_DIR, REPORT_DIR

def main():
    # Get input from user
    account1 = input("Enter first Instagram account: ")
    account2 = input("Enter second Instagram account: ")

    # Compare accounts and generate report
    screenshots, text = compare_accounts(account1, account2)
    report = PDFReport()
    report.generate_report(screenshots, text)

    # Move screenshots to screenshots directory
    for screenshot in screenshots:
        shutil.move(screenshot, os.path.join(SCREENSHOT_DIR, os.path.basename(screenshot)))

    # Move report to reports directory
    shutil.move('report.pdf', os.path.join(REPORT_DIR, f'{account1}_vs_{account2}.pdf'))

if __name__ == '__main__':
    main()

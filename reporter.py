import datetime

def generate_report(target_ip, open_ports):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    report = f"""
    =========================================
       RED TEAM - AUTOMATED SECURITY REPORT
    =========================================
    [+] Target IP     : {target_ip}
    [+] Scan Time     : {current_time}
    [+] Status        : Completed Successfully
    
    -----------------------------------------
    [!] DISCOVERED OPEN PORTS:
    -----------------------------------------
    """
    
    for port in open_ports:
        report += f"    -> Port {port} is OPEN (Requires Review)\n"
        
    report += """
    -----------------------------------------
    [*] Recommendation: Ensure unused ports 
        are closed and update router firmware.
    =========================================
    """
    return report

if __name__ == "__main__":
    # تجربة لنتائج فحص الراوتر التي ظهرت معك سابقاً
    target = "192.168.1.1"
    ports_found = [80, 443, 22]
    
    print("[*] Generating security report...")
    final_output = generate_report(target, ports_found)
    print(final_output)
    
    # حفظ التقرير في ملف نصي تلقائياً
    with open("security_report.txt", "w") as f:
        f.write(final_output)
    print("[+] Report saved successfully as 'security_report.txt'!")


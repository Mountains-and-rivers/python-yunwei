import time
from ssh import sshExec

# if __name__ == "__main__":
#     ips='''47.110.149.198
# 47.110.149.198
# 47.110.149.198
# 47.110.149.198
# 47.110.149.198
# 47.110.149.198
# '''
#     #根据n分割ip
#     ip_list = ips.split("\n")
#     username = "moja"#主机用户名
#     password = "Image0@Huawei123"#主机密码
#     while (True):
#         ipl = ip_list[0:2]#每次拿2个
#         for ip in ipl:
#             print("11111111111111111111------------------------------000000000000000000000000000000000000000")
#             ssh = sshExec.creatSShConnectOb("47.110.149.198",22,"moja","Image0@Huawei123")
#             chanelSSHOb = ssh.invoke_shell()
            
#             sshCmd = """ whoami
#                      df -h """        
#             sshCmd = 'su -'
#             if sshExec.chanel_exe_cmd(chanelSSHOb, sshCmd).endswith(u"Password: "):
#                 sshCmd = "Image0@Huawei123"
#                 sshExec.chanel_exe_cmd(chanelSSHOb, sshCmd)
            
#             sshCmd = """ whoami
#                      df -h """  
#             sshExec.chanel_exe_cmd(chanelSSHOb, sshCmd)
#         time.sleep(5)ßßßßß
#         del ip_list[0:2]#删除2个
#         if len(ip_list) == 0: 
#             print("773894692q83649862q3")
#             break#如果没了退出

if __name__ == '__main__':
#    sshExec.sftp_upload_file("47.110.149.198","moja","Image0@Huawei123","/home/moja/test.txt", "test.txt",timeout=10)
     sshExec.sftp_down_file("47.110.149.198","moja","Image0@Huawei123","/home/moja/test.txt", "test.txt",timeout=10)
    